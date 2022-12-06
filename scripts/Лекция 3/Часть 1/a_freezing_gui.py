"""
Демонстрация 'зависания' приложения при долгом выполнении слота
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

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Отсчёт идёт: ")
        self.button = QtWidgets.QPushButton("Начать")

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.button.pressed.connect(self.startCounter)

    def startCounter(self) -> None:
        """
        Функция отсчёта до 10 (имитация длительного выполнения функции)

        :return: None
        """

        for i in range(10):
            time.sleep(1)
            self.label.setText(f"Отсчёт идёт: {i} сек.")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
