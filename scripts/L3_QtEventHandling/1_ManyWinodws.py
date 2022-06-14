import sys
from PySide2 import QtCore, QtWidgets, QtGui


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.childWindow = Child()

        self.button1 = QtWidgets.QPushButton("1", self)
        self.button1.move(50, 0)
        self.button2 = QtWidgets.QPushButton("2", self)
        self.button2.move(0, 50)

        self.button1.clicked.connect(self.showChild)

    def showChild(self):
        self.childWindow.show()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.childWindow.close()
        event.accept()


class Child(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        label = QtWidgets.QLabel("Другое окно", self)
        label.move(10, 10)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())
