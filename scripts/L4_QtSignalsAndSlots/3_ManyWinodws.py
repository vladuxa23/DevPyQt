import sys
from PySide2 import QtCore, QtWidgets, QtGui


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        button1 = QtWidgets.QPushButton("Другое окно", self)
        button1.clicked.connect(self.showChild)

    def showChild(self):
        self.childWindow = Child()
        self.childWindow.show()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.childWindow.close()
        event.accept()


class Child(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        label = QtWidgets.QLabel("Другое окно", self)
        label.move(10, 10)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())
