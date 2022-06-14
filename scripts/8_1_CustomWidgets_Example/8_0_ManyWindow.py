import sys
from PySide2 import QtWidgets
from DropFile import DropWindow


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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ManyWindow()
    window.show()
    app.exec_()
