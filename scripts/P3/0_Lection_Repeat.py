# Группа 2021-2
import time

from PySide2 import QtCore, QtWidgets

class MyTimer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyTimer, self).__init__(parent)

        self.initUi()

        self.timerTread = MyTimerThread()
        self.timerTread.timer_signal.connect(self.setTimerCount)

        self.timerTread.started.connect(lambda: self.lineEditTimer.setEnabled(False))
        self.timerTread.finished.connect(self.timerFinished)

    def initUi(self):
        self.lineEditTimer = QtWidgets.QLineEdit()
        self.lineEditTimer.setPlaceholderText("Введите количество секунд")

        self.pbStartTimer = QtWidgets.QPushButton()
        self.pbStartTimer.setText("Старт")
        self.pbStartTimer.clicked.connect(self.onPBStartTimerClicked)

        mainLayout = QtWidgets.QVBoxLayout()

        mainLayout.addWidget(self.lineEditTimer)
        mainLayout.addWidget(self.pbStartTimer)

        self.setLayout(mainLayout)

    def onPBStartTimerClicked(self):
        self.timerTread.setCounter(int(self.lineEditTimer.text()))
        self.timerTread.start()

    def setTimerCount(self, count):
        self.lineEditTimer.setText(count)

    def timerFinished(self):
        self.lineEditTimer.setEnabled(True)
        self.lineEditTimer.setText("")


class MyTimerThread(QtCore.QThread):
    timer_signal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(MyTimerThread, self).__init__(parent)

        self.time_count = 0

    def setCounter(self, time_count):
        self.time_count = time_count

    def run(self):
        for i in range(self.time_count, 0, -1):
            self.timer_signal.emit(str(i))
            time.sleep(1)



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyTimer()
    win.show()

    app.exec_()




