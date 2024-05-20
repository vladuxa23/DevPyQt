"""
Демонстрация работы с QSplashScreen
"""
import os
import time
from PySide6 import QtCore, QtWidgets, QtGui

from conf import ROOT_FOLDER


class SplashScreen(QtWidgets.QSplashScreen):
    """
    Создание класса на базе QSplashScreen для отключения события mousePressEvent
    """

    def mousePressEvent(self, arg__1: QtGui.QMouseEvent) -> None:
        pass


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.pushButton = QtWidgets.QPushButton("Отмена")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

        self.loadGUI()

    def loadGUI(self):
        """
        'Долгая' загрузка приложения

        :return: None
        """

        # splash = QtWidgets.QSplashScreen(QtGui.QPixmap(os.path.join(ROOT_FOLDER, 'static', 'images', 'python.png')))
        splash = SplashScreen(QtGui.QPixmap(os.path.join(ROOT_FOLDER, 'static', 'images', 'python.png')))
        splash.showMessage("Загрузка данных...     0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
        splash.show()
        for _ in range(100):
            time.sleep(0.05)
            if (_ % 10) == 0:
                splash.showMessage(f"Загрузка данных...     {_}%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter, QtCore.Qt.black)

        splash.finish(self)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()

    app.exec()
