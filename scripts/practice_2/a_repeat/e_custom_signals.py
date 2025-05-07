"""
Файл для повторения темы генерации сигналов и передачи данных из одного виджета в другой

Напомнить про работу с пользовательскими сигналами.

Предлагается создать 2 формы:
* На первый форме label с надписью "Пройдите регистрацию" и pushButton с текстом "Зарегистрироваться"
* На второй (QDialog) форме:
  * lineEdit с placeholder'ом "Введите логин"
  * lineEdit с placeholder'ом "Введите пароль"
  * pushButton "Зарегистрироваться"

  при нажатии на кнопку, данные из lineEdit'ов передаются в главное окно, в
  котором надпись "Пройдите регистрацию", меняется на "Добро пожаловать {данные из lineEdit с логином}"
  (пароль можно показать в терминале в захешированном виде)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        label = QtWidgets.QLabel(self)
        label.setText("<h1>Пройдите регистрацию</h1>")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.__pushButton = QtWidgets.QPushButton(self)
        self.__pushButton.setText("Зарегистрироваться")

        l = QtWidgets.QVBoxLayout()
        l.addWidget(label)
        l.addWidget(self.__pushButton)

        self.setLayout(l)

    def __initSignals(self):
        self.__pushButton.clicked.connect(self.showRegistrationWindow)

    def showRegistrationWindow(self):
        self.r_w = RegistrationWindow()
        self.r_w.registered.connect(self.userDataRecieved)
        self.r_w.show()

    def userDataRecieved(self, data):
        print(data)


class RegistrationWindow(QtWidgets.QWidget):
    registered = QtCore.Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()

    def __initUi(self):
        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setPlaceholderText("Введите логин")

        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setPlaceholderText("Введите пароль")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.pushButtonRegistration = QtWidgets.QPushButton("Регистрация")
        self.pushButtonRegistration.clicked.connect(self.onPushButtonRegistrationClicked)

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.lineEditLogin)
        l.addWidget(self.lineEditPassword)
        l.addWidget(self.pushButtonRegistration)

        self.setLayout(l)

    def onPushButtonRegistrationClicked(self):
        user_data = self.lineEditLogin.text(), self.lineEditPassword.text()
        self.registered.emit(user_data)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
