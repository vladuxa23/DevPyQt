import sys

from PySide6 import QtWidgets, QtGui

from ui import my_res


# https://doc.qt.io/qtforpython/tutorials/basictutorial/qrcfiles.html

class MyStyle(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        my_res.qInitResources()

        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/ico/action.ico")))

        label = QtWidgets.QLabel()
        label.setPixmap(QtGui.QPixmap(":/img/img/1.jpg"))

        pushButton = QtWidgets.QPushButton()
        pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/ico/axialis-iconworkshop.ico")))

        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addWidget(label)
        v_layout.addWidget(pushButton)

        self.setLayout(v_layout)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        layout = self.layout()
        label = layout.itemAt(0).widget()

        w = label.width()
        h = label.height()
        p = QtGui.QPixmap(":/img/img/1.jpg")

        label.setPixmap(p.scaled(w, h))
        self.repaint()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    windows = MyStyle()
    windows.show()

    app.exec()
