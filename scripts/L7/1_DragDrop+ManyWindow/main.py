import sys
from PySide2 import QtWidgets, QtCore


class ManyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ManyWindow, self).__init__()

        self.other_window = DropWindow()

        pb = QtWidgets.QPushButton("Открыть")
        pb.clicked.connect(self.open_many_window)

        # frame = QtWidgets.QFrame()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(pb)
        # layout.addWidget(frame)

        self.setLayout(layout)

    def open_many_window(self):
        self.other_window.show()
        self.other_window.send_data.connect(lambda x: print(f"Main {x}"))


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
    window = ManyWindow()
    window.show()
    app.exec_()
