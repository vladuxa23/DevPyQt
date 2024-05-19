from PySide6 import QtWidgets, QtGui
from static import res


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        res.qInitResources()

        pushButton = QtWidgets.QPushButton()
        icon = QtGui.QIcon(":/ico/ico/icons8-джейк-16.png")
        pushButton.setIcon(icon)

        label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(":/gif/gif/load_2.gif")
        label.setPixmap(pixmap)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(pushButton)
        layout.addWidget(label)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
