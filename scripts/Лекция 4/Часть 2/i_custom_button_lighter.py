from PySide6 import QtCore, QtWidgets, QtGui


class PushButtonLighter(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.count = 0

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setMinimumSize(60, 180)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.clicked.connect(self.changeColor)

    def changeColor(self) -> None:
        """
        Изменение цвета

        :return: None
        """

        self.count += 1
        if self.count > 2:
            self.count = 0
        self.update()  # Перерисовка виджета

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        """
        Переопределение метода отрисовки виджета

        :param event: событие рисования
        :return: None
        """

        painter = QtGui.QPainter(self)
        traffic_lights_color = {0: QtCore.Qt.red, 1: QtCore.Qt.yellow, 2: QtCore.Qt.green}
        ellipse_y = 0

        for i in range(3):
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 4))
            painter.setBrush(QtGui.QBrush(QtCore.Qt.gray))

            if self.count == i:
                painter.setBrush(QtGui.QBrush(traffic_lights_color.get(i)))

            painter.drawEllipse(5, 5 + ellipse_y, self.width() - 10, (self.height() - 10) / 3)
            ellipse_y += ((self.height() - 10) / 3)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = PushButtonLighter()
    myapp.show()

    app.exec_()
