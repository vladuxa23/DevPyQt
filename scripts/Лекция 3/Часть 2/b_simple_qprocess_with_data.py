"""
Простейшее использование QProcess с получением данных
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
            self.plainTextEdit.appendPlainText("Выполнение процесса")
            self.process = QtCore.QProcess()
            self.process.readyReadStandardOutput.connect(self.handleOutput)
            self.process.readyReadStandardError.connect(self.handleError)
            self.process.stateChanged.connect(self.handleStateChange)
            self.process.finished.connect(self.processFinished)
            # self.process.start("python", ["c_other_py_script.py"])  # запуск py скрипта в отдельном потоке
            self.process.start("ping", ["8.8.8.8"])  # запуск команды ping в отдельном потоке

    def handleError(self) -> None:
        """
        Обработка данных из потока stderr

        :return: None
        """

        data = self.process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.plainTextEdit.appendPlainText(stderr)

    def handleOutput(self) -> None:
        """
        Обработка данных из потока stdout

        :return: None
        """

        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.plainTextEdit.appendPlainText(stdout)

    def handleStateChange(self, state) -> None:
        """
        Изменение статуса потока

        :param state: статус
        :return: None
        """

        states = {
            QtCore.QProcess.NotRunning: 'Not running',
            QtCore.QProcess.Starting: 'Starting',
            QtCore.QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.plainTextEdit.appendPlainText(f"Состояние изменено: {state_name}")

    def processFinished(self) -> None:
        """
        Обработка завершения потока

        :return: None
        """

        self.plainTextEdit.appendPlainText("Процесс завершен")
        self.process = None


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
