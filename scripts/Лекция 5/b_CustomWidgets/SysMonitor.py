import time

from PySide2 import QtCore, QtWidgets, QtGui

import psutil


class SystemMonitorGUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SystemMonitorGUI, self).__init__(parent)

        self.initUI()
        self.initThreads()

    def initUI(self):
        self.setFixedSize(1400, 400)

        layout = QtWidgets.QHBoxLayout()

        for _ in range(psutil.cpu_count()):
            layout.addWidget(CPUWidget(self))

        self.setLayout(layout)

    def initThreads(self):
        self.systemMonitor = SystemMonitor()
        self.systemMonitor.start()
        self.systemMonitor.cpuInfo.connect(self.updatePB, QtCore.Qt.QueuedConnection)

    def updatePB(self, cpu_percent_list):
        print(cpu_percent_list)
        layout = self.layout()

        for cpu_count in range(layout.count()):
            widget_link = layout.itemAt(cpu_count).widget()

            widget_link.progressBar.setValue(cpu_percent_list[cpu_count])
            widget_link.cpuLabel.setText(f"CPU №{cpu_count+1} - {cpu_percent_list[cpu_count]}")


class SystemMonitor(QtCore.QThread):
    cpuInfo = QtCore.Signal(list)

    def run(self):
        while True:
            time.sleep(0.5)
            self.cpuInfo.emit(psutil.cpu_percent(percpu=True))


class CPUWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CPUWidget, self).__init__(parent)



        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setRange(0, 100)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )

        self.cpuLabel = QtWidgets.QLabel()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.progressBar)
        layout.addWidget(self.cpuLabel)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = SystemMonitorGUI()
    # win = CPUWidget()
    win.show()

    app.exec_()
