import psutil

import cpuinfo

import pythoncom

import win32com.client

import time

from time import sleep

from PySide6 import QtCore

from re import search


class SystemInfo(QtCore.QThread):
    """
    поток для получения системной информации

    """
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, timeout=1, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.status = True

    def run(self) -> None:

        self.status = True
        # sys_info = []

        while self.status:
            sys_info = []
            sys_info.append(f"Название процессора: {cpuinfo.get_cpu_info()['brand_raw']}")
            sys_info.append(f"Количество ядер: {psutil.cpu_count()}")
            sys_info.append(f"Текущая загрузка: {psutil.cpu_percent()}")
            sys_info.append(f"Оперативная память: {psutil.virtual_memory().total//1024**2}")
            sys_info.append(f"Текущая загрузка оперативной памяти: {psutil.virtual_memory().used//1024**2}")


            self.systemInfoReceived.emit(sys_info)

            time.sleep(self.timeout)

class DisksInfo(QtCore.QThread):
    disksInfoReceived = QtCore.Signal(list)

    def __init__(self, timeout=1, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.status = True

    def run(self) -> None:

        self.status = True
        disks_info = []
        for disk in psutil.disk_partitions(all=False):
            disks_info.append((disk.device,
                              round(psutil.disk_usage(disk.device).total / 1024 ** 3, 2),
                              round(psutil.disk_usage(disk.device).used / 1024 ** 3, 2)))

        self.disksInfoReceived.emit(disks_info)



class ProcInfoThread(QtCore.QThread):
    """
    Поток для получения информации об активных процессах

    """
    procInfoReceived = QtCore.Signal(list)

    def __init__(self, timeout=1, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.status = True

    def run(self):
        self.status = True

        while self.status:
            proc_info = []
            for proc in psutil.process_iter():
                if proc.is_running():
                    with proc.oneshot():
                        proc_info.append([
                            proc.ppid(), proc.name(),
                            proc.cpu_percent(),
                            round(proc.memory_percent(), 3),
                            proc.status()
                        ])

            self.procInfoReceived.emit(proc_info)
            time.sleep(self.timeout)

class ServInfoThread(QtCore.QThread):

    """
    поток для получения информации о службах
    """

    servInfoReceived = QtCore.Signal(list)

    def __init__(self, timeout=1, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.status = True

    def run(self) -> None:

        self.status = True

        while self.status:
            serv_info = []
            for win in psutil.win_service_iter():
                if win.status() == "running":
                    info = psutil.win_service_get(win.name()).as_dict()
                    service = [info["name"], info["pid"], info["description"], info["start_type"], info["binpath"]]
                    serv_info.append(service)
            self.servInfoReceived.emit(serv_info)
            time.sleep(self.timeout)


class TaskSchedulerInfo(QtCore.QThread):
    taskSchedulerInfoReceived = QtCore.Signal(list)
    TASK_STATE = {0: 'Unknown',
                  1: 'Disabled',
                  2: 'Queued',
                  3: 'Ready',
                  4: 'Running'}

    def __init__(self, timeout=100, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.status = None

    def run(self):
        self.status = True

        while self.status:
            pythoncom.CoInitialize()
            taskSchedulerInfo = []
            scheduler = win32com.client.Dispatch('Schedule.Service')
            scheduler.Connect()
            folders = [scheduler.GetFolder('\\')]
            while folders:
                folder = folders.pop(0)
                folders += list(folder.GetFolders(0))
                for task in folder.GetTasks(0):
                    task_path = task.Path
                    task_state = TaskSchedulerInfo.TASK_STATE[task.State]
                    task_schedule = str(task.NextRunTime)
                    taskSchedulerInfo.append([task_path, task_state, task_schedule])
            self.taskSchedulerInfoReceived.emit(taskSchedulerInfo)
            sleep(self.timeout)


