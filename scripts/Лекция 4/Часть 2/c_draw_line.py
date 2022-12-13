from PySide6 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        # через QPoint
        p1 = QtCore.QPoint(10, 10)
        p2 = QtCore.QPoint(100, 60)
        painter.drawLine(p1, p2)

        # через координаты
        painter.drawLine(25, 25, 80, 80)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()
    myapp.show()

    app.exec()
