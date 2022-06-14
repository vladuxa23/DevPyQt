import time
from PySide2 import QtCore, QtWidgets, QtGui


class MyDrawRect(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyDrawRect, self).__init__(parent)
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        w, h = self.x2 - self.x1, self.y2 - self.y1
        painter.drawRect(self.x1, self.y1, w, h)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        self.x2, self.y2 = event.x(), event.y()
        self.repaint()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.x1, self.y1 = event.x(), event.y()
        self.x2, self.y2 = event.x(), event.y()
        self.repaint()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyDrawRect()
    myapp.show()

    app.exec_()
