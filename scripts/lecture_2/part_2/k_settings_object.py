"""
Работа с классом QSettings (сохранение объектов)
"""

from PySide6 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):

    # Конструктор класса
    def __init__(self, parent=None):

        super().__init__(parent)  # Вызов конструктора родительского класса

        self.ip_list_settings = QtCore.QSettings("IPViewer")  # Создание объекта QSettings для хранения настроек

        self.initUi()  # Инициализация пользовательского интерфейса

    def initUi(self) -> None:
        """
        Инициализация пользовательского интерфейса

        :return: None
        """

        main_layout = QtWidgets.QVBoxLayout()  # Создание вертикального макета для виджетов

        ip_list = self.ip_list_settings.value("ip_list", [])  # Получение списка IP-адресов из настроек

        for ip in ip_list:  # Вывод каждого IP-адреса в консоль
            print(ip)

        self.lineEdit_1 = QtWidgets.QLineEdit()  # Создание виджета QLineEdit для ввода IP-адреса
        # Если список IP-адресов не пуст, установить текст в первом QLineEdit
        if ip_list:
            self.lineEdit_1.setText(ip_list[0])

        self.lineEdit_2 = QtWidgets.QLineEdit()  # Создание еще двух виджетов QLineEdit для ввода IP-адреса
        if ip_list:
            self.lineEdit_2.setText(ip_list[1])

        self.lineEdit_3 = QtWidgets.QLineEdit()
        if ip_list:
            self.lineEdit_3.setText(ip_list[2])

        # Добавление виджетов QLineEdit в вертикальный макет
        main_layout.addWidget(self.lineEdit_1)
        main_layout.addWidget(self.lineEdit_2)
        main_layout.addWidget(self.lineEdit_3)

        # Установка вертикального макета для текущего виджета
        self.setLayout(main_layout)

    # Метод, вызываемый при закрытии окна
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        # Сохранение списка IP-адресов в настройки
        self.ip_list_settings.setValue(
            "ip_list", [self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text()]
        )


# Точка входа в приложение
if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создание объекта QApplication

    myWindow = Window()  # Создание и отображение окна приложения
    myWindow.show()

    app.exec()  # Запуск основного цикла обработки событий приложения
