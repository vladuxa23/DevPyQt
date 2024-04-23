"""
Создание окна с радиокнопками
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(200, 200, 300, 200)  # Устанавливаем положение и размер окна
        self.setWindowTitle("PyQt6 QRadioButton")  # Задаем заголовок окна

        # Создание интерфейса
        self.label = QtWidgets.QLabel("Заглушка")  # Создаем метку для отображения текста

        rb_1 = QtWidgets.QRadioButton("JavaScript")  # Создаем радио-кнопку с надписью "JavaScript"
        rb_1.setChecked(True)  # Устанавливаем флажок по умолчанию

        rb_2 = QtWidgets.QRadioButton("Python")  # Создаем радио-кнопку с надписью "Python"

        rb_3 = QtWidgets.QRadioButton("Java")  # Создаем радио-кнопку с надписью "Java"

        hbox = QtWidgets.QHBoxLayout()  # Создаем горизонтальный макет

        hbox.addWidget(rb_1)  # Добавляем радио-кнопку в горизонтальный макет
        hbox.addWidget(rb_2)  # Добавляем радио-кнопку в горизонтальный макет
        hbox.addWidget(rb_3)  # Добавляем радио-кнопку в горизонтальный макет

        vbox = QtWidgets.QVBoxLayout()  # Создаем вертикальный макет
        vbox.addWidget(self.label)  # Добавляем метку в вертикальный макет
        vbox.addLayout(hbox)  # Добавляем горизонтальный макет в вертикальный макет

        self.setLayout(vbox)  # Устанавливаем вертикальный макет в качестве основного макета окна


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
