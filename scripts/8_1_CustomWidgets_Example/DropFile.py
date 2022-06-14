import sys
from PySide2 import QtCore, QtWidgets


class DropWindow(QtWidgets.QWidget):
    send_data = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(DropWindow, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setMinimumSize(150, 150)

        self.send_data.connect(lambda x: print(x))

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        print(e.mimeData().urls())
        for url in e.mimeData().urls():
            file_name = url.toLocalFile()
            self.send_data.emit("Dropped file: " + file_name)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DropWindow()
    window.show()
    app.exec_()
