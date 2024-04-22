"""
Создание окна с вертикальным расположением элементов
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)  # Установка геометрии окна
        self.setWindowTitle("PyQt6 QVBoxLayout")  # Установка заголовка окна

        # ----Создание объекта QVBoxLayout-----

        v_box = QtWidgets.QVBoxLayout()  # Создание вертикального макета

        # Создание кнопок
        btn1 = QtWidgets.QPushButton("Click One")  # Кнопка 1
        btn2 = QtWidgets.QPushButton("Click Two")  # Кнопка 2
        btn3 = QtWidgets.QPushButton("Click Three")  # Кнопка 3
        btn4 = QtWidgets.QPushButton("Click Four")  # Кнопка 4
        btn5 = QtWidgets.QPushButton("Click Five")  # Кнопка 5

        # Добавление кнопок в вертикальный макет
        v_box.addWidget(btn1)  # Добавление кнопки 1 в макет
        v_box.addWidget(btn2)  # Добавление кнопки 2 в макет
        v_box.addWidget(btn3)  # Добавление кнопки 3 в макет
        v_box.addWidget(btn4)  # Добавление кнопки 4 в макет
        v_box.addWidget(btn5)  # Добавление кнопки 5 в макет
        v_box.addSpacing(100)  # Добавление дополнительного расстояния между кнопками

        self.setLayout(v_box)  # Установка вертикального макета для окна


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
