"""
Открытие нескольких окон из основного
"""

from PySide6 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

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

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pb.clicked.connect(self.open_child_window)

    def open_child_window(self) -> None:
        """
        Открытие второго окна

        :return: None
        """

        self.child_window = OtherWindow()
        self.child_window.show()


class OtherWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setFixedSize(300, 300)
        label = QtWidgets.QLineEdit("Hello", self)
        label.move(10, 10)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()
