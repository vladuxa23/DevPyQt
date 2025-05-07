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

        self.setFixedSize(300, 500)

        self.label = QtWidgets.QLabel("<H1>Нажми</H1> на меня")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.installEventFilter(self)  # Установка фильтра событий на конкретный виджет

        self.label_2 = QtWidgets.QLabel("<H1 style='color:red'>Вторая</H1> кнопка")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.installEventFilter(self)  # Установка фильтра событий на конкретный виджет

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label_2)
        self.setLayout(layout)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Настройка дополнительного поведения виджетов

        :param watched: QtCore.QObject
        :param event: QtCore.QEvent
        :return: bool
        """

        # print(watched, event)

        if watched == self.label and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            print("mouse pressed")

        if watched == self.label and event.type() == QtCore.QEvent.Type.Wheel:
            print("wheel changed")
            print(type(event))

        if watched == self.label_2 and event.type() == QtCore.QEvent.Type.MouseButtonDblClick:
            print("dbl click")

        return super(Window, self).eventFilter(watched, event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
