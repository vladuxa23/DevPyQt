"""
Демонстрация работы с QMovie
"""

import time

from PySide6 import QtCore, QtWidgets, QtGui


class LoadScreen(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

        # Таймер для вызова метода, для подгонки размера под родителя
        timer = QtCore.QTimer(self)
        timer.setInterval(10)
        timer.timeout.connect(lambda: self.resize(self.parent().size()))
        timer.start()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.hide()  # скрываем по умолчанию

        # self.movie = QtGui.QMovie("static/gif/load_1.gif")
        self.movie = QtGui.QMovie("static/gif/load_2.gif")

        labelAnimation = QtWidgets.QLabel()
        labelAnimation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        labelAnimation.setMovie(self.movie)

        labelLoad = QtWidgets.QLabel("Идёт загрузка...")
        labelLoad.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout = QtWidgets.QVBoxLayout()
        layout.addSpacerItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                   QtWidgets.QSizePolicy.Policy.Expanding))
        layout.addWidget(labelAnimation)
        layout.addWidget(labelLoad)
        layout.addSpacerItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                   QtWidgets.QSizePolicy.Policy.Expanding))
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def startAnimation(self) -> None:
        """
        Запуск анимации

        :return: None
        """

        self.show()
        self.parent().setEnabled(False)
        self.movie.start()

    def stopAnimation(self) -> None:
        """
        Остановка анимации

        :return: None
        """

        self.hide()
        self.parent().setEnabled(True)
        self.movie.stop()


class HandleThread(QtCore.QThread):
    sending = QtCore.Signal(str)

    def run(self):
        time.sleep(5)
        self.sending.emit("Данные загружены")


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

        self.load_screen = LoadScreen(self)
        self.handleThread = HandleThread()

        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.resize(300, 300)

        self.label = QtWidgets.QLabel("...")
        self.button = QtWidgets.QPushButton("Загрузить данные")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.button.clicked.connect(self.loadData)

        self.handleThread.started.connect(self.load_screen.startAnimation)
        self.handleThread.finished.connect(self.load_screen.stopAnimation)
        self.handleThread.sending.connect(self.label.setText)

    def loadData(self) -> None:
        """
        Загрузка данных

        :return: None
        """

        self.handleThread.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
