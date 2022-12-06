import time
from PySide2 import QtCore, QtWidgets, QtGui


class MyDrawing(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyDrawing, self).__init__(parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        # p1 = QtCore.QPoint(10, 10)
        # p2 = QtCore.QPoint(100, 60)
        painter.drawLine(p1, p2)

        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setStyle(QtCore.Qt.DashDotLine)

        brush = QtGui.QBrush(QtCore.Qt.darkGray)
        brush.setStyle(QtCore.Qt.Dense3Pattern)
        pen.setBrush(brush)
        painter.setPen(pen)
        # painter.setBrush(brush)

        rects = [QtCore.QRect(10, 10, 100, 60),
                 QtCore.QRect(20, 20, 100, 60)]
        painter.drawRects(rects)

        # painter.drawArc(50, 20, 500, 200, 4*0, 16*90)

        # painter.drawEllipse(50, 20, 500, 200)

        # painter.drawRect(10, 10, 100, 60)
        # painter.drawLines([QtCore.QLine(10, 10, 100, 60),
        #                    QtCore.QLine(100, 60, 20, 30)])
        # x1, y1 = 10, 10
        # x2, y2 = 100, 60
        # painter.drawLines(x1, y1, x2, y2)
        # p1 = QtCore.QPoint(10, 10)
        # p2 = QtCore.QPoint(100, 60)
        # painter.drawLine(p1, p2)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyDrawing()
    myapp.show()

    app.exec_()
