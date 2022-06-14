import time

from PySide2 import QtWidgets, QtCore, QtGui
from circular_push_button_design import Ui_CircularPB


class MyPB(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MyPB, self).__init__(parent)

        self.threadCounter = ThreadCounter()
        self.threadCounter.count_value.connect(self.update_pb_value, QtCore.Qt.QueuedConnection)
        self.threadStatus = False

        layout = QtWidgets.QVBoxLayout()
        self.pb = CircularPB()
        layout.addWidget(self.pb)

        self.setLayout(layout)

        self.pb.ui.labelTitle.installEventFilter(self)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:

        if watched.objectName() == 'labelTitle' and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.startWorking()

        return super(MyPB, self).eventFilter(watched, event)

    def startWorking(self):
        if not self.threadStatus:
            self.threadCounter.start()
            self.threadStatus = True
        else:
            self.pb.setProgressBarValue(0)
            self.threadCounter.status = False
            self.threadStatus = False

    @QtCore.Slot()
    def update_pb_value(self, count):
        self.pb.setProgressBarValue(count)


class ThreadCounter(QtCore.QThread):
    count_value = QtCore.Signal(int)

    def run(self):

        self.status = True
        count = 0

        while self.status:
            count += 1
            self.count_value.emit(count)
            time.sleep(0.01)
            if count == 360:
                count = 0


class CircularPB(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CircularPB, self).__init__(parent)
        self.ui = Ui_CircularPB()
        self.ui.setupUi(self)

        # ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

        # ==> APPLY DROP SHADOW EFFECT
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(4)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

    def setProgressBarValue(self, value):
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
            border-radius: 61px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:-{ANGLE}, stop:1 rgba(255, 0, 127, 0), stop:0 rgba(85, 170, 255, 255));
        }
        """

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{ANGLE}", str(270+value))

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = MyPB()
    win.show()
    app.exec_()
