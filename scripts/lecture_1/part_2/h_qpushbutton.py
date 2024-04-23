"""
Создание окна с кнопкой
"""
import os

from PySide6 import QtCore, QtGui, QtWidgets

from conf import ROOT_FOLDER


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(200, 200, 700, 400)  # Установка геометрии окна
        self.setWindowTitle("PySide6 QPushButton")  # Установка заголовка окна
        self.setWindowIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'python.png')))  # Установка иконки окна

        btn = QtWidgets.QPushButton("Click", self)  # Инициализация кнопки
        btn.setGeometry(100, 100, 110, 50)  # Изменение размера кнопки
        btn.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))  # Установка стиля шрифта для кнопки
        btn.setIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'python.png')))  # Установка иконки для кнопки
        btn.setIconSize(QtCore.QSize(36, 36))  # Изменение размера иконки


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
