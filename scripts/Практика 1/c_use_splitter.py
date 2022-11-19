"""
Пример работы с QSplitter
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        textEdit_1 = QtWidgets.QTextEdit()
        textEdit_1.append("textEdit_1")

        textEdit_2 = QtWidgets.QTextEdit()
        textEdit_2.append("textEdit_2")

        textEdit_3 = QtWidgets.QTextEdit()
        textEdit_3.append("textEdit_3")

        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(textEdit_1)
        splitter.addWidget(textEdit_2)
        splitter.addWidget(textEdit_3)

        splitter.setCollapsible(0, False)  # Отключение "схлопывания" элементов

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(splitter)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
