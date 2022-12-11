"""
Демонстрация перевода пользовательского текста в приложении
"""

import os
from pathlib import Path

from PySide6 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.initUi()
        self.initTranslators()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setWindowTitle("Переводчик")
        self.setFixedSize(400, 300)

        self.button_ru = QtWidgets.QPushButton("RU")
        self.button_en = QtWidgets.QPushButton("EN")
        self.button_input = QtWidgets.QPushButton("Ввод")

        self.line_edit_name = QtWidgets.QLineEdit()
        self.line_edit_surname = QtWidgets.QLineEdit()

        self.labelName = QtWidgets.QLabel("Имя")
        self.labelName.setMinimumWidth(60)
        self.labelSurname = QtWidgets.QLabel("Фамилия")
        self.labelSurname.setMinimumWidth(60)

        layout_v = QtWidgets.QVBoxLayout()
        layout_h1 = QtWidgets.QHBoxLayout()
        layout_h2 = QtWidgets.QHBoxLayout()
        layout_h3 = QtWidgets.QHBoxLayout()
        layout_h4 = QtWidgets.QHBoxLayout()

        layout_h1.addWidget(self.labelName)
        layout_h1.addWidget(self.line_edit_name)

        layout_h2.addWidget(self.labelSurname)
        layout_h2.addWidget(self.line_edit_surname)

        layout_h3.addWidget(self.button_input)

        layout_h4.addWidget(self.button_ru)
        layout_h4.addWidget(self.button_en)

        layout_v.addLayout(layout_h1)
        layout_v.addLayout(layout_h2)
        layout_v.addLayout(layout_h3)
        layout_v.addLayout(layout_h4)
        layout_v.addItem(QtWidgets.QSpacerItem(
            1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        )
        self.setLayout(layout_v)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.button_ru.clicked.connect(self.setLocalization)
        self.button_en.clicked.connect(self.setLocalization)

    def initTranslators(self) -> None:
        """
        Инициализация переводчиков

        :return: None
        """

        self.translator = QtCore.QTranslator(self)
        self.translatorApp = QtCore.QTranslator(self)

        self.setLocalization()

    def changeEvent(self, event: QtCore.QEvent) -> None:
        """
        Отслеживание изменения состояния окна

        :param event: QtCore.QEvent
        :return: None
        """

        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi()
        super().changeEvent(event)

    def setLocalization(self) -> None:
        """
        Установка локализации

        :return: None
        """

        sender = self.sender()
        if sender is None:
            lang = "ru"
        else:
            lang = sender.text().lower()

        root_dir = Path(__file__).parent.parent.parent.parent
        qt_translation_folder = os.path.join(root_dir, "venv", "Lib", "site-packages", "PySide6", "translations")

        if lang == "ru":
            QtCore.QCoreApplication.removeTranslator(self.translator)

            self.translatorApp.load(os.path.join(qt_translation_folder, f"qtbase_ru.qm"))

        elif lang == "en":
            self.translator.load(os.path.join(os.getcwd(), "translations", f"to_en.qm"))
            QtCore.QCoreApplication.installTranslator(self.translator)

            self.translatorApp.load(os.path.join(qt_translation_folder, f"qtbase_en.qm"))

        QtCore.QCoreApplication.installTranslator(self.translatorApp)

    def retranslateUi(self) -> None:
        """
        Обновление фраз для перевода

        :return: None
        """

        self.setWindowTitle(QtCore.QCoreApplication.translate("MyTranslateApp", "Переводчик"))
        self.labelName.setText(QtCore.QCoreApplication.translate("MyTranslateApp", "Имя"))
        self.labelSurname.setText(QtCore.QCoreApplication.translate("MyTranslateApp", "Фамилия"))
        self.button_input.setText(QtCore.QCoreApplication.translate("MyTranslateApp", "Ввод"))

        self.exit_question_title = QtCore.QCoreApplication.translate("MyTranslateApp", "Выход")
        self.exit_question_body = QtCore.QCoreApplication.translate(
            "MyTranslateApp", "Вы действительно хотите закрыть программу?"
        )

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Действия при закрытии окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        reply = QtWidgets.QMessageBox.question(
            self,
            self.exit_question_title,
            self.exit_question_body,
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
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