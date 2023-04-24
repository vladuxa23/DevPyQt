# import psutil
# import win32com.client
#
# TASK_ENUM_HIDDEN = 1
# TASK_STATE = {0: 'Unknown',
#               1: 'Disabled',
#               2: 'Queued',
#               3: 'Ready',
#               4: 'Running'}
#
# scheduler = win32com.client.Dispatch('Schedule.Service')
# scheduler.Connect()
#
# n = 0
# folders = [scheduler.GetFolder('\\')]
# while folders:
#     folder = folders.pop(0)
#     folders += list(folder.GetFolders(0))
#     tasks = list(folder.GetTasks(TASK_ENUM_HIDDEN))
#     n += len(tasks)
#     # print(list(tasks))
#     for task in tasks:
#         settings = task.Definition.Settings
#         print('Path       : %s' % task.Path)
#         # print('Hidden     : %s' % settings.Hidden)
#         print('State      : %s' % TASK_STATE[task.State])
#         print('Last Run   : %s' % task.LastRunTime)
#         # print('Last Result: %s\n' % task.LastTaskResult)

import win32com.client
#
# TASK_STATE = {0: 'Unknown',
#               1: 'Disabled',
#               2: 'Queued',
#               3: 'Ready',
#               4: 'Running'}
#
# scheduler = win32com.client.Dispatch('Schedule.Service')
# scheduler.Connect()
#
# folders = [scheduler.GetFolder('\\')]
# schedulertasks = []
# while folders:
#     folder = folders.pop(0)
#     folders += list(folder.GetFolders(0))
#     for task in folder.GetTasks(0):
#         task_path = task.Path
#         task_state = TASK_STATE[task.State]
#         task_lust_runtime = task.LastRunTime
#         tusk_result = task.LastTaskResult
#         schedulertasks.append([task_path, task_state, task_lust_runtime, tusk_result])
# print(schedulertasks)
# print(schedulertasks[1][2])


def Scheduler():
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
            tusk_result = task.LastTaskResult
            schedulertasks.append([task_path, task_state, task_lust_runtime, tusk_result])
    return schedulertasks

if __name__ == "__main__":
    # print(Scheduler())
    sch = Scheduler()
    print(sch)