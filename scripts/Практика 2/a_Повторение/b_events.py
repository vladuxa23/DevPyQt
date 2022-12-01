"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль и в plainTextEdit,
размещённый на виджете, при выводе события указывать время, когда оно произошло
"""

from PySide6 import QtWidgets
from time import ctime
from b_form import Ui_MainWindow


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def event(self, event) -> bool:
        self.ui.plainTextEdit.setPlainText(str(event)+"\n")
        print(event)
        return super().event(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
