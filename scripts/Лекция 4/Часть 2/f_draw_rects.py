from PySide6 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        rects = [QtCore.QRect(10, 10, 100, 60),
                 QtCore.QRect(20, 20, 100, 60)]

        painter.drawRects(rects)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()
    myapp.show()

    app.exec()
