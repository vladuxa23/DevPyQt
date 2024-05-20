from PySide6 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setStyle(QtCore.Qt.PenStyle.DashLine)

        brush = QtGui.QBrush()
        brush.setColor("green")
        brush.setStyle(QtCore.Qt.BrushStyle.DiagCrossPattern)

        rects = [QtCore.QRect(10, 10, 100, 60),
                 QtCore.QRect(20, 20, 100, 60)]

        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRects(rects)

        brush.setColor("red")

        rects = [QtCore.QRect(100, 100, 200, 260),
                 QtCore.QRect(200, 200, 300, 360)]
        painter.setBrush(brush)
        painter.drawRects(rects)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()
    myapp.show()

    app.exec()
