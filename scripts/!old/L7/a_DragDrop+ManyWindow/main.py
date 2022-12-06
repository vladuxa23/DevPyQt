import sys
from PySide2 import QtWidgets, QtCore, QtGui
import ast


class ManyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initWindows()

    def initUi(self):
        self.setFixedSize(300, 100)

        pb = QtWidgets.QPushButton("Открыть")
        pb.clicked.connect(self.open_child_window)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(pb)

        self.setLayout(layout)

    def initWindows(self):
        self.child_window = DroppedWindow()
        self.child_window.send_data.connect(lambda x: print(f"Main {x}"))

    def open_child_window(self):
        self.child_window.show()


class DroppedWindow(QtWidgets.QWidget):
    send_data = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.setAcceptDrops(True)  # устанавливаем возможность делать Drop на виджет
        self.setFixedSize(300, 300)

        self.send_data.connect(lambda x: print(x))  # перехватываем сигнал внутри приложения

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()  # разрешаем перетаскивание, если url

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            file_name = url.toLocalFile()
            self.send_data.emit("Dropped file: " + file_name)

    def paintEvent(self, event:QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        painter.drawText(
            QtCore.QPoint(
                self.width() - self.width()/2 - 40,
                self.height() - self.height()/2
            ),
            "Перетащите сюда")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ManyWindow()
    window.show()
    app.exec_()
