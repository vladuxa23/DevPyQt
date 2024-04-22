"""
Создание простого окна в ООП стиле
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):  # Наследование от QWidget
    def __init__(self, parent=None) -> None:  # Создание конструктора класса
        super().__init__(parent)  # Вызов конструктора родительского класса


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создание объекта приложения

    window = Window()  # Создание объекта окна
    window.show()  # Показ окна

    app.exec()  # Запуск бесконечного цикла приложения (событий)
