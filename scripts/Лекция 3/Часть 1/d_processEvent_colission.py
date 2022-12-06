"""
Демонстрация коллизии в приложении при использовании processEvents()
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

        self.setFixedSize(200, 100)

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Отсчёт идёт: ")
        self.button = QtWidgets.QPushButton("Начать")
        self.buttonCollision = QtWidgets.QPushButton("Помешать")

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.buttonCollision)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.button.clicked.connect(self.startCounter)
        self.buttonCollision.clicked.connect(lambda: self.label.setText("Я вклинилась в основной поток"))

    def startCounter(self) -> None:
        """
        Функция отсчёта до 10 (имитация длительного выполнения функции)

        :return: None
        """

        for i in range(1, 11):
            time.sleep(1)
            self.label.setText(f"Отсчёт идёт: {i} сек.")
            QtWidgets.QApplication.processEvents()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
