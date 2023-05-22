from PySide6 import QtCore, QtWidgets, QtGui


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0

        pb = QtWidgets.QPushButton("Some text", parent=self)
        pb.setStyleSheet("""""")

        pb.move(50, 50)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        print(event)
        painter = QtGui.QPainter(self)

        pen = QtGui.QPen()
        pen.setColor(QtCore.Qt.GlobalColor.darkBlue)
        # pen.setBrush(QtCore.Qt.BrushStyle.Dense4Pattern)

        brush = QtGui.QBrush()
        color = QtGui.QColor(QtCore.Qt.GlobalColor.blue)
        color.setAlphaF(0.6)
        brush.setColor(color)
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)

        painter.setPen(pen)
        painter.setBrush(brush)

        w, h = self.x2 - self.x1, self.y2 - self.y1
        painter.drawLine(50, 100, 200, 300)
        painter.drawRect(self.x1, self.y1, w, h)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        print(event)
        self.x2, self.y2 = event.x(), event.y()
        self.repaint()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        print(event)
        self.x1, self.y1 = event.x(), event.y()
        self.x2, self.y2 = event.x(), event.y()
        self.repaint()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Widget()
    myapp.show()

    app.exec()
