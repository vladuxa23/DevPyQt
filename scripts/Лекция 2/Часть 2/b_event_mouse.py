"""
Перехват и обработка событий мыши
"""

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
        self.setMouseTracking(True)

        self.label = QtWidgets.QLabel("Нажми на меня")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Обработка событий движения мыши

        :param event: QtGui.QMouseEvent
        :return: None
        """

        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Обработка событий нажатия мыши

        :param event: QtGui.QMouseEvent
        :return: None
        """

        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Обработка событий отпускания мыши

        :param event: QtGui.QMouseEvent
        :return: None
        """

        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Обработка событий двойного нажатия мыши

        :param event: QtGui.QMouseEvent
        :return: None
        """

        self.label.setText("mouseDoubleClickEvent")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
