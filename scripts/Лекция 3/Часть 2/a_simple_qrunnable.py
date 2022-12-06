"""
Использование классов QRunnable и QThreadPool для создания сразу множества задач
"""

import logging
import random
import time

from PySide6 import QtCore, QtWidgets

logging.basicConfig(format="%(message)s", level=logging.INFO)


class Runnable(QtCore.QRunnable):
    def __init__(self, thread_number):
        super().__init__()
        self.thread_number = thread_number

    def run(self) -> None:
        """
        Имитация выполнения долгой функции

        :return: None
        """

        for i in range(5):
            logging.info(f"Working in thread {self.thread_number}, step {i + 1}/5")
            time.sleep(random.randint(700, 2500) / 1000)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.resize(250, 150)
        self.setWindowTitle("QThreadPool + QRunnable")

        self.label = QtWidgets.QLabel("Hello!")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.pushButton = QtWidgets.QPushButton("Выполнить задачи")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(self.runTasks)

    def runTasks(self) -> None:
        """
        Запуск всех задач в пуле потоков

        :return: None
        """

        threadCount = QtCore.QThreadPool.globalInstance().maxThreadCount()
        self.label.setText(f"Running {threadCount} Threads")

        threadPool = QtCore.QThreadPool.globalInstance()
        for thread_number in range(threadCount):
            runnable = Runnable(thread_number)

            threadPool.start(runnable)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
