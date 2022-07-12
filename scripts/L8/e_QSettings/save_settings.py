import sys

from PySide2 import QtWidgets, QtGui, QtCore  # Импорт класса, который содержит элементы окна


class MyFirstWindow(QtWidgets.QWidget):  # Наследуемся от QMainWindow

    def __init__(self, parent=None):  # Создаем конструктор класса
        super().__init__(parent)  # Передаем конструктору ссылку на родительский компонент

        self.ip_list_settings = QtCore.QSettings("MyDataCard")

        self.initUi()

    def initUi(self):

        main_layout = QtWidgets.QVBoxLayout()

        ip_list = self.ip_list_settings.value("ip_list", [])

        for ip in ip_list:
            print(ip)

        self.lineEdit_1 = QtWidgets.QLineEdit()
        if ip_list:
            self.lineEdit_1.setText(ip_list[0])

        self.lineEdit_2 = QtWidgets.QLineEdit()
        if ip_list:
            self.lineEdit_2.setText(ip_list[1])

        self.lineEdit_3 = QtWidgets.QLineEdit()
        if ip_list:
            self.lineEdit_3.setText(ip_list[2])

        main_layout.addWidget(self.lineEdit_1)
        main_layout.addWidget(self.lineEdit_2)
        main_layout.addWidget(self.lineEdit_3)

        self.setLayout(main_layout)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.ip_list_settings.setValue("ip_list",
                                       [self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text()])
        print("Приложение закрылось")


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения

    myWindow = MyFirstWindow()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется
