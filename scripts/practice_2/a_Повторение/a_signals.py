"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()

        self.pushButtonMirror = QtWidgets.QPushButton('Mirror')
        self.pushButtonClear = QtWidgets.QPushButton('Clear')

    def __initSignals(self):
        pass

    def __onPushButtonMirrorClicked(self):
        pass

    def __onPushButtonClearClicked(self):
        pass

    def __onLineEditMirrorTextChanged(self, text):
        print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
