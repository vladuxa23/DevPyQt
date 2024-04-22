from PySide6 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        super(Window, self).paintEvent(event)
        painter = QtGui.QPainter(self)

        line_1 = QtCore.QLine(10, 10, 100, 60)
        line_2 = QtCore.QLine(100, 70, 20, 30)

        painter.drawLines([line_1, line_2])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()
    myapp.show()

    app.exec()
