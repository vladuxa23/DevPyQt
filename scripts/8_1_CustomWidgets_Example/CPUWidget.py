from PySide2 import QtCore, QtWidgets, QtGui


class CPUWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CPUWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()

        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setRange(0, 100)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.cpuLabel = QtWidgets.QLabel()

        layout.addWidget(self.progressBar)
        layout.addWidget(self.cpuLabel)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = CPUWidget()
    win.show()
    app.exec_()
