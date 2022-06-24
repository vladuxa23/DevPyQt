import time
import psutil
import requests
from PySide2 import QtCore, QtWidgets
from ui.practice_form_design import Ui_Form


class QThreadPractice(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initThread()
        self.initUi()

    def initThread(self):
        # init threads
        self.timerThread = TimerThread()

        # init threads signals
        self.timerThread.timerSignal.connect(self.timerThreadTimerSignal)
        self.timerThread.started.connect(self.timerThreadStarted)
        self.timerThread.finished.connect(self.timerThreadFinished)


    def initUi(self):
        # ui
        self.ui.pushButtonStopTimer.setEnabled(False)

        # signals
        self.ui.pushButtonStartTimer.clicked.connect(self.onPushButtonStartTimerClicked)
        self.ui.pushButtonStopTimer.clicked.connect(self.onPushButtonStopTimerClicked)

    # timerThread SLOTS
    def onPushButtonStartTimerClicked(self):
        self.timerThread.timerCount = self.ui.spinBoxTimerCount.value()
        self.timerThread.start()

    def onPushButtonStopTimerClicked(self):
        self.timerThread.status = False

    def timerThreadTimerSignal(self, emit_value):
        self.ui.lineEditTimerEnd.setText(emit_value)

    def timerThreadStarted(self):
        self.ui.pushButtonStartTimer.setEnabled(False)
        self.ui.pushButtonStopTimer.setEnabled(True)

    def timerThreadFinished(self):
        self.ui.pushButtonStartTimer.setEnabled(True)
        self.ui.pushButtonStopTimer.setEnabled(False)


class TimerThread(QtCore.QThread):
    timerSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.timerCount = None
        self.status = None

    def run(self):
        self.status = True

        if self.timerCount is None:
            self.timerCount = 10

        while self.status:
            if self.timerCount < 1:
                break

            time.sleep(1)
            self.timerCount -= 1
            self.timerSignal.emit(str(self.timerCount))




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = QThreadPractice()
    myapp.show()

    app.exec_()
