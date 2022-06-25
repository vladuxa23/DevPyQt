import time
import psutil
import requests
from requests.exceptions import MissingSchema
from PySide2 import QtCore, QtWidgets
from ui.QThread_design import Ui_Form


class QThreadPractice(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.timerThread = None
        self.urlCheckerThread = None
        self.systemInfoThread = None

        self.initThreads()
        self.initUi()

    def initThreads(self):
        # init threads
        self.timerThread = TimerThread()
        self.urlCheckerThread = UrlCheckerThread()
        self.systemInfoThread = SystemInfoThread()

        # init threads signals
        self.timerThread.timerSignal.connect(self.timerThreadTimerSignal)
        self.timerThread.finished.connect(self.timerThreadFinished)

        self.urlCheckerThread.urlSignal.connect(self.urlCheckerThreadUrlSignal)
        self.urlCheckerThread.logSignal.connect(self.urlCheckerThreadUrlSignal)

        self.systemInfoThread.systemSignal.connect(self.systemInfoThreadSystemSignal)

        # run threads
        self.systemInfoThread.start()

    def initUi(self):

        # init widget signals
        self.ui.spinBoxSystemInfoDelay.valueChanged.connect(self.setSystemInfoDelay)

        self.ui.pushButtonTimerStart.clicked.connect(self.onPushButtonTimerStartClicked)
        self.ui.pushButtonUrlCheckStart.clicked.connect(self.onPushButtonUrlCheckStartClicked)

    # Слоты для таймера
    def onPushButtonTimerStartClicked(self) -> None:
        """
        Слот для кнопки потока self.timerThread

        :return: None
        """

        if self.ui.pushButtonTimerStart.isChecked():
            self.ui.lineEditTimerEnd.setText(str(self.ui.spinBoxTimerCount.value()))
            self.timerThread.setTimer(self.ui.spinBoxTimerCount.value())
            self.timerThread.start()
            self.ui.pushButtonTimerStart.setText("Стоп")
        else:
            self.timerThreadFinished()

    def timerThreadTimerSignal(self, count) -> None:
        """
        Слот для обработки сигнала timerSignal, который шлёт данные из потока self.timerThread

        :param count: число оставшихся секунд
        :return: None
        """

        self.ui.lineEditTimerEnd.setText(str(count))

    def timerThreadFinished(self) -> None:
        """
        Слот для сигнала finished потока self.timerThread

        :return: None
        """

        self.ui.pushButtonTimerStart.setText("Начать отсчёт")
        self.ui.pushButtonTimerStart.setChecked(False)
        self.timerThread.status = False

    # Слоты для url
    def onPushButtonUrlCheckStartClicked(self) -> None:
        """
        Слот для кнопки потока self.urlCheckerThread

        :return: None
        """

        if self.ui.pushButtonUrlCheckStart.isChecked():
            self.urlCheckerThread.setUrl(self.ui.lineEditURL.text())
            self.urlCheckerThread.setDelay(self.ui.spinBoxUrlCheckTime.value())
            self.urlCheckerThread.start()
            self.ui.pushButtonUrlCheckStart.setText("Стоп")
        else:
            self.ui.pushButtonUrlCheckStart.setText("Начать проверку")
            self.ui.pushButtonUrlCheckStart.setChecked(False)
            self.urlCheckerThread.status = False

    def urlCheckerThreadUrlSignal(self, status_code) -> None:
        """
        Слот для обработки сигнала urlSignal, который шлёт данные из потока self.urlCheckerThread

        :param status_code: статус код, который вернул сайт
        :return: None
        """

        if isinstance(status_code, MissingSchema):
            self.ui.plainTextEditUrlCheckLog.appendPlainText(str(status_code))
        else:
            self.ui.plainTextEditUrlCheckLog.appendPlainText(f"{time.ctime()} - Статус {status_code}")

    # Слоты для system_info
    def systemInfoThreadSystemSignal(self, info_list) -> None:
        """
        Слот для обработки сигнала systemSignal, который шлёт данные из потока self.systemInfo

        :param info_list: значение полученное из потока self.systemInfo
        :return: None
        """

        self.ui.progressBarCPU.setValue(info_list[0])
        self.ui.labelCPUPercent.setText(f"{info_list[0]} %")
        self.ui.progressBarRAM.setValue(info_list[1])
        self.ui.labelRAMPercent.setText(f"{info_list[1]} %")

    def setSystemInfoDelay(self) -> None:
        """
        Слот для установки значения времени задержки обновления системных параметров

        :return: None
        """

        self.systemInfoThread.delay = self.ui.spinBoxSystemInfoDelay.value()


class TimerThread(QtCore.QThread):
    timerSignal = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__timerCount = None

    def setTimer(self, count) -> None:
        """
        Метод для установки начального значения таймера

        :param count: значение таймера
        :return: None
        """

        self.__timerCount = count

    def run(self) -> None:
        self.status = True

        while self.status:
            if self.__timerCount < 1:
                break

            time.sleep(1)
            self.__timerCount -= 1
            self.timerSignal.emit(self.__timerCount)


class UrlCheckerThread(QtCore.QThread):
    urlSignal = QtCore.Signal(int)
    logSignal = QtCore.Signal(Exception)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__url = None
        self.__delay = None
        self.status = None

    def setUrl(self, url) -> None:
        """
        Метод для установки url который будем проверять

        :param url: адрес сайта для проверки
        :return: None
        """

        self.__url = url

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:

        if self.__url is None:
            self.__url = "http://www.google.com"

        if self.__delay is None:
            self.__delay = 10

        self.status = True

        while self.status:
            try:
                response = requests.get(self.__url)
                self.urlSignal.emit(response.status_code)
                time.sleep(self.__delay)
            except MissingSchema as err:
                self.status = False
                self.logSignal.emit(err)


class SystemInfoThread(QtCore.QThread):
    systemSignal = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            ram_value = int(ram.used * 100 / ram.total)
            self.systemSignal.emit([cpu_value, ram_value])
            time.sleep(self.delay)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = QThreadPractice()
    myapp.show()

    app.exec_()
