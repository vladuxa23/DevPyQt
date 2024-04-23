"""
Создание окно с текстом, изображением и анимированным gif-изображением.
"""

import os

from PySide6 import QtWidgets, QtGui

from conf import ROOT_FOLDER


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(200, 200, 700, 400)  # Установка геометрии окна
        self.setWindowTitle("Приложение")  # Установка заголовка окна
        # Установка иконки окна
        self.setWindowIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'python.png')))

        # ----------Установка текста-------------

        label_text = QtWidgets.QLabel(self)  # Создание метки для текста
        label_text.setText("Новый текст")  # Установка текста метки
        label_text.move(100, 10)  # Перемещение текста
        label_text.setFont(QtGui.QFont("Arial", 10))  # Установка шрифта и размера текста
        label_text.setStyleSheet('color: red')  # Установка цвета текста

        # ----------Загрузка изображения------------

        pixmap = QtGui.QPixmap(os.path.join(ROOT_FOLDER, 'static', 'images', 'python.png'))  # Загрузка изображения
        pixmap_scaled = pixmap.scaled(100, 100)  # Изменение размера изображения

        label_image = QtWidgets.QLabel(self)  # Создание метки для изображения
        label_image.setPixmap(pixmap_scaled)  # Установка изображения в метку

        # ----------Загрузка gif-----------

        movie = QtGui.QMovie(os.path.join(ROOT_FOLDER, 'static', 'images', 'airplane.gif'))  # Загрузка gif
        movie.setSpeed(100)  # Установка скорости проигрывания gif

        label_gif = QtWidgets.QLabel(self)  # Создание метки для gif
        label_gif.setGeometry(100, 100, 800, 400)  # Установка геометрии метки для gif
        label_gif.setMovie(movie)  # Установка gif в метку

        movie.start()  # Запуск проигрывания gif


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
