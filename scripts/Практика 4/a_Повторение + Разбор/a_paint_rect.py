from PySide6 import QtCore, QtWidgets, QtGui


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        pen = QtGui.QPen()
        pen.setColor(QtCore.Qt.GlobalColor.red)
        # pen.setBrush(QtCore.Qt.BrushStyle.Dense4Pattern)

        brush = QtGui.QBrush()
        brush.setColor(QtCore.Qt.GlobalColor.green)

        painter.setPen(pen)
        painter.setBrush(brush)

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

    myapp = Widget()
    myapp.show()

    app.exec()
