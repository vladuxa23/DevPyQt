"""
Создание окна с сетчатым расположением элементов
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(200, 200, 700, 400)  # Устанавливаем положение и размер окна
        self.setWindowTitle("PyQt6 QGridLayout")  # Задаем заголовок окна

        grid = QtWidgets.QGridLayout()  # Создаем экземпляр QGridLayout

        # Создание кнопок
        btn1 = QtWidgets.QPushButton("Click One")  # Создаем кнопку с надписью "Click One"
        btn2 = QtWidgets.QPushButton("Click Two")  # Создаем кнопку с надписью "Click Two"
        btn3 = QtWidgets.QPushButton("Click Three")  # Создаем кнопку с надписью "Click Three"
        btn4 = QtWidgets.QPushButton("Click Four")  # Создаем кнопку с надписью "Click Four"
        btn5 = QtWidgets.QPushButton("Click Five")  # Создаем кнопку с надписью "Click Five"
        btn6 = QtWidgets.QPushButton("Click Six")  # Создаем кнопку с надписью "Click Six"
        btn7 = QtWidgets.QPushButton("Click Seven")  # Создаем кнопку с надписью "Click Seven"
        btn8 = QtWidgets.QPushButton("Click Eight")  # Создаем кнопку с надписью "Click Eight"

        # Добавление кнопок в сетку
        grid.addWidget(btn1, 0, 0)  # Добавляем кнопку btn1 в сетку на первой строке и первом столбце
        grid.addWidget(btn2, 0, 1)  # Добавляем кнопку btn2 в сетку на первой строке и втором столбце
        grid.addWidget(btn3, 0, 2)  # Добавляем кнопку btn3 в сетку на первой строке и третьем столбце
        grid.addWidget(btn4, 0, 3)  # Добавляем кнопку btn4 в сетку на первой строке и четвертом столбце
        grid.addWidget(btn5, 1, 0)  # Добавляем кнопку btn5 в сетку на второй строке и первом столбце
        grid.addWidget(btn6, 2, 1)  # Добавляем кнопку btn6 в сетку на второй строке и втором столбце
        grid.addWidget(btn7, 3, 2)  # Добавляем кнопку btn7 в сетку на второй строке и третьем столбце
        grid.addWidget(btn8, 4, 3)  # Добавляем кнопку btn8 в сетку на второй строке и четвертом столбце

        # Установка сетки в качестве основного макета окна
        self.setLayout(grid)  # Устанавливаем сетку в качестве основного макета окна


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
