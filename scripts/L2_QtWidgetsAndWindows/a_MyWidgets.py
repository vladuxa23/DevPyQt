import sys
from PySide2 import QtWidgets, QtCore


class MyWidgets(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        btn = QtWidgets.QPushButton("Кнопка", self)
        btn.move(30, 30)

        self.setMinimumSize(QtCore.QSize(200, 200))
        self.setMaximumSize(QtCore.QSize(200, 200))

        # self.initUi()

        # self.pushButton.clicked.connect(self.print_something)  # Добавляем слот для сигнала нажатия
        # print(self.layout())

    # def print_something(self):
    #     print("Hello")

    # def initUi(self):
    #     layout = QtWidgets.QVBoxLayout()

    # self.pushButton = QtWidgets.QPushButton("Кнопка")
    # self.radioButton = QtWidgets.QRadioButton("some text")
    # self.checkBox = QtWidgets.QCheckBox("check box")
    # self.radioButton.setChecked(True)
    # self.combo = QtWidgets.QComboBox()
    # self.combo.addItems(["abc", "bca"])

    # self.slider = QtWidgets.QSlider()
    # self.slider.setOrientation(QtCore.Qt.Vertical)

    # layout.addWidget(self.pushButton)
    # layout.addWidget(self.radioButton)
    # layout.addWidget(self.combo)
    # layout.addWidget(self.slider)
    # self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
