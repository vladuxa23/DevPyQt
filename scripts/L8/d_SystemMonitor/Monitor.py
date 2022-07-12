import sys
import time
import psutil
from PySide2 import QtCore, QtGui, QtWidgets

from ui.circular_pb import Ui_CircularPB


class SystemMonitorGUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SystemMonitorGUI, self).__init__(parent)

        self.initUi()
        self.initThreads()

    def initThreads(self):
        self.systemInfo = SystemMonitor()
        self.systemInfo.start()
        self.systemInfo.cpuInfo.connect(self.updatePB, QtCore.Qt.QueuedConnection)

    def initUi(self):
        self.resize(1000, 200)

        self.layout = QtWidgets.QHBoxLayout()
        for cpu in range(psutil.cpu_count()):
            self.layout.addWidget(CircularPB())

        self.setLayout(self.layout)

        self.setStyleSheet("background-color: #282a36")

    def updatePB(self, cpu_percent_list):
        print(cpu_percent_list)
        for cpu_count in range(self.layout.count()):
            self.layout.itemAt(cpu_count).widget().setProgressBarValue(cpu_count+1, cpu_percent_list[cpu_count])


class SystemMonitor(QtCore.QThread):
    cpuInfo = QtCore.Signal(list)

    def run(self):
        while True:
            time.sleep(1)
            self.cpuInfo.emit(psutil.cpu_percent(percpu=True))


class CircularPB(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CircularPB, self).__init__(parent)
        self.ui = Ui_CircularPB()
        self.ui.setupUi(self)

        # self.setProgressBarValue(value)

        # ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

        # ==> APPLY DROP SHADOW EFFECT
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

    def setProgressBarValue(self, cpu, value):
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
            border-radius: 78px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        cpu_percent = f"""<p><span style=" font-size:24pt;">{value}</span><span style=" font-size:24pt; vertical-align:super;">%</span></p>"""
        self.ui.labelPercentage.setText(cpu_percent)

        cpu_number = f"""<html><head/><body><p><span style=" font-weight:600; color:#9b9bff;">CPU</span> # {cpu}</p></body></html>"""
        self.ui.labelTitle.setText(cpu_number)
        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SystemMonitorGUI()
    # window = CircularPB()
    window.show()
    sys.exit(app.exec_())
