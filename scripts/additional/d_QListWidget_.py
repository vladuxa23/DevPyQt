import sys

from PySide2 import QtWidgets


class MyFirstWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.lw = QtWidgets.QListWidget()
        self.lw.itemPressed.connect(self.item_clicked)

        for number, _path in enumerate(['1', '2', '3'], 0):

            item = QtWidgets.QListWidgetItem(_path)

            self.lw.addItem(item)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.lw)

        self.setLayout(main_layout)

    def item_clicked(self, item):
        print(item.data(0))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myWindow = MyFirstWindow()
    myWindow.show()

    sys.exit(app.exec_())
