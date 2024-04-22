"""
Простейшее использование QProcess
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.process = None

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.pushButton = QtWidgets.QPushButton("Показать список файлов")

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(self.executeOtherProcess)

    def executeOtherProcess(self) -> None:
        """
        Запуск выполнения другого процесса

        :return: None
        """

        if self.process is None:
            self.plainTextEdit.appendPlainText("Запуск другого процесса")
            self.process = QtCore.QProcess()
            self.process.start("python", ['c_other_py_script.py'])
            self.process.finished.connect(self.processFinished)

    def processFinished(self) -> None:
        """
        Действие при завершении другого процесса

        :return: None
        """

        self.plainTextEdit.appendPlainText("Другой процесс завершен")
        self.process = None


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
