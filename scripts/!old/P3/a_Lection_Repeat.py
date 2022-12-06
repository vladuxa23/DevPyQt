# Группа 2021-2
# import time
#
# from PySide2 import QtCore, QtWidgets
#
# class MyTimer(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(MyTimer, self).__init__(parent)
#
#         self.initUi()
#
#         self.timerTread = MyTimerThread()
#         self.timerTread.timer_signal.connect(self.setTimerCount)
#
#         self.timerTread.started.connect(lambda: self.lineEditTimer.setEnabled(False))
#         self.timerTread.finished.connect(self.timerFinished)
#
#     def initUi(self):
#         self.lineEditTimer = QtWidgets.QLineEdit()
#         self.lineEditTimer.setPlaceholderText("Введите количество секунд")
#
#         self.pbStartTimer = QtWidgets.QPushButton()
#         self.pbStartTimer.setText("Старт")
#         self.pbStartTimer.clicked.connect(self.onPBStartTimerClicked)
#
#         mainLayout = QtWidgets.QVBoxLayout()
#
#         mainLayout.addWidget(self.lineEditTimer)
#         mainLayout.addWidget(self.pbStartTimer)
#
#         self.setLayout(mainLayout)
#
#     def onPBStartTimerClicked(self):
#         self.timerTread.setCounter(int(self.lineEditTimer.text()))
#         self.timerTread.start()
#
#     def setTimerCount(self, count):
#         self.lineEditTimer.setText(count)
#
#     def timerFinished(self):
#         self.lineEditTimer.setEnabled(True)
#         self.lineEditTimer.setText("")
#
#
# class MyTimerThread(QtCore.QThread):
#     timer_signal = QtCore.Signal(str)
#
#     def __init__(self, parent=None):
#         super(MyTimerThread, self).__init__(parent)
#
#         self.time_count = 0
#
#     def setCounter(self, time_count):
#         self.time_count = time_count
#
#     def run(self):
#         for i in range(self.time_count, 0, -1):
#             self.timer_signal.emit(str(i))
#             time.sleep(1)


# Группа 2021-1
import time
from PySide2 import QtWidgets, QtCore


class MyApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # init treads
        self.initThreads()

        # init ui
        self.initUi()

    def initUi(self):
        """
        Метод инициализации пользовательского интерфейса
        """

        # init QLineEdit
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Введите количество секунд")

        # init QPushButton START
        self.pbStart = QtWidgets.QPushButton()
        self.pbStart.setText("Старт")

        # init QPushButton STOP
        self.pbStop = QtWidgets.QPushButton()
        self.pbStop.setText("Стоп")
        self.pbStop.setEnabled(False)

        # init main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.lineEdit)
        main_layout.addWidget(self.pbStart)
        main_layout.addWidget(self.pbStop)

        # set main layout on main widget
        self.setLayout(main_layout)

        # init signals
        self.pbStart.clicked.connect(self.onPBStartClicked)
        self.pbStop.clicked.connect(self.onPBStopClicked)

    def initThreads(self):
        """
        Метод инициализации потоков
        """

        # create QThread instance
        self.timerThread = TimerThread()

        # init signals
        self.timerThread.started.connect(self.timerThreadStarted)  # выполняется, когда метод run запущен
        self.timerThread.finished.connect(self.timerThreadFinished)  # выполняется, когда метод run закончен

        self.timerThread.timerSignal.connect(self.timerSignalEmit)  # выполняется, когда вызывавется метод emit у
        # сигнала timerSignal в потоке self.timerThread

    def onPBStartClicked(self):
        """
        Метод-слот для отработки сигнала clicked виджета self.pbStart

        Запускает поток, в котором будет выполняться бэкенд
        """

        try:
            self.timerThread.timerCount = int(self.lineEdit.text())  # установка числа относительно которого начнётся отсчёт
            self.timerThread.start()  # запуск потока
        except ValueError:  # обработка сценария, если пользователь введёт не число
            self.lineEdit.setText("")
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введено неправильное значение")

    def onPBStopClicked(self):
        """
        Метод-слот для отработки сигнала clicked виджета self.pbStop
        """

        self.timerThread.status = False

    def timerThreadStarted(self):
        """
        Метод-слот для отработки сигнала started потока self.timerThread
        """

        self.pbStart.setEnabled(False)
        self.pbStop.setEnabled(True)
        self.lineEdit.setEnabled(False)

    def timerThreadFinished(self):
        """
        Метод-слот для отработки сигнала finished потока self.timerThread
        """

        self.pbStart.setEnabled(True)
        self.pbStop.setEnabled(False)
        self.lineEdit.setEnabled(True)

        self.lineEdit.setText("")

    def timerSignalEmit(self, emit_value):
        """
        Метод-слот для отработки сигнала timerSignal потока self.timerThread

        Будет срабатывать, когда в потоке у сигнала self.timerSignal, будет вызываться метод emit()
        П-р: self.timerSignal.emit(str(self.timerCount))
        """

        self.lineEdit.setText(emit_value)


class TimerThread(QtCore.QThread):
    timerSignal = QtCore.Signal(str)  # создаём кастомный сигнал для потока

    def __init__(self, parent=None):
        super(TimerThread, self).__init__(parent)

        self.timerCount = None  # атрибут, который будет содержать количество оставшихся секунд
        self.status = True  # атрибут, который является флагом, для остановки потока

    def run(self):
        self.status = True
        while self.status:
            time.sleep(1)
            self.timerCount -= 1
            self.timerSignal.emit(str(self.timerCount))  # отправка данных из потока


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyApp()
    win.show()

    app.exec_()




