"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtCore, QtGui


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


class CommonWidget(QtWidgets.QWidget):
    def __init__(self, parnet=None):
        super().__init__(parnet)

        self.move(1200, 800)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)  # Удаление titleBar

        g = QtGui.QGuiApplication.primaryScreen().availableGeometry()

        self.move(
            g.right() - self.frameGeometry().width(),
            g.bottom() - self.frameGeometry().height()
        )


        self.clockWidget = ClockWidget()
        self.label = QtWidgets.QLabel("ЦИФРОВЫЕ ЧАСЫ")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.label)
        l.addWidget(self.clockWidget)

        self.setLayout(l)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    w = CommonWidget()
    w.show()

    app.exec()
