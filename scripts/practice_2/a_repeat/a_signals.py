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
        self.lineEditInput.setPlaceholderText("Введите фразу")

        self.lineEditMirror = QtWidgets.QLineEdit()

        self.pushButtonMirror = QtWidgets.QPushButton('Mirror')
        self.pushButtonClear = QtWidgets.QPushButton('Clear')

        l_lineEdit = QtWidgets.QHBoxLayout()
        l_lineEdit.addWidget(self.lineEditInput)
        l_lineEdit.addWidget(self.lineEditMirror)

        l_pushButton = QtWidgets.QHBoxLayout()
        l_pushButton.addWidget(self.pushButtonMirror)
        l_pushButton.addWidget(self.pushButtonClear)

        l_main = QtWidgets.QVBoxLayout()
        l_main.addLayout(l_lineEdit)
        l_main.addLayout(l_pushButton)

        self.setLayout(l_main)

    def __initSignals(self):
        self.pushButtonMirror.clicked.connect(self.__onPushButtonMirrorClicked)
        self.pushButtonClear.clicked.connect(self.__onPushButtonClearClicked)
        self.lineEditInput.textChanged.connect(self.__onLineEditMirrorTextChanged)

    def __onPushButtonMirrorClicked(self):
        self.lineEditMirror.setText(self.lineEditInput.text()[::-1])

    def __onPushButtonClearClicked(self):
        self.lineEditMirror.clear()
        self.lineEditInput.clear()

    def __onLineEditMirrorTextChanged(self, text):
        self.lineEditMirror.setText(text[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
