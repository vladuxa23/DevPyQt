"""
Простейшее использование класса QTimer
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initTimers()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.labelTime = QtWidgets.QLabel()
        self.labelTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.labelTime)
        layout.addWidget(QtWidgets.QPlainTextEdit())

        self.setLayout(layout)

        self.showTime()

    def initTimers(self) -> None:
        """
        Инициализация таймеров

        :return: None
        """

        self.timeTimer = QtCore.QTimer()
        self.timeTimer.setInterval(1000)
        self.timeTimer.start()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.timeTimer.timeout.connect(self.showTime)

    def showTime(self) -> None:
        """
        Слот для отображения в labelTime текущего времени

        :return: None
        """

        time = QtCore.QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.labelTime.setText(timeDisplay)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
