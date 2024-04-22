from PySide6 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        painter.drawRect(QtCore.QRect(10, 20, 200, 80))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()
    myapp.show()

    app.exec()
