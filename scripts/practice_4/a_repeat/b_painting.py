from PySide6 import QtCore, QtGui, QtWidgets

COLORS = [
    '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
    '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
    '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]


class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()

        self.color = color
        self.setFixedSize(QtCore.QSize(24, 24))
        self.setStyleSheet(f"border: 1px solid black; border-radius: 12px;background-color: {self.color};")

        self.setCheckable(True)

    def setActive(self, status):
        if status:
            self.setActivate()
        else:
            self.setDeactivate()

    def setActivate(self):
        self.setStyleSheet(f"border: 3px solid white; border-radius: 10px;background-color: {self.color};")

    def setDeactivate(self):
        self.setStyleSheet(f"border: 1px solid black; border-radius: 10px;background-color: {self.color};")


class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        self.pen_color = QtGui.QColor('#000000')

        pixmap = QtGui.QPixmap(600, 300)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None

    def set_pen_color(self, color):
        self.pen_color = QtGui.QColor(color)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.last_x is None:  # Первое срабатывание
            self.last_x = event.position().x()
            self.last_y = event.position().y()
            return  # Игнорируем его

        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, event.position().x(), event.position().y())
        painter.end()
        self.setPixmap(canvas)

        # Обновляем глобальные параметры точек X и Y
        self.last_x = event.position().x()
        self.last_y = event.position().y()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.last_x = None
        self.last_y = None


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.canvas = Canvas()

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addLayout(palette)

        self.setLayout(layout)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            b.clicked.connect(self.chooseButton)
            layout.addWidget(b)

    def chooseButton(self):
        l = self.layout().itemAt(1).layout()
        for i in range(l.count()):
            widget = l.itemAt(i).widget()
            if widget is self.sender():
                widget.setActivate()
                continue
            widget.setDeactivate()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
