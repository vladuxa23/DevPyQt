"""
Подключение сигнала к анонимной функции
"""
import time

from PySide6 import QtWidgets


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

        self.pushButton = QtWidgets.QCheckBox("Выполнить функцию")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(lambda data: print(f"{time.ctime()}: Выполняю lambda функцию, сигнал clicked возвращает значение {data}"))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
