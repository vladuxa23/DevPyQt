import sys
from PySide2 import QtWidgets, QtGui


class MyWidgets(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        abc = QtWidgets.QPushButton("Текст кнопки")

        checkbox = QtWidgets.QCheckBox("Флажок")
        checkbox.setChecked(True)
        print(checkbox.isChecked())

        layout.addWidget(abc)
        layout.addWidget(checkbox)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
