"""
Создание окна на основе QWidget
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        # Настройка компоновки окна
        abc = QtWidgets.QPushButton("Текст кнопки")
        checkbox = QtWidgets.QCheckBox("Флажок")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(abc)
        layout.addWidget(checkbox)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec_()
