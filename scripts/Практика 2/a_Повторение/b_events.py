"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль и в plainTextEdit,
размещённый на виджете, при выводе события указывать время, когда оно произошло
"""
import time

import PySide6
from PySide6 import QtWidgets, QtCore
from time import ctime
from b_form import Ui_MainWindow


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.initUi()

    # def initUi(self) -> None:
    #     self.plainTextEdit = QtWidgets.QPlainTextEdit()
    #
    #     layout = QtWidgets.QHBoxLayout()
    #     layout.addWidget(self.plainTextEdit)
    #
    #     self.setLayout(layout)

    def event(self, event: QtCore.QEvent) -> bool:
        a = f"{time.ctime()}: {event}"
        print(a)
        # self.plainTextEdit.appendPlainText(a + "\n")

        return super(Window, self).event(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
