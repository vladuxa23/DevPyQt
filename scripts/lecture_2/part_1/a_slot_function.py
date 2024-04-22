"""
Подключение сигнала к функции
"""

from PySide6 import QtWidgets


def print_something() -> None:
    """
    Функция вывода на печать

    :return: None
    """

    print("Функция выполнена")


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

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(print_something)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
