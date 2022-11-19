from PySide2 import QtCore, QtWidgets, QtGui


class MyEventHandler(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QtWidgets.QVBoxLayout()

        self.button1 = QtWidgets.QPushButton("1")
        self.button2 = QtWidgets.QPushButton("2")
        self.le = QtWidgets.QLineEdit()

        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.button2)
        main_layout.addWidget(self.le)

        self.setLayout(main_layout)

        self.button1.installEventFilter(self)
        self.button2.installEventFilter(self)
        self.le.installEventFilter(self)

    # def closeEvent(self, event):
    #
    #     reply = QtWidgets.QMessageBox.question(self, "Закрыть окно?",
    #                                            "Вы действительно хотите закрыть окно?",
    #                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
    #                                            QtWidgets.QMessageBox.No)
    #     if reply == QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()
    #
    # def wheelEvent(self, event:QtGui.QWheelEvent) -> None:
    #     print(event.angleDelta())

    # def event(self, event: QtCore.QEvent) -> bool:
    #     print(event.type())
    #
    #     if event.type() == QtCore.QEvent.Type.Wheel:
    #         print(event.angleDelta())
    #
    #     if event.type() == QtCore.QEvent.Close:
    #         event.setAccepted(False)
    #
    #     if event.type() == QtCore.QEvent.Resize:
    #         print(f"Ширина: {event.size().width()}")
    #         print(f"Старая ширина: {event.oldSize().width()}")
    #         print(f"Высота: {self.size().height()}")
    #
    #     return QtWidgets.QWidget.event(self, event)

    # def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
    #     print(event.count())
    #
    # def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
    #     print(event.type())

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:

        # print(watched)

        if watched == self.button2 and event.type() == QtCore.QEvent.KeyPress:
            print(f"key {event.text()} pressed")
        if watched == self.button2 and event.type() == QtCore.QEvent.MouseButtonPress:
            print("mouse pressed")
        if ((watched == self.button2) or (watched == self.button1)) and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("mouse dbl pressed")
            self.hello(watched)

        return super(MyEventHandler, self).eventFilter(watched, event)

    def hello(self, watched):

        self.le.setText(f"Hello {watched.text()}")




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyEventHandler()
    myapp.show()
    app.exec_()
