import time
from PySide2 import QtCore, QtWidgets, QtGui

# Задания

# Реализовать светофор с возможностью смены цвета на нём по клику.

class MyDrawing(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(MyDrawing, self).__init__(parent)

        # Устанавливаем размеры
        self.setMinimumSize(60, 180)
        self.setMaximumSize(60, 180)

        self.clicked.connect(self.changeColor)

        self.count = 0

    def changeColor(self):

        self.count += 1
        if self.count > 2:
            self.count = 0
        self.update()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        traffic_lights_color = {0: QtCore.Qt.red, 1: QtCore.Qt.yellow, 2: QtCore.Qt.green}
        ellipse_y = 0

        for i in range(3):
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 4))
            painter.setBrush(QtGui.QBrush(QtCore.Qt.gray))

            if self.count == i:
                painter.setBrush(QtGui.QBrush(traffic_lights_color.get(i)))

            painter.drawEllipse(5, 5 + ellipse_y, 50, 50)
            ellipse_y += 60


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyDrawing()
    # myapp.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    myapp.show()

    app.exec_()
