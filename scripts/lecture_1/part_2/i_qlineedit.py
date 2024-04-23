"""
Создание окна с полем для ввода
"""
import os

from PySide6 import QtGui, QtWidgets

from conf import ROOT_FOLDER


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(200, 200, 700, 400)  # Установка геометрии окна
        self.setWindowTitle("PySide6 QLineEdit")  # Установка заголовка окна
        self.setWindowIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'python.png')))  # Установка иконки окна

        line_edit = QtWidgets.QLineEdit(self)  # Создание поля ввода
        line_edit.setFont(QtGui.QFont("Sanserif", 12))  # Установка стиля шрифта для поля ввода
        line_edit.setPlaceholderText("Enter Your Name")  # Установка текста-подсказки в поле ввода
        line_edit.setMaxLength(5)  # Установка максимальной длины текста в поле ввода

        # line_edit.setReadOnly(True)
        # line_edit.setText("Default Text")   # Запись текста по умолчанию
        # line_edit.setEnabled(False)    # Включение/отключение поля ввода


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
