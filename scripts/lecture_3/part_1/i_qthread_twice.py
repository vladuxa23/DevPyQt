"""
Использование нескольких потоков
"""

import time
import requests

from PySide6 import QtCore, QtWidgets


class WorkerOne(QtCore.QThread):
    progress = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.status = None

    def run(self) -> None:
        """
        Метод имитирующий долгую задачу

        :return: None
        """

        self.status = True

        counter = 0

        while self.status:
            time.sleep(1)
            counter += 1
            self.progress.emit(counter)


class WorkerTwo(QtCore.QThread):
    data_responced = QtCore.Signal(dict)

    def run(self) -> None:
        """
        Метод имитирующий долгую задачу

        :return: None
        """

        while True:
            response = requests.get("http://ip-api.com/json/")
            data = response.json()
            self.data_responced.emit(data)
            time.sleep(5)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.label = QtWidgets.QLabel("Выполнение долгой задачи: ")
        self.pushButton = QtWidgets.QPushButton("Запустить долгую задачу")
        self.pushButtonApi = QtWidgets.QPushButton("Получить данные по ip")
        self.pushButtonOtherProcess = QtWidgets.QPushButton("Другие действия с GUI")
        self.plainTextEdit = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.pushButtonApi)
        layout.addWidget(self.pushButtonOtherProcess)
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """

        self.thread = WorkerOne()
        self.api_thread = WorkerTwo()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(self.runLongProcess)
        self.pushButtonOtherProcess.clicked.connect(
            lambda: self.plainTextEdit.appendPlainText(f"{time.ctime()}: push clicked")
        )

        self.pushButtonApi.clicked.connect(self.api_thread.start)

        self.thread.progress.connect(self.reportProgress)
        self.thread.finished.connect(lambda: print("Поток остановлен"))

        self.api_thread.data_responced.connect(self.ip_updated)
        self.api_thread.started.connect(lambda: print("Поток погоды запущен"))

    def runLongProcess(self) -> None:
        """
        Запуск потока с "долгим" выполнением

        :return: None
        """

        # self.pushButton.setEnabled(False)
        if self.thread.status:
            self.thread.status = False
        else:
            self.thread.start()

    def reportProgress(self, progress) -> None:
        """
        Приём данных из потока и обработка их в основном цикле приложения

        :param progress: прогресс выполнения функции в потоке
        :return: None
        """

        self.label.setText(f"Выполнение долгой задачи: {progress}")

    def ip_updated(self, data: dict) -> None:

        self.plainTextEdit.setPlainText(f"Обновлено: {time.ctime()}\n{str(data)}")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
