from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """
        self.setFixedSize(250, 150)

        labelLogin = QtWidgets.QLabel("Логин")
        labelLogin.setMinimumWidth(80)
        labelRegistration = QtWidgets.QLabel("Пароль")
        labelRegistration.setMinimumWidth(80)

        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setPlaceholderText("Введите логин")
        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setPlaceholderText("Введите пароль")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.pushButtonLogin = QtWidgets.QPushButton()
        self.pushButtonLogin.setText("Войти")

        self.pushButtonRegistration = QtWidgets.QPushButton()
        self.pushButtonRegistration.setText("Регистрация")

        layoutLogin = QtWidgets.QHBoxLayout()
        layoutLogin.addWidget(labelLogin)
        layoutLogin.addWidget(self.lineEditLogin)

        layoutPassword = QtWidgets.QHBoxLayout()
        layoutPassword.addWidget(labelRegistration)
        layoutPassword.addWidget(self.lineEditPassword)

        layoutButtons = QtWidgets.QHBoxLayout()
        layoutButtons.addWidget(self.pushButtonLogin)
        layoutButtons.addWidget(self.pushButtonRegistration)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLogin)
        layoutMain.addLayout(layoutPassword)
        layoutMain.addLayout(layoutButtons)

        self.setLayout(layoutMain)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
