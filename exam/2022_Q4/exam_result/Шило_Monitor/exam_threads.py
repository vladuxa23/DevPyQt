import time
import psutil
import win32com.client
from PySide6 import QtCore
from PySide6.QtCore import Signal


class SystemInfo(QtCore.QThread):
    """
    Получение информации о системе
    """
    systemInfoReceived = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent()
            ram_value = psutil.virtual_memory().percent
            self.systemInfoReceived.emit([cpu_value, ram_value])
            time.sleep(self.delay)


class SystemServices(QtCore.QThread):
    """
    Получение информации о службах
    """
    SystemServicesReceived = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 30

        while True:
            services = list(psutil.win_service_iter())
            self.SystemServicesReceived.emit(services)
            time.sleep(self.delay)


class SystemProc(QtCore.QThread):
    """
    Получение информации о процессах
    """
    SystemProcReceived = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 5

        while True:
            procs = list(psutil.process_iter())
            self.SystemProcReceived.emit(procs)
            time.sleep(self.delay)


# class SystemScheduler(QtCore.QThread):
#     """
#     Получение информации о задачах в планировщике
#     """
#     SystemSchedulerReceived = Signal(list)
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.delay = None
#
#     def schel(self):
#         TASK_STATE = {0: 'Unknown',
#                       1: 'Disabled',
#                       2: 'Queued',
#                       3: 'Ready',
#                       4: 'Running'}
#         scheduler = win32com.client.Dispatch('Schedule.Service')
#         scheduler.Connect()
#         folders = [scheduler.GetFolder('\\')]
#         schedulertasks = []
#         while folders:
#             folder = folders.pop(0)
#             folders += list(folder.GetFolders(0))
#             for task in folder.GetTasks(0):
#                 task_path = task.Path
#                 task_state = TASK_STATE[task.State]
#                 task_lust_runtime = task.LastRunTime
#                 tusk_result = task.LastTaskResult
#                 schedulertasks.append([task_path, task_state, task_lust_runtime, tusk_result])
#         return schedulertasks
#
#     def run(self) -> None:
#         if self.delay is None:
#             self.delay = 15
#
#         while True:
#             tasks = self.schel()
#             self.SystemSchedulerReceived.emit(tasks)
#             time.sleep(self.delay)
