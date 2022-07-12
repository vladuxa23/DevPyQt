from PySide2 import QtWidgets


class ManySignalsOneSlot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.setFixedSize(200, 200)

        layout = QtWidgets.QVBoxLayout()

        self.button1 = QtWidgets.QPushButton("1", self)
        self.button2 = QtWidgets.QPushButton("2", self)

        self.button1.clicked.connect(self.print_button_text)
        self.button2.clicked.connect(self.print_button_text)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def print_button_text(self):
        widget_link = self.sender()
        print(widget_link.text())



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = ManySignalsOneSlot()
    myapp.show()

    app.exec_()
