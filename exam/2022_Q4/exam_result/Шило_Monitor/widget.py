from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem
from examsysinfo import Ui_Form
from exam_threads import SystemInfo, SystemServices, SystemProc

import psutil
import cpuinfo
import win32com.client


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.sysinfo = SystemInfo()
        self.sysservices = SystemServices()
        self.sysprocs = SystemProc()
        # self.sysscheduler = SystemScheduler()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUi()
        self.initThread()
        self.initSignals()
        self.getInfoSched()

    def initUi(self):
        """
        Иниуиализацтя UI
        :return:
        """
        self.setWindowTitle("Диспетчер")
        self.ui.comboBox.addItem("5")
        self.ui.comboBox.addItem("10")
        self.ui.comboBox.addItem("15")
        self.sysinfo.delay = int(self.ui.comboBox.currentText())
        self.ui.textEdit_proc_name.setEnabled(False)
        self.ui.textEdit_proc_name.setText(
            str(cpuinfo.get_cpu_info()['brand_raw'])
        )
        self.ui.textEdit_proc_core.setEnabled(False)
        self.ui.textEdit_proc_core.setText(
            str(psutil.cpu_count())
        )
        self.ui.textEdit_proc_core_2.setEnabled(False)
        self.ui.textEdit_mem_1.setEnabled(False)
        memory_size = int(psutil.virtual_memory()[0])
        self.ui.textEdit_mem_1.setText(
            str(round(memory_size / 1024 / 1024, 1))
        )
        self.ui.textEdit_mem_2.setEnabled(False)
        available_memory = int(psutil.virtual_memory()[1])
        self.ui.textEdit_mem_2.setText(
            str(round(available_memory / 1024 / 1024, 1))
        )
        self.ui.textEdit_mem_3.setEnabled(False)
        used_memory = int(psutil.virtual_memory()[3])
        self.ui.textEdit_mem_3.setText(
            str(round(used_memory / 1024 / 1024, 1))
        )
        self.ui.textEdit_mem_4.setEnabled(False)

        self.ui.textEdit_HDD.setEnabled(False)
        self.ui.textEdit_HDD.setText(
            f"Объём всего: {round(psutil.disk_usage('/')[0] / 1024 / 1024, 1)} MB\n"
            f"Использовано: {round(psutil.disk_usage('/')[1] / 1024 / 1024, 1)} MB\n"
            f"Свободно: {round(psutil.disk_usage('/')[2] / 1024 / 1024, 1)} MB\n"
            f"Процент: {psutil.disk_usage('/')[3]} %"
        )
        if len(psutil.disk_partitions()) == 1:
            self.ui.textEdit_HDD2.setEnabled(False)
            self.ui.textEdit_HDD2.setText("Диск отсутствует")

    def initThread(self):
        """
        Инициализация потоков
        :return:
        """
        self.sysinfo.start()
        self.sysservices.start()
        self.sysprocs.start()
        # self.sysscheduler.start()

    def initSignals(self):
        """
        Инициализация сигналов
        :return:
        """
        self.ui.comboBox.currentTextChanged.connect(self.onComboBoxChanged)
        self.sysinfo.systemInfoReceived.connect(self.getInfo)
        self.sysservices.SystemServicesReceived.connect(self.getInfoServices)
        self.sysprocs.SystemProcReceived.connect(self.getInfoProcs)
        # self.sysscheduler.SystemSchedulerReceived(self.getInfoSched)

    def onComboBoxChanged(self):
        """
        ComboBox изменяющий delay
        :return:
        """
        self.sysinfo.delay = int(self.ui.comboBox.currentText())

    def getInfoServices(self, value):
        """
        Получение информации о службах
        :param value:
        :return:
        """
        service = value
        row_count = (len(service))
        column_count = 2
        self.ui.table_service.setColumnCount(column_count)
        self.ui.table_service.setColumnWidth(0, 150)
        self.ui.table_service.setHorizontalHeaderItem(0, QTableWidgetItem("serv_name"))
        self.ui.table_service.setHorizontalHeaderItem(1, QTableWidgetItem("Описание"))
        self.ui.table_service.setColumnWidth(1, 350)
        self.ui.table_service.setRowCount(row_count)
        for num, elem in enumerate(service):
            self.ui.table_service.setItem(num, 1, QTableWidgetItem(elem.display_name()))
            self.ui.table_service.setItem(num, 2, QTableWidgetItem(elem.name()))

    def getInfoProcs(self, value):
        """
        Получение информации о процессах
        :param value:
        :return:
        """
        service = value
        row_count = len(service)
        column_count = 3
        self.ui.table_proc.setColumnCount(column_count)
        self.ui.table_proc.setColumnWidth(0, 300)
        self.ui.table_proc.setHorizontalHeaderItem(0, QTableWidgetItem("proc_name"))
        self.ui.table_proc.setColumnWidth(1, 100)
        self.ui.table_proc.setHorizontalHeaderItem(1, QTableWidgetItem("cpu_%"))
        self.ui.table_proc.setColumnWidth(2, 100)
        self.ui.table_proc.setHorizontalHeaderItem(2, QTableWidgetItem("mem_%"))
        self.ui.table_proc.setRowCount(row_count)
        self.ui.table_proc.setSortingEnabled(True)
        for num, proc in enumerate(service):
            self.ui.table_proc.setItem(num, 0, QTableWidgetItem(proc.name()))
            self.ui.table_proc.setItem(num, 1, QTableWidgetItem(str(proc.cpu_percent())))
            self.ui.table_proc.setItem(num, 2, QTableWidgetItem(str(round(proc.memory_percent(), 2))))

    def getInfoSched(self):
        """
        Информация о задачах
        :return:
        """
        service = self.scheduler()
        row_count = len(service)
        column_count = 4
        self.ui.table_sched.setColumnCount(column_count)
        self.ui.table_sched.setRowCount(row_count)
        self.ui.table_sched.setColumnWidth(0, 300)
        self.ui.table_sched.setHorizontalHeaderItem(0, QTableWidgetItem("task_path"))
        self.ui.table_sched.setColumnWidth(1, 100)
        self.ui.table_sched.setHorizontalHeaderItem(1, QTableWidgetItem("task_state"))
        self.ui.table_sched.setColumnWidth(2, 100)
        self.ui.table_sched.setHorizontalHeaderItem(2, QTableWidgetItem("task_lust_runtime"))
        for num, work in enumerate(service):
            # print(num, work[0], work[1], work[2])
            self.ui.table_sched.setItem(num, 0, QTableWidgetItem(work[0]))
            self.ui.table_sched.setItem(num, 1, QTableWidgetItem(str(work[1])))
            self.ui.table_sched.setItem(num, 2, QTableWidgetItem(str(work[2])))

    def scheduler(self):
        """
        Получение информации о задачах
        :return:
        """
        TASK_STATE = {0: 'Unknown',
                      1: 'Disabled',
                      2: 'Queued',
                      3: 'Ready',
                      4: 'Running'}
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        folders = [scheduler.GetFolder('\\')]
        schedulertasks = []
        while folders:
            folder = folders.pop(0)
            folders += list(folder.GetFolders(0))
            for task in folder.GetTasks(0):
                task_path = task.Path
                task_state = TASK_STATE[task.State]
                task_lust_runtime = task.LastRunTime
                schedulertasks.append([task_path, task_state, task_lust_runtime])
        return schedulertasks

    def getInfo(self, value):
        """
        Получение информации о системе
        :param value:
        :return:
        """
        cpu_value = value[0]
        ram_value = value[1]
        self.ui.progressBar_proc.setValue(cpu_value)
        self.ui.progressBar_mem.setValue(ram_value)
        self.ui.textEdit_proc_core_2.setText(str(cpu_value))
        self.ui.textEdit_mem_4.setText(str(ram_value))

    def closeEvent(self, event):
        self.sysinfo.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
