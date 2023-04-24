import psutil
import platform
import time

import pythoncom
import win32com.client
from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.initUi()
        self.initSignals()

    def initSignals(self):
        self.systemInfoTread.systemInfoReceived.connect(self.updateSystemInfo)
        self.processInfoThread.processInfoReceived.connect(self.updateProcessInfo)
        self.serviceInfoThread.serviceInfoReceived.connect(self.updateServiceInfo)
        self.spinBox.valueChanged.connect(self.onSpinBoxValueChanged)
        self.taskInfoThread.taskInfoReceived.connect(self.updateTaskInfo)

    def initThreads(self):
        self.systemInfoTread = SystemViewerTread()
        self.systemInfoTread.start()
        self.processInfoThread = ProcessInfoThread()
        self.processInfoThread.start()
        self.serviceInfoThread = ServiceInfoThread()
        self.serviceInfoThread.start()
        self.taskInfoThread = TaskInfoThread()
        self.taskInfoThread.start()

    def initUi(self):
        """

        """
        self.systemPlaintextEdit = QtWidgets.QPlainTextEdit()
        self.systemPlaintextEdit.setReadOnly(True)
        self.proccesPlaintextEdit = QtWidgets.QPlainTextEdit()
        self.proccesPlaintextEdit.setReadOnly(True)
        self.servisePlaintextedit = QtWidgets.QPlainTextEdit()
        self.servisePlaintextedit.setReadOnly(True)
        self.tasksPlaintextEdit = QtWidgets.QPlainTextEdit()

        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.addTab(self.systemPlaintextEdit, 'Система')
        self.tabWidget.addTab(self.proccesPlaintextEdit, 'Процессы')
        self.tabWidget.addTab(self.servisePlaintextedit, 'Службы')
        self.tabWidget.addTab(self.tasksPlaintextEdit, 'Задачи')

        self.spinBoxLabel = QtWidgets.QLabel("Чатсота обновления")
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setRange(1, 30)

        spinboxLayout = QtWidgets.QHBoxLayout()
        spinboxLayout.addWidget(self.spinBoxLabel)
        spinboxLayout.addWidget(self.spinBox)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.tabWidget)
        mainLayout.addLayout(spinboxLayout)

        self.setLayout(mainLayout)
        self.setMinimumSize(500, 400)

    def updateSystemInfo(self, data):
        self.systemPlaintextEdit.clear()
        for i in data:
            self.systemPlaintextEdit.appendPlainText(f"{i} {data[i]}")

    def updateProcessInfo(self, data):
        self.proccesPlaintextEdit.clear()
        for i in data:
            self.proccesPlaintextEdit.appendPlainText(str(i.info))

    def updateServiceInfo(self, data):
        self.servisePlaintextedit.clear()
        for i in data:
            self.servisePlaintextedit.appendPlainText(str(i))

    def updateTaskInfo(self, data):
        self.tasksPlaintextEdit.clear()
        for i in data:
            self.tasksPlaintextEdit.appendPlainText(str(i))

    def onSpinBoxValueChanged(self, value):
        self.systemInfoTread.delay = value
        self.taskInfoThread.delay = value
        self.serviceInfoThread.delay = value
        self.taskInfoThread.delay = value

class SystemViewerTread(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = {}
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while True:
            self.data["Название процессора:"] = platform.processor()
            self.data["Логических ядер:"] = psutil.cpu_count(logical=True)
            self.data["Физических ядер:"] = psutil.cpu_count(logical=False)
            self.data["Загрузка процессора, %:"] = psutil.cpu_percent()
            self.data["Оперативной памяти, Гб:"] = round(psutil.virtual_memory().total/1073741824, 2)
            self.data["Использовано памяти, %:"] = psutil.virtual_memory().percent
            self.data["Количество дисков:"] = len(psutil.disk_partitions())
            pathes = [i.mountpoint for i in psutil.disk_partitions()]
            self.data["Всего/использовано, Гб/Гб"] = \
                [f"{round(psutil.disk_usage(i).total/1073741824, 2)}/{round(psutil.disk_usage(i).used/1073741824, 2)}" for i in pathes]
            self.systemInfoReceived.emit(self.data)
            time.sleep(self.delay)


class ProcessInfoThread(QtCore.QThread):
    processInfoReceived = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while True:
            self.data = psutil.process_iter(['pid', 'name', 'username'])
            self.processInfoReceived.emit(self.data)
            time.sleep(self.delay)


class ServiceInfoThread(QtCore.QThread):
    serviceInfoReceived = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while True:
            self.data = psutil.win_service_iter()
            self.serviceInfoReceived.emit(self.data)
            time.sleep(self.delay)

class TaskInfoThread(QtCore.QThread):
    taskInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None



    def run(self) -> None:
        if self.delay is None:
            self.delay = 5

        pythoncom.CoInitialize()

        while True:
            scheduler = win32com.client.dynamic.Dispatch('Schedule.Service')
            scheduler.Connect()
            # print(type(scheduler))
            tasks = scheduler.GetRunningTasks(1)
            names = [tasks.Item(i+1).Name for i in range(tasks.Count)]
            print(names)
            self.taskInfoReceived.emit(names)
            time.sleep(self.delay)


if __name__ == "__main__":

    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
