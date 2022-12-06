import time
from PySide2 import QtCore, QtWidgets, QtGui


class MyQPixmap(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        for i in QtGui.QImageReader.supportedImageFormats():
            print(str(i, "ascii"), end=" ")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyQPixmap()
    myapp.show()

    app.exec_()
