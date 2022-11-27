"""
Генерация "кастомных" сигналов и открытие нескольких окон
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Main(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initChilds()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.pushButton = QtWidgets.QPushButton("Открыть дополнительное окно")
        self.lineEdit = QtWidgets.QLineEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.lineEdit)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(self.childWindow.show)

        self.childWindow.custom_signal.connect(lambda x: print(x))
        self.childWindow.custom_signal.connect(self.childCustomSignalActivated)

    def initChilds(self) -> None:
        """
        Инициализация дочерних окон

        :return: None
        """

        self.childWindow = Child()  # Обязательно является атрибутом класса (self)

    def childCustomSignalActivated(self, text) -> None:
        """
        Метод срабатывает при выполнении
        сигнала custom_signal (в момент вызова emit)

        :param text: текст из дочернего окна
        :return: None
        """

        self.lineEdit.setText(text)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Действия при закрытии программы

        :param event: QtGui.QCloseEvent
        :return: None
        """

        self.childWindow.close()


class Child(QtWidgets.QWidget):
    custom_signal = QtCore.Signal(str)  # Обязательно указать тип данных

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        label = QtWidgets.QLabel("Другое окно")

        self.lineEdit = QtWidgets.QLineEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.lineEdit)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.lineEdit.textChanged.connect(self.changedLineEditText)

    def changedLineEditText(self) -> None:
        """
        Метод обрабатывающий изменение текста в lineEdit

        :return: None
        """

        self.custom_signal.emit(self.lineEdit.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Main()
    myapp.show()
    app.exec()
