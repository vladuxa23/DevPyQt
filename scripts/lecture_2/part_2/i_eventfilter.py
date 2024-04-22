import sys

from PySide6 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setFixedSize(300, 100)

        self.label = QtWidgets.QLabel("<H1>Нажми</H1> на меня")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.installEventFilter(self)  # Установка фильтра событий на конкретный виджет

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Настройка дополнительного поведения виджетов

        :param watched: QtCore.QObject
        :param event: QtCore.QEvent
        :return: bool
        """

        if watched == self.label and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            print("mouse pressed")

        if watched == self.label and event.type() == QtCore.QEvent.Type.Wheel:
            print("wheel changed")
            print(event.angleDelta())

        return super(Window, self).eventFilter(watched, event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
