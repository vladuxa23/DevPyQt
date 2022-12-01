"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets, QtCore
from mirror_text import Ui_MainWindow

def reverse_(str_) -> str:
    """
    Внешняя функция разворота
    """
    # result = ''.join(reversed(str_))
    result = str_[::-1]
    return result

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()


    def initUi(self):
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()
        self.pushButtonMirror = QtWidgets.QPushButton("Развернуть")

        layout_1 = QtWidgets.QHBoxLayout()
        layout_1.addWidget(self.lineEditInput)
        layout_1.addWidget(self.lineEditMirror)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(layout_1)
        main_layout.addWidget(self.pushButtonMirror)

        self.setLayout(main_layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.pushButtonMirror.clicked.connect(self.set_lineEditMirror())  # = QtCore.Signal(...)

    def set_lineEditMirror(self):
        self.lineEditMirror.setText(self.lineEditInput.text()[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
