"""
Создание окна с чекбоксами
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(200, 200, 400, 200)  # Устанавливаем положение и размер окна
        self.setWindowTitle("PyQt6 QCheckBox")  # Задаем заголовок окна

        label = QtWidgets.QLabel("Hello")  # Создаем метку с текстом "Hello"

        # Создание чекбоксов с иконками
        ch_box_python = QtWidgets.QCheckBox("Python")  # Создаем чекбокс с надписью "Python"
        ch_box_js = QtWidgets.QCheckBox("JavaScript")  # Создаем чекбокс с надписью "JavaScript"
        ch_box_java = QtWidgets.QCheckBox("Java")  # Создаем чекбокс с надписью "Java"

        # Создание метки
        hbox = QtWidgets.QHBoxLayout()  # Создаем горизонтальный макет
        hbox.addWidget(ch_box_python)  # Добавляем чекбокс "Python" в горизонтальный макет
        hbox.addWidget(ch_box_js)  # Добавляем чекбокс "JavaScript" в горизонтальный макет
        hbox.addWidget(ch_box_java)  # Добавляем чекбокс "Java" в горизонтальный макет

        vbox = QtWidgets.QVBoxLayout()  # Создаем вертикальный макет
        vbox.addWidget(label)  # Добавляем метку в вертикальный макет
        vbox.addLayout(hbox)  # Добавляем горизонтальный макет в вертикальный макет

        self.setLayout(vbox)  # Устанавливаем вертикальный макет в качестве основного макета окна


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
