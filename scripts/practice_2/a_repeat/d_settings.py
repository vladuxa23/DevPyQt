"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtCore


class QPlainTextEditWithSaveData(QtWidgets.QPlainTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__loadSettings()

    def closeEvent(self, event):

        self.__saveSettings()

        return super().closeEvent(event)

    def __loadSettings(self):
        settings = QtCore.QSettings("SimpleTextEditApp")
        self.setPlainText(settings.value("text", ""))

    def __saveSettings(self):
        settings = QtCore.QSettings("SimpleTextEditApp")
        settings.setValue("text", self.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = QPlainTextEditWithSaveData()
    window.show()

    app.exec()

