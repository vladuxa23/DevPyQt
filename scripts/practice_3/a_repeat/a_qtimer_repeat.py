"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""
import time

from PySide6 import QtWidgets, QtCore


class ClockWidget(QtWidgets.QDateTimeEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.showCurrentDateTime()
        self.__initTimer()

    def __initUi(self):
        self.setMinimumSize(290, 45)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("color: green; font-size: 25px; font-weight:600")
        self.setDisplayFormat("dd.MM.yyyy HH:mm:ss")
        self.setEnabled(False)

    def __initTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.showCurrentDateTime)
        self.timer.start()

    def showCurrentDateTime(self):
        current_datetime = QtCore.QDateTime.currentDateTime()
        self.setDateTime(current_datetime)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    w = QtWidgets.QWidget()
    l = QtWidgets.QVBoxLayout()
    lbl = QtWidgets.QLabel("Какой то текст")
    clock = ClockWidget()

    l.addWidget(clock)
    l.addWidget(lbl)

    w.setLayout(l)
    w.show()

    app.exec()
