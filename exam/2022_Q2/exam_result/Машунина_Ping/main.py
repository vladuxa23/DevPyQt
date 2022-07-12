import sys, os
import subprocess, platform, requests
from PySide2 import QtWidgets, QtCore, QtGui
import time


class MainWindow(QtWidgets.QWidget):
    """Вызов главного окна"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ip_list_save = QtCore.QSettings("PingMonitoring")  #QSettings - папка для сохранения IP
        self.initUI()

        #Отдельный поток для ping
        self.IpChecker = ThreadPingIP()
        self.IpChecker.IpPingThread.connect(self.updateLogFile, QtCore.Qt.AutoConnection)

        #Отдельный поток для трассировки
        self.IpTracert = ThreadTracertIP()
        self.IpTracert.IpTracertThread.connect(self.updateTracertFile, QtCore.Qt.AutoConnection)

    def initUI(self):
        main_layout = QtWidgets.QVBoxLayout()

        # Установка IP
        self.labelName = QtWidgets.QLabel("Список IP адресов:")

        list_ip = self.ip_list_save.value("list_ip", [])
        self.startIP = QtWidgets.QLineEdit()
        self.endIP = QtWidgets.QLineEdit()
        if list_ip:
            self.startIP.setText(list_ip[0])
        if list_ip:
            self.endIP.setText(list_ip[1])

        # Слоты для запуска
        self.buttonPing = QtWidgets.QPushButton()
        self.buttonPing.setText("Начать мониторинг")
        self.buttonPing.setCheckable(True)
        self.buttonPing.clicked.connect(self.handlePing)

        # Слоты для tracert
        self.buttonTracert = QtWidgets.QPushButton()
        self.buttonTracert.setText("Tracert")
        self.buttonTracert.setCheckable(True)
        self.buttonTracert.clicked.connect(self.handleTracert)

        #Слоты для прогресс бара, Лога и трассировки
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setRange(0, 0)

        self.labelLog = QtWidgets.QLabel("Лог")
        self.textEditLog = QtWidgets.QPlainTextEdit()

        self.labelTracert = QtWidgets.QLabel("Данные о трассировке")
        self.textEditTracert = QtWidgets.QPlainTextEdit()

        #Установка все на слой
        main_layout.addWidget(self.labelName)
        main_layout.addWidget(self.startIP)
        main_layout.addWidget(self.endIP)

        main_layout.addWidget(self.buttonPing)
        main_layout.addWidget(self.buttonTracert)
        main_layout.addWidget(self.progressBar)
        main_layout.addWidget(self.labelLog)
        main_layout.addWidget(self.textEditLog)
        main_layout.addWidget(self.labelTracert)
        main_layout.addWidget(self.textEditTracert)

        self.setLayout(main_layout)

    def handlePing(self):
        "Слот для кнопки запуска мониторинга"
        if self.buttonPing.isChecked():
            self.IpChecker.setIP(self.startIP.text(), self.endIP.text())
            self.IpChecker.start()
            self.buttonPing.setText("Остановить мониторинг")
        else:
            self.buttonPing.setText("Начать мониторинг")
            self.buttonPing.setChecked(False)
            self.IpChecker.status = False

    def handleTracert(self):
        """Слот для кнопки трассировки"""
        self.IpTracert.setTracertIP(self.startIP.text())
        self.IpTracert.start()


    def updateLogFile(self, emit_value):
        """Функция для обнволения лог файла"""
        self.textEditLog.appendPlainText(time.ctime() + "    " + str(emit_value))

    def updateTracertFile(self, emit_value):
        """Функция для обнволения tracert файла"""
        self.textEditTracert.appendPlainText(str(emit_value))


    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """Функция для сохранения IP при закрытии"""
        self.ip_list_save.setValue("list_ip", [self.startIP.text(), self.endIP.text()])
        print("Приложение закрылось")


class ThreadPingIP(QtCore.QThread):
    "Класс потока для пинга"
    IpPingThread = QtCore.Signal(tuple)

    def setIP(self, pingIP1, pingIP2):
        self.__ip = [str(pingIP1), str(pingIP2)]


    def run(self):
        self.status = True
        ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"

        while self.status:
            for ip_addr in self.__ip:
                args = ["ping", ping_str, ip_addr]
                # need_sh = False if platform.system().lower() == "windows" else True
                pr = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                stdout, stderr = pr.communicate()
                self.IpPingThread.emit((ip_addr, self.check_ip_status(ip_addr)))
                time.sleep(1)


    def check_ip_status(self, ip_addr) -> bool:
        response = os.popen(f"ping {ip_addr}").read()
        if "Received = 4" in response:
            return True
        else:
            return False

class ThreadTracertIP(QtCore.QThread):
    """Класс потока для трассировки"""
    IpTracertThread = QtCore.Signal(str)

    def setTracertIP(self, pingIP1): #Реализован один
        "Функция для установки адреса для tracert"
        self.__ip1 = pingIP1


    def run(self):
        args = f"tracert {self.__ip1}"
        pr = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = pr.communicate()
        self.IpTracertThread.emit(stdout.decode("cp866", "ignore"))


if __name__ == "__main__":

    app = QtWidgets.QApplication()
    windows = MainWindow()
    windows.show()
    app.exec_()
