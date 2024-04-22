"""
Пример работы метода singleShot класса QTimer
"""

import time

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initTimer()

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.labelTime = QtWidgets.QLabel()

        self.spinBoxDelay = QtWidgets.QSpinBox()

        self.pushButtonStart = QtWidgets.QPushButton("Выполнить")

        plainTextEdit = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.labelTime)
        layout.addWidget(self.spinBoxDelay)
        layout.addWidget(self.pushButtonStart)
        layout.addWidget(plainTextEdit)

        self.setLayout(layout)

    def initTimer(self) -> None:
        """
        Инициализация таймеров

        :return: None
        """

        self.timerShot = QtCore.QTimer()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonStart.clicked.connect(self.startDelayMethod)

    def startDelayMethod(self) -> None:
        """
        Запуск отсчёта задержки для выполнения функции

        :return: None
        """

        self.pushButtonStart.setEnabled(False)

        self.timerShot.singleShot(self.spinBoxDelay.value() * 1000, self.printCurrentTime)
        self.timerShot.start()

    def printCurrentTime(self) -> None:
        """
        Функция которая выводит в self.labelTime текущее время

        :return: None
        """

        self.pushButtonStart.setEnabled(True)

        self.labelTime.setText(time.ctime())


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = Window()
    win.show()
    app.exec()
