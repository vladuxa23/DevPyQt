import sys
from PySide2 import QtWidgets, QtGui


class MyWidgets(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        # menuBar отсутствует у QWidgets
        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction("Open")

        # toolBar отсутствует у QWidgets
        self.toolBarFirst = self.addToolBar("First")
        self.toolBarFirst.addAction("Edit_1")

        self.toolBarSec = self.addToolBar("Second")
        self.toolBarSec.addAction("Edit_2")
        self.toolBarSec.addAction("Edit_3")

        # statusBar отсутствует у QWidgets
        self.appStatusBar = self.statusBar()
        self.appStatusBar.showMessage("Status: Ok!")

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        layout = QtWidgets.QHBoxLayout()
        self.abc = QtWidgets.QPushButton("abc")
        self.abc.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        layout.addWidget(self.abc)

        centralWidget.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
