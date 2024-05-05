from PySide6 import QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Widget()
    window.show()

    app.exec()
