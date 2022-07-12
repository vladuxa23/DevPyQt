import sys
import platform

from PySide2.QtCore import QDateTime
from PySide2.QtSql import QSqlQuery, QSqlTableModel
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtSql, QtWidgets
from django.conf import settings
from django.contrib.auth.hashers import check_password

from exam.ui import ui_db, ui_login


if platform.system() == 'Windows':
    DB_PATH = r'C:\Users\geosok\PycharmProjects\todo_list\db.sqlite3'   # на Windows
else:
    DB_PATH = '/Users/georgysokolov/PycharmProjects/todo_list/db.sqlite3'   # Mac
    import os
    os.environ['QT_MAC_WANTS_LAYER'] = '1'   # Прописываю, чтобы открывалось на Mac OS

settings.configure()  # конфигурация настроек джанги для check_password


class Login(QDialog):
    """ Диалоговое окно авторизации """
    username = None
    id = None

    def __init__(self, parent=None):
        super().__init__(parent)

        self.model = None
        self.db = None

        self.ui = ui_login.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_login.clicked.connect(self.handle_login)
        self.ui.pushButton.clicked.connect(self.close)

    def handle_login(self):
        """ Проверка имени пользователя и пароля """
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(DB_PATH)  # путь до места, где находится БД

        self.model = QtSql.QSqlTableModel()
        self.model.setTable('auth_user')  # выбираем нужную таблицу из БД

        self.model.select()

        query = QSqlQuery()
        query.exec_(f"SELECT id, username, password FROM auth_user WHERE username == '{self.ui.lineEdit_name.text()}' ")

        query.first()  # Первая запись
        if query.value('username') is None:
            QtWidgets.QMessageBox.warning(
                self, 'Error;', 'Введен неверный логин!')
        else:
            if check_password(self.ui.lineEdit_password.text(), query.value('password')):
                Login.username = query.value('username')  # Сохраняем нашего пользователя
                Login.id = query.value('id')   # Сохраняем его id
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error;', 'Введен неверный пароль!')


class MyDBClient(QMainWindow):
    """ Основное окно для работы с БД """

    def __init__(self, parent=None):  # Чтобы было отдельное окно parent = None
        super().__init__(parent)

        self.model = None
        self.db = None

        self.ui = ui_db.Ui_MainWindow()
        self.ui.setupUi(self)

        options = ['Активно', 'Отложено', 'Выполнено']
        for option in options:
            self.ui.comboBox_status.addItem(option)

        self.ui.lineEdit_author.setText(f'{Login().username}')

        self.init_sql_model()

        self.init_signals()

    def init_sql_model(self):
        """ Инициализация модели БД и представление ее в нашем приложении """
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(DB_PATH)  # путь до места, где находится БД

        self.model = QtSql.QSqlTableModel()
        self.model.setTable('note_note')  # выбираем нужную таблицу из БД

        self.model.select()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)  # чтобы можно было менять значения в БД из таблицы

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)  # Прячем столбец id
        # self.ui.tableView.setColumnHidden(8, True)  # Прячем столбец author_id
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)  # Делаем таблицу подвижной
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def init_signals(self):
        self.ui.pushButtonADD.clicked.connect(self.add)
        self.ui.pushButtonDEL.clicked.connect(self.delete)

    def add(self):
        """ Добавление записей в БД """
        index = self.model.rowCount()

        status = self.ui.comboBox_status.currentText()
        if status == 'Активно':
            status = 'AC'
        elif status == 'Отложено':
            status = 'PO'
        elif status == 'Выполнено':
            status = 'CO'

        importance = self.ui.checkBox_importance.isChecked()
        if importance:
            importance = 1
        else:
            importance = 0

        publish = self.ui.checkBox_publish.isChecked()
        if publish:
            publish = 1
        else:
            publish = 0

        current_date = QDateTime.currentDateTime()
        format_date = 'dd-MM-yyyy hh:mm:ss'
        create_at = current_date.toString(format_date)
        complete_at = current_date.addDays(1).toString(format_date)

        self.model.insertRows(index, 1)
        self.model.setData(self.model.index(index, 1), self.ui.lineEdit_topic.text())
        self.model.setData(self.model.index(index, 2), self.ui.textEdit.toPlainText())
        self.model.setData(self.model.index(index, 3), status)
        self.model.setData(self.model.index(index, 4), importance)
        self.model.setData(self.model.index(index, 5), publish)
        self.model.setData(self.model.index(index, 6), complete_at)
        self.model.setData(self.model.index(index, 7), create_at)
        self.model.setData(self.model.index(index, 8), Login.id)
        self.model.submitAll()

        # Далее необходимо очистить все значения из полей ввода
        self.ui.lineEdit_topic.setText('')
        self.ui.textEdit.setText('')
        self.ui.comboBox_status.setCurrentText('Активно')
        self.ui.checkBox_importance.setChecked(False)
        self.ui.checkBox_publish.setChecked(False)

    def delete(self):
        """ Удаление записей из БД """
        if self.ui.tableView.currentIndex().row() > -1:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
            self.model.select()
        else:
            QtWidgets.QMessageBox.question(self, 'Message', 'Выберете строчку для удаления', QtWidgets.QMessageBox.Ok)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно",
                                               "Вы хотите закрыть окно?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    if Login().exec_() == QDialog.Accepted:
        window = MyDBClient()
        window.show()

        sys.exit(app.exec_())