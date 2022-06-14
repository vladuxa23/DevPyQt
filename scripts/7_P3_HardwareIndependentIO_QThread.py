import time
import psutil
import requests
from PySide2 import QtCore, QtWidgets, QtGui
from res.ui import P3_HardwareIndependentIO_QThread_design


# ЗАДАНИЯ:
# 1. Реализовать таймер до 0 с возможностью остановки
# 2. Бесконечная проверка доступности сайта с возможностью остановки и установки времени задержки (при запуске)
# 3. Получение системных параметров (запуск при старте программы), предусмотреть "горячий" режим установки времени задержки

# Все 3 блока должны быть реализованы в одном окне и работать одновременно друг с другом

class QThreadPractice(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QThreadPractice, self).__init__(parent)

        self.ui = P3_HardwareIndependentIO_QThread_design.Ui_Form()
        self.ui.setupUi(self)

        self.timerThread = MyTimer()
        self.timerThread.timeLeftSignal.connect(self.updateLineEditTimeLeft, QtCore.Qt.AutoConnection)
        self.timerThread.finished.connect(self.timerFinished)

        self.urlChecker = MyUrlChecker()
        self.urlChecker.urlResponceSignal.connect(self.updateUrlCheck, QtCore.Qt.AutoConnection)

        self.systemInfo = SystemInfoThread()
        self.systemInfo.start()
        self.systemInfo.systemInfoSignal.connect(self.updateSystemInfo, QtCore.Qt.AutoConnection)
        self.ui.spinBoxSystemInfoDelay.valueChanged.connect(self.setSystemInfoDelay)

        self.ui.pushButtonTimerStart.clicked.connect(self.handleTimer)
        self.ui.pushButtonUrlCheckStart.clicked.connect(self.handleUrl)

    # Слоты для таймера
    def handleTimer(self):
        if self.ui.pushButtonTimerStart.isChecked():
            self.ui.lineEditTimerEnd.setText(str(self.ui.spinBoxTimerCount.value()))
            self.timerThread.setTimer(self.ui.spinBoxTimerCount.value())
            self.timerThread.start()
            self.ui.pushButtonTimerStart.setText("Стоп")
        else:
            self.timerFinished()

    def timerFinished(self):
        self.ui.pushButtonTimerStart.setText("Начать отсчёт")
        self.ui.pushButtonTimerStart.setChecked(False)
        self.timerThread.status = False

    # Слоты для url
    def handleUrl(self):
        if self.ui.pushButtonUrlCheckStart.isChecked():
            self.urlChecker.setUrl(self.ui.lineEditURL.text())
            self.urlChecker.setDelay(self.ui.spinBoxUrlCheckTime.value())
            self.urlChecker.start()
            self.ui.pushButtonUrlCheckStart.setText("Стоп")
        else:
            self.ui.pushButtonUrlCheckStart.setText("Начать проверку")
            self.ui.pushButtonUrlCheckStart.setChecked(False)
            self.urlChecker.status = False

    def updateLineEditTimeLeft(self, count):
        self.ui.lineEditTimerEnd.setText(str(count))

    def updateUrlCheck(self, status_code):
        self.ui.plainTextEditUrlCheckLog.appendPlainText(f"{time.ctime()} - Статус {status_code}")

    # Слоты для system_info
    def updateSystemInfo(self, info_list):
        self.ui.progressBarCPU.setValue(info_list[0])
        self.ui.labelCPUPercent.setText(f"{info_list[0]} %")
        self.ui.progressBarRAM.setValue(info_list[1])
        self.ui.labelRAMPercent.setText(f"{info_list[1]} %")

    def setSystemInfoDelay(self):
        self.systemInfo.delay = self.ui.spinBoxSystemInfoDelay.value()

class MyTimer(QtCore.QThread):
    timeLeftSignal = QtCore.Signal(int)

    def setTimer(self, count):
        self.__timerCount = count

    def run(self):
        self.status = True

        while self.status:
            if not self.__timerCount == 0:
                self.__timerCount -= 1
                time.sleep(1)
                self.timeLeftSignal.emit(self.__timerCount)
            else:
                self.status = False


class MyUrlChecker(QtCore.QThread):
    urlResponceSignal = QtCore.Signal(int)

    def setUrl(self, url):
        self.__url = url

    def setDelay(self, delay):
        self.__delay = delay

    def run(self):
        self.status = True

        while self.status:
            responce = requests.get(self.__url)
            self.urlResponceSignal.emit(responce.status_code)
            time.sleep(self.__delay)


class SystemInfoThread(QtCore.QThread):
    systemInfoSignal = QtCore.Signal(list)

    def run(self):
        self.delay = 1
        while True:
            cpu_value = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            ram_value = int(ram.used * 100 / ram.total)
            self.systemInfoSignal.emit([cpu_value, ram_value])
            time.sleep(self.delay)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = QThreadPractice()
    # myapp.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    myapp.show()

    app.exec_()
