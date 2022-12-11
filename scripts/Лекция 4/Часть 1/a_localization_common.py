"""
Демонстрация локализации стандартных элементов Qt
"""

import os.path
from pathlib import Path

from PySide6 import QtCore, QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.initTranslation()

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.pushButtonQuestion = QtWidgets.QPushButton("Выполнить действие")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButtonQuestion)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonQuestion.clicked.connect(
            lambda: QtWidgets.QMessageBox.question(self, "Вопрос", "Окно на русском")
        )

    def initTranslation(self) -> None:
        """
        Инициализация локализации

        :return: None
        """

        # Получение корневого каталога
        root_dir = Path(__file__).parent.parent.parent.parent
        # Получение каталога, где находятся стандартные переводы
        qt_translation_folder = os.path.join(root_dir, "venv", "Lib", "site-packages", "PySide6", "translations")
        # Инициализируем класс QTranslator
        translator = QtCore.QTranslator(self)
        # Загружаем файл qm для перевода стандартных элементов
        translator.load(os.path.join(qt_translation_folder, "qtbase_ru.qm"))
        # Устанавливаем локализацию окна
        QtCore.QCoreApplication.instance().installTranslator(translator)

    def closeEvent(self, event):
        """Функция-обработчик события закрытия окна"""

        reply = QtWidgets.QMessageBox.question(
            self,
            "Выход",
            "Закрыть приложение?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
            QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()
    myapp.show()

    app.exec()
