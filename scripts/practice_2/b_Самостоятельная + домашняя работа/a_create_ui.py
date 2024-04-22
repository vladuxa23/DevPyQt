from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # TODO Вызовите метод для инициализации интерфейса

    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        labelLogin = ...  # TODO Создайте виджет QLabel с текстом "Логин"
        labelRegistration = ...  # TODO Создайте виджет QLabel с текстом "Регистрация"

        self.lineEditLogin = ...  # TODO создайте виджет QLineEdit
        self.lineEditLogin  # TODO добавьте placeholderText "Введите логин" с помощью метода .setPlaceholderText()
        self.lineEditPassword = ...  # TODO создайте виджет QLineEdit
        self.lineEditPassword  # TODO добавьте placeholderText "Введите пароль"
        self.lineEditPassword  # TODO установите ограничение видимости вводимых знаков с помощью метода .setEchoMode()

        self.pushButtonLogin = ...  # TODO создайте виджет QPushButton
        self.pushButtonLogin  # TODO установите текст "Войти" с помощью метода setText()

        self.pushButtonRegistration = ...  # TODO создайте виджет QPushButton
        self.pushButtonRegistration  # TODO установите текст "Регистрация" с помощью метода setText()

        layoutLogin = ...  # TODO Создайте QHBoxLayout
        layoutLogin  # TODO с помощью метода .addWidget() добавьте labelLogin
        layoutLogin  # TODO с помощью метода .addWidget() добавьте self.lineEditLogin

        layoutPassword = ...  # TODO Создайте QHBoxLayout
        layoutPassword  # TODO с помощью метода .addWidget() добавьте labelRegistration
        layoutPassword  # TODO с помощью метода .addWidget() добавьте self.lineEditPassword

        layoutButtons = ...  # TODO Создайте QHBoxLayout
        layoutButtons  # TODO с помощью метода .addWidget() добавьте self.pushButtonLogin
        layoutButtons  # TODO с помощью метода .addWidget() добавьте self.pushButtonRegistration

        layoutMain = ...  # TODO Создайте QVBoxLayout
        layoutMain  # TODO с помощью метода .addLayout() добавьте layoutLogin
        layoutMain  # TODO с помощью метода .addLayout() добавьте layoutPassword
        layoutMain  # TODO с помощью метода .addLayout() добавьте layoutButtons

        self  # TODO с помощью метода setLayout установите layoutMain на основной виджет


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
