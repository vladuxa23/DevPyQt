from PySide6 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        painter.drawArc(50, 20, 500, 200, 4 * 0, 16 * 90)

        # drawArc(x, y, w, h, a, alen) – дуга;
        # x, y, w, h – < int > – область рисования дуги;
        # a – начальный угол(1 / 16 градуса);
        # alen – длина дуги(1 / 16 градуса);

        # 0 = 0
        # 90 = 16 * 90 = 1440
        # 180 = 16 * 180 = 2880
        # 270 = 16 * 270 = 4320
        # 360 = 16 * 360 = 5760


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()
    myapp.show()

    app.exec()
