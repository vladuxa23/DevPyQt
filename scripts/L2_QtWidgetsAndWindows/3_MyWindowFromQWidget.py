import sys
from PySide2 import QtWidgets, QtGui


class MyWidgets(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        abc = QtWidgets.QPushButton("Текст кнопки")

        checkbox = QtWidgets.QCheckBox("Флажок")
        checkbox.setChecked(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(abc)
        layout.addWidget(checkbox)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
