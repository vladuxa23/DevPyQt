import sys
import time

import requests
from PySide2 import QtCore, QtWidgets, QtGui

from ui.clientdb import Ui_Form
from settings import client
from ui.icons import resource


class PushButtonDelegate(QtWidgets.QStyledItemDelegate):
    clicked = QtCore.Signal(QtCore.QModelIndex)

    def paint(self, painter, option, index):
        if (isinstance(self.parent(), QtWidgets.QAbstractItemView)
                and self.parent().model() is index.model()):
            self.parent().openPersistentEditor(index)

    def createEditor(self, parent, option, index):
        button = QtWidgets.QPushButton(parent)
        button.clicked.connect(lambda *args, ix=index: self.clicked.emit(ix))
        return button

    def setEditorData(self, editor, index):
        editor.setText("Скачать")

    def setModelData(self, editor: QtWidgets.QWidget, model: QtCore.QAbstractItemModel,
                     index: QtCore.QModelIndex) -> None:
        pass

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        resource.qInitResources()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/rss.ico")))
        self.file_list = []  # список файлов для отправки
        self.download_list_files = []  # список файлов для загрузки

        self.bucket_name = None  # Название корзины min.io для загрузки файла

        self.ui = Ui_Form()  # основное окно
        self.about_window = AboutWindow()  # инициализируем окно about

        self.ui.setupUi(self)

        self.set_url()  # Устанавливаем url подключения по умолчанию http://127.0.0.1:8000

        # Проверяем статус подключения при загрузке программы
        self.ui.pb_reconnect.clicked.connect(self.initStatusConnection)  # Кнопка reconnect

        # Устанавливаем неактивные кнопки по умолчанию
        self.ui.pb_download_all.setEnabled(False)
        self.ui.pb_delete.setEnabled(False)
        self.ui.pd_send_file.setEnabled(False)

        # Сигналы
        self.ui.pd_open_file.clicked.connect(self.add_files_to_send)
        self.ui.pd_send_file.clicked.connect(self.post_file)
        self.ui.pb_get_info.clicked.connect(self.get_info)
        self.ui.pb_download_all.clicked.connect(self.save_all_files)
        self.ui.pb_delete.clicked.connect(self.delete_files)
        self.ui.pb_about.clicked.connect(self.open_about)

        # Подключение окна Connection
        self.conn_window = ConnectionWindow()
        self.ui.pb_connect_adress.clicked.connect(self.open_connection)
        self.conn_window.urlLineEdit.setText(self.url)
        self.conn_window.data[str].connect(self.set_url)

        # Делегаты
        self.openDelegate = PushButtonDelegate()
        self.openDelegate.clicked.connect(self.download_file)

        # Загрузочное окно
        self.loadGUI()

    def loadGUI(self):
        """
        Загрузочное окно
        """
        splash = QtWidgets.QSplashScreen(
            QtGui.QPixmap(":/logo/logo_project.png").scaled(500, 500))  # Подключаем заставку
        splash.show()
        time.sleep(1)
        splash.finish(self)
        self.show()

    def set_url(self, url='http://127.0.0.1:8000'):
        """
        Установка url для подключения к сервису
        :param url: Строковое значение получаемое из окна Connection
        :return: Строка url
        """
        self.ui.labelUrl.setText(url)
        self.url = url
        self.initStatusConnection()  # Проверяем подключение

    def initStatusConnection(self):
        """
        Проверяем подключение к серверу.
        """
        try:
            resp = requests.get(self.url)
            if resp.status_code == 200:
                self.ui.statusLabel.setText("Подключено")
                # Устанавливаем поля для отправки и получения данных активными
                self.ui.getinfoline.setEnabled(True)
                self.ui.pb_get_info.setEnabled(True)
                self.ui.listWidget.setEnabled(True)
                self.setAcceptDrops(True)  # Подключаем Drag and Drop
                self.ui.pd_open_file.setEnabled(True)  # Делаем активной кнопку выбора файлов
                # Подключаем горячие клавиши
                self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+O"), self)
                self.shortcut.activated.connect(self.add_files_to_send)
        except requests.exceptions.ConnectionError:
            self.ui.statusLabel.setText("Подключение отсутствует")
            # Устанавливаем поля для отправки и получения данных неактивными
            self.ui.getinfoline.setEnabled(False)
            self.ui.pb_get_info.setEnabled(False)
            self.ui.listWidget.setEnabled(False)
            self.setAcceptDrops(False)
            self.ui.pd_open_file.setEnabled(False)
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Отсутствует подключение к {self.url}")

    def open_about(self):
        """
        Открытие окна about
        """
        self.about_window.show()

    def open_connection(self):
        """
        Открытия окна Connection
        """
        self.conn_window.show()

    def dragEnterEvent(self, event):
        mime = event.mimeData()
        if mime.hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_name = url.toLocalFile()
            self.file_list.append(url.toLocalFile())
            self.ui.listWidget.addItem(file_name)

        self.ui.pd_send_file.setEnabled(True)
        return super().dropEvent(event)

    def add_files_to_send(self):
        """
        Функция добавления файлов на отправку.
        """
        # Через диалоговое окно OpenFile получаем ссылку на файла
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')[0]

        self.file_list.append(fname)
        self.ui.listWidget.addItem(f'{fname}')
        self.ui.pd_send_file.setEnabled(True)

    def post_file(self):
        """
        Отправка файлов на сервис по api
        """
        files = []  # Временный список файлов для отправки
        for file_local in self.file_list:
            files.append(('files', open(f'{file_local}', 'rb')))
        resp = requests.post(url=f'{self.url}/frames/', files=files)  # post запрос на отправку файлов
        QtWidgets.QMessageBox.information(self, "Готово",
                                          f"Файлы отправлены. Ваш номер запроса: {resp.json()['request_number']}")

    def get_info(self):
        """
        Получаем информацию об отправке
        """
        source = self.ui.getinfoline.text()  # Получаем номер отправки из lineEdit
        self.download_list_files.clear()  # Очищаем список файлов для скачивания
        resp = requests.get(f"{self.url}/frames/{source}")
        if 'error' not in resp.json().keys():  # Проверяем есть ли ошибки
            self.ui.pb_download_all.setEnabled(True)
            self.ui.pb_delete.setEnabled(True)
            dict_ = resp.json()
            # Формируем таблицу с файлами
            headers = ["№", "Название", "Дата регистрации", "Загрузить"]
            stm = QtGui.QStandardItemModel()
            stm.setHorizontalHeaderLabels(headers)
            for key in dict_:
                if key != "request_number":
                    try:
                        temp_list = [val for val in dict_[key].values()]
                        self.download_list_files.append(temp_list)  # Список списков с информацией о файлах
                    except AttributeError:
                        QtWidgets.QMessageBox.warning(self, "Ошибка", f"Неправильный запрос")

            # Заполняем таблицу
            for row in range(len(self.download_list_files)):
                stm.setItem(row, 0, QtGui.QStandardItem(str(row + 1)))
                stm.setItem(row, 1, QtGui.QStandardItem(self.download_list_files[row][0]))
                stm.setItem(row, 2, QtGui.QStandardItem(self.download_list_files[row][1]))
                stm.setItem(row, 3, QtGui.QStandardItem("Скачать"))
            self.ui.tableView.setModel(stm)
            self.ui.tableView.setItemDelegateForColumn(3, self.openDelegate)

        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неправильный номер запроса")

    def delete_files(self):
        """
        Удаление отправки.
        Отправка delete запроса, при нажатии "Удалить"
        """
        source = self.ui.getinfoline.text()
        reply = QtWidgets.QMessageBox.question(self, 'Удалить файлы?',
                                               f'Удалить запрос {source} и его файлы из хранилища?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            requests.delete(f"{self.url}/frames/{source}")  # delete запрос на удаление файлов и записи бд
        QtWidgets.QMessageBox.information(self, 'Успешно',
                                               f'Запрос {source} и его файлы из хранилища удалены')
        headers = ["№", "Название", "Дата регистрации", "Загрузить"]
        stm = QtGui.QStandardItemModel()
        stm.setHorizontalHeaderLabels(headers)
        self.ui.tableView.setModel(stm)

    def download_file(self, item: QtCore.QModelIndex):
        """
        Скачать один выбранный файл
        """
        file_name = self.download_list_files[item.row()][0]
        fname, ok = QtWidgets.QFileDialog.getSaveFileName(self, "Save as", file_name)
        if not ok:
            return None
        directory_file = fname.replace(fname.split('/')[-1], "")  # Директория для сохранения файла
        source = self.ui.getinfoline.text()
        # Получаем название корзины с файлами
        resp = requests.get(f"{self.url}/bucket/{source}")
        bucket_name = resp.json()['bucket_name']
        client.fget_object(bucket_name, file_name, f"{fname}")  # Скачиваем файл с хранилища
        QtWidgets.QMessageBox.information(self, "Успешно", f"{file_name} \nЗагружен в \n{directory_file}")

    def save_all_files(self):
        """
        Сохранение всех файлов в указанную директорию
        """
        # Получаем путь, куда будем сохранять файлы
        fname = QtWidgets.QFileDialog.getExistingDirectoryUrl(self, "Save as").url()[8:]
        try:
            source = self.ui.getinfoline.text()
            resp = requests.get(f"{self.url}/bucket/{source}")  # Получаем название корзины с сервиса
            for item in self.download_list_files:
                # Сохраняем все файлы
                client.fget_object(resp.json()['bucket_name'], item[0], f"{fname}/{item[0]}")
            # В зависимости от количества файлов, выдаем информационное сообщение в нужном исчислении
            if len(self.download_list_files) == 1:
                QtWidgets.QMessageBox.information(self, "Успешно", f"1 файл загружен в {fname}")
            elif 1 < len(self.download_list_files) < 5:
                QtWidgets.QMessageBox.information(self, "Успешно",
                                                  f"{len(self.download_list_files)} файла загружены в {fname}")
            else:
                QtWidgets.QMessageBox.information(self, "Успешно",
                                                  f"{len(self.download_list_files)} файлов загружены в {fname}")
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Ошибка загрузки")

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Эвент на закрытие приложения
        """
        reply = QtWidgets.QMessageBox.question(self, 'Закрыть окно?', 'Вы хотите закрыть окно?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class AboutWindow(QtWidgets.QWidget):
    """
    Окно About. Просто так.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        resource.qInitResources()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/rss.ico")))
        self.setWindowTitle("About")
        self.textarea = QtWidgets.QLabel("Отправляем файлы в min.io и записываем в sqlite3\n")
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.textarea)
        self.setLayout(main_layout)


class ConnectionWindow(QtWidgets.QWidget):
    """
    Окно Connection. Устанавливаем IP адрес сервиса.
    """
    data = QtCore.Signal(str)  # Сигнал с IP адресом

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.pb_ok.clicked.connect(self.send_data)
        self.shortcut_enter.activated.connect(self.send_data)
        self.shortcut_esc.activated.connect(self.close)

    def initUi(self):
        resource.qInitResources()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/rss.ico")))
        self.urlLineEdit = QtWidgets.QLineEdit()
        self.setWindowTitle("Адрес подключения")
        self.pb_ok = QtWidgets.QPushButton("Ok")
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.urlLineEdit)
        main_layout.addWidget(self.pb_ok)
        self.shortcut_enter = QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), self)
        self.shortcut_esc = QtWidgets.QShortcut(QtGui.QKeySequence("Esc"), self)
        self.setLayout(main_layout)

    def send_data(self):
        self.data.emit(self.urlLineEdit.text())
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    win = MainWindow()
    win.show()

    app.exec_()
