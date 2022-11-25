"""
Открытие нескольких окон из основного
"""

from time import ctime

from PySide6 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initChilds()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setFixedSize(300, 100)

        self.pb = QtWidgets.QPushButton("Открыть")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pb)

        self.setLayout(layout)

    def initChilds(self) -> None:
        """
        Инициализация дочерних окон

        :return: None
        """

        # self.child_window = OtherWindow()
        self.child_window = OtherWindow(self)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pb.clicked.connect(self.open_child_window)

        self.child_window.send_data.connect(lambda x: print(f"{ctime()} Main {x}"))

    def open_child_window(self) -> None:
        """
        Открытие второго окна

        :return: None
        """

        self.child_window.show()


class OtherWindow(QtWidgets.QWidget):
    send_data = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setFixedSize(300, 300)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.send_data.connect(lambda x: print(f"{ctime()} Child {x}"))  # перехватываем сигнал внутри приложения

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Обработка нажатия мыши в виджете

        :param event: QtGui.QMouseEvent
        :return: None
        """

        self.send_data.emit(str(event.buttons()))
        print()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()
