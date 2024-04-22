"""
Подключение сигнала к методу другого класса
"""

from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.pushButton = QtWidgets.QPushButton("Выполнить функцию")
        self.pushButton.setCheckable(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(Test.some_function)


class Test:
    @Slot()
    def some_function(self):
        print("Метод другого класса")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
