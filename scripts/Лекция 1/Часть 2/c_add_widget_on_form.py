"""
Добавление виджетов на форму
"""

from PySide6 import QtWidgets


class AddWidgets(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        # Напрямую
        btn = QtWidgets.QPushButton("Кнопка", self)
        btn.move(30, 30)

        # Через компоновку
        # layout = QtWidgets.QVBoxLayout()
        #
        # pushButton = QtWidgets.QPushButton("Кнопка")
        # radioButton = QtWidgets.QRadioButton("some text")
        # checkBox = QtWidgets.QCheckBox("check box")
        #
        # layout.addWidget(pushButton)
        # layout.addWidget(radioButton)
        # layout.addWidget(checkBox)
        # self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = AddWidgets()
    window.show()

    app.exec_()
