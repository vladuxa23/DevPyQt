"""
Создание окна на основе QMainWindow
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
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

        # Настройка компоновки окна
        layout = QtWidgets.QHBoxLayout()

        self.abc = QtWidgets.QPushButton("abc")
        # Настройка "растяжения" кнопки
        self.abc.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        layout.addWidget(QtWidgets.QLabel("Надпись"))
        layout.addWidget(self.abc)

        # Центральный виджет особенность QMainWindow
        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec_()
