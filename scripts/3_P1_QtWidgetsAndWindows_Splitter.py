import sys
from PySide2 import QtWidgets, QtCore, QtGui


class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.initUi()

    def initUi(self):

        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)

        self.textEdit_1 = QtWidgets.QTextEdit()
        self.textEdit_1.append("textEdit_1")

        textEdit_2 = QtWidgets.QTextEdit()
        textEdit_2.append("textEdit_2")

        textEdit_3 = QtWidgets.QTextEdit()
        textEdit_3.append("textEdit_3")

        splitter.addWidget(self.textEdit_1)
        splitter.addWidget(textEdit_2)
        splitter.addWidget(textEdit_3)

        self.setCentralWidget(splitter)

        self.textEdit_1.installEventFilter(self)

    def eventFilter(self, watched:QtCore.QObject, event:QtCore.QEvent) -> bool:
        if watched == self.textEdit_1 and event.type() == QtCore.QEvent.Resize:
            print(self.textEdit_1.size().height())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = MainTestWindow()
    windows.show()
    app.exec_()