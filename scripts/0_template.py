from PySide6 import QtWidgets, QtCore


class Task(QtWidgets.QWidget):
    def __init__(self):
        super().__init__(None)
        self.label_1 = QtWidgets.QLabel("Hello")
        self.label_2 = QtWidgets.QLabel("Hello 2")
        self.label_3 = QtWidgets.QLabel("Hello 3")

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.label_1)
        l.addWidget(self.label_2)
        l.addWidget(self.label_3)

        self.setLayout(l)

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.listWidget = QtWidgets.QListWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.listWidget)

        self.setLayout(layout)

        self.addWidget(Task())
        self.addWidget(Task())
        self.addWidget(Task())
        self.addWidget(Task())
        self.addWidget(Task())
        self.addWidget(Task())

    def addWidget(self, widget) -> None:

        new_item = QtWidgets.QListWidgetItem()
        widget_size = widget.sizeHint()
        new_item.setSizeHint(QtCore.QSize(widget_size.width(), widget_size.height()))
        self.listWidget.addItem(new_item)
        self.listWidget.setItemWidget(new_item, widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
