"""
Пример работы с классом QTimer
"""

import psutil
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

        self.labelCPU = QtWidgets.QLabel("CPU usage: ")
        self.labelRAM = QtWidgets.QLabel("RAM usage: ")

        self.pushButtonStart = QtWidgets.QPushButton("Отслеживать значения")
        self.pushButtonStop = QtWidgets.QPushButton("Прекратить отслеживание")

        plainTextEdit = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.labelCPU)
        layout.addWidget(self.labelRAM)
        layout.addWidget(plainTextEdit)
        layout.addWidget(self.pushButtonStart)
        layout.addWidget(self.pushButtonStop)

        self.setLayout(layout)

    def initTimer(self) -> None:
        """
        Инициализация таймеров

        :return: None
        """

        self.timerCPU = QtCore.QTimer()
        self.timerCPU.setInterval(1000)
        # self.timerCPU.start()  # Запуск сразу при открытии приложения

        self.timerRAM = QtCore.QTimer()
        self.timerRAM.setInterval(1000)
        # self.timerRAM.start()  # Запуск сразу при открытии приложения

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonStart.clicked.connect(self.startTimers)
        self.pushButtonStop.clicked.connect(self.stopTimers)

        self.timerCPU.timeout.connect(self.checkCPU)
        self.timerRAM.timeout.connect(self.checkRAM)

    def startTimers(self) -> None:
        """
        Запуск таймеров для отслеживания значений ПК

        :return: None
        """

        self.timerRAM.start()
        self.timerCPU.start()

    def stopTimers(self) -> None:
        """
        Остановка таймеров отслеживания параметров ПК

        :return: None
        """

        self.timerRAM.stop()
        self.timerCPU.stop()

    def checkCPU(self) -> None:
        """
        Получение значений использования CPU

        :return: None
        """

        # time.sleep(3)  # Всё равно даже с учётом таймера, долгие процессы работать не будут
        cpu_usage = psutil.cpu_percent()
        self.labelCPU.setText(f"CPU usage: {cpu_usage} %")

    def checkRAM(self) -> None:
        """
        Получение значений использования RAM

        :return: None
        """

        ram_usage = psutil.virtual_memory()
        self.labelRAM.setText(f"RAM usage: {ram_usage.percent} %")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = Window()
    win.show()
    app.exec()
