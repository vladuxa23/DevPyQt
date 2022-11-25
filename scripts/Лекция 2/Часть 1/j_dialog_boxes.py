"""
Использование диалоговых окон
"""

import time

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        dialog_boxes = [
            "QtWidgets.QMessageBox.about",
            "QtWidgets.QMessageBox.question",
            "QtWidgets.QMessageBox.warning",
            "QtWidgets.QMessageBox.critical",
            "QtWidgets.QMessageBox.aboutQt",
            "------------",
            "QtWidgets.QInputDialog.getText",
            "QtWidgets.QInputDialog.getInt",
            "QtWidgets.QInputDialog.getDouble",
            "QtWidgets.QInputDialog.getItem",
            "QtWidgets.QInputDialog.getMultiLineText",
            "------------",
            "QtWidgets.QFileDialog.getExistingDirectory",
            "QtWidgets.QFileDialog.getExistingDirectoryUrl",
            "QtWidgets.QFileDialog.getOpenFileUrl",
            "QtWidgets.QFileDialog.getOpenFileUrls",
            "QtWidgets.QFileDialog.getOpenFileName",
            "QtWidgets.QFileDialog.getOpenFileNames",
            "QtWidgets.QFileDialog.getSaveFileName",
            "QtWidgets.QFileDialog.getSaveFileUrl",
            "------------",
            "QtWidgets.QColorDialog.getColor",
            "QtWidgets.QFontDialog.getFont",
            "QtWidgets.QProgressDialog",
        ]

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(dialog_boxes)

        self.pushButton = QtWidgets.QPushButton("Вызов окна")

        self.plainTextEdit = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.comboBox)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.plainTextEdit)
        self.setLayout(layout)

        self.errorMsg = QtWidgets.QErrorMessage(self)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(self.show_dialog_window)

    def show_dialog_window(self) -> None:
        """
        Показ выбранного диалогового окна

        :return: None
        """

        selected_dialog_window = self.comboBox.currentText()
        if selected_dialog_window == "------------":
            return None

        if selected_dialog_window == "QtWidgets.QMessageBox.about":
            self.show_message_about()
        elif selected_dialog_window == "QtWidgets.QMessageBox.question":
            self.show_message_question()
        elif selected_dialog_window == "QtWidgets.QMessageBox.warning":
            self.show_message_warning()
        elif selected_dialog_window == "QtWidgets.QMessageBox.critical":
            self.show_message_critical()
        elif selected_dialog_window == "QtWidgets.QMessageBox.aboutQt":
            self.show_message_aboutQt()
        elif selected_dialog_window == "QtWidgets.QInputDialog.getText":
            self.show_input_text()
        elif selected_dialog_window == "QtWidgets.QInputDialog.getInt":
            self.show_input_int()
        elif selected_dialog_window == "QtWidgets.QInputDialog.getDouble":
            self.show_input_double()
        elif selected_dialog_window == "QtWidgets.QInputDialog.getItem":
            self.show_input_item()
        elif selected_dialog_window == "QtWidgets.QInputDialog.getMultiLineText":
            self.show_input_multiline()
        elif selected_dialog_window == "QtWidgets.QFileDialog.getExistingDirectory":
            self.show_file_directory()
        elif selected_dialog_window == "QtWidgets.QFileDialog.getExistingDirectoryUrl":
            self.show_file_directory_url()
        elif selected_dialog_window == "QtWidgets.QFileDialog.getOpenFileUrl":
            self.show_file_file_url()
        elif selected_dialog_window == "QtWidgets.QFileDialog.getOpenFileUrls":
            self.show_file_file_urls()
        elif selected_dialog_window == "QtWidgets.QFileDialog.getOpenFileName":
            self.show_file_file_name()
        elif selected_dialog_window == "QtWidgets.QFileDialog.getOpenFileNames":
            self.show_file_file_names()
        elif selected_dialog_window == "QtWidgets.QFileDialog.getSaveFileName":
            self.show_file_save_name()
        elif selected_dialog_window == "QtWidgets.QFileDialog.getSaveFileUrl":
            self.show_file_save_url()
        elif selected_dialog_window == "QtWidgets.QColorDialog.getColor":
            self.show_color()
        elif selected_dialog_window == "QtWidgets.QFontDialog.getFont":
            self.show_font()
        elif selected_dialog_window == "QtWidgets.QProgressDialog":
            self.show_progress()

    # QMessageBox
    def show_message_about(self) -> None:
        """
        Работа с окном QtWidgets.QMessageBox.about

        :return: None
        """

        self.plainTextEdit.setPlainText("Обработка выполнена")
        QtWidgets.QMessageBox.about(self, "Уведомление", "Обработка выполнена")

    def show_message_question(self) -> None:
        """
        Работа с окном QtWidgets.QMessageBox.question

        :return: None
        """

        answer = QtWidgets.QMessageBox.question(
            self, "Продолжить обработку", "Вы хотите продолжить выполнение цикла?",
        )

        if answer == QtWidgets.QMessageBox.Yes:
            self.plainTextEdit.setPlainText("Продолжаю обработку")
        elif answer == QtWidgets.QMessageBox.No:
            self.plainTextEdit.setPlainText("Обработка остановлена")

    def show_message_warning(self) -> None:
        """
        Работа с окном QtWidgets.QMessageBox.warning

        :return: None
        """

        self.plainTextEdit.setPlainText("Пользователь предупреждён")
        QtWidgets.QMessageBox.warning(self, "Предупреждение", "Проверьте конфигурацию")

    def show_message_critical(self) -> None:
        """
        Работа с окном QtWidgets.QMessageBox.critical

        :return: None
        """

        self.plainTextEdit.setPlainText("Критическая ошибка")
        QtWidgets.QMessageBox.critical(self, "Ошибка", "Ошибка запуска модуля")

    def show_message_aboutQt(self) -> None:
        """
        Работа с окном QtWidgets.QMessageBox.aboutQt

        :return: None
        """

        QtWidgets.QMessageBox.aboutQt(self, "О Qt")

    # QInputDialog
    def show_input_text(self) -> None:
        """
        Работа с окном QtWidgets.QInputDialog.getText

        :return: None
        """

        text, ok = QtWidgets.QInputDialog.getText(self, "Введите имя", "Как вас зовут?")

        if ok:
            self.plainTextEdit.setPlainText(f"Вас зовут: {text}")

    def show_input_int(self) -> None:
        """
        Работа с окном QtWidgets.QInputDialog.getInt

        :return: None
        """

        text, ok = QtWidgets.QInputDialog.getInt(self, "Введите число", "Сколько вам лет?")
        if ok:
            self.plainTextEdit.setPlainText(f"Вам {str(text)} лет")

    def show_input_double(self) -> None:
        """
        Работа с окном QtWidgets.QInputDialog.getDouble

        :return: None
        """

        text, ok = QtWidgets.QInputDialog.getDouble(self, "Введите число", "Какая температура за окном?")
        if ok:
            self.plainTextEdit.setPlainText(f"За окном {str(text)} C")

    def show_input_item(self) -> None:
        """
        Работа с окном QtWidgets.QInputDialog.getItem

        :return: None
        """

        text, ok = QtWidgets.QInputDialog.getItem(
            self, "Вопрос", "Сколько комнат в вашей квартире?", ["1", "2", "3"], editable=False
        )
        if ok:
            self.plainTextEdit.setPlainText(f"У вас {str(text)} комната(ы)")

    def show_input_multiline(self) -> None:
        """
        Работа с окном QtWidgets.QInputDialog.getMultiLineText

        :return: None
        """

        text, ok = QtWidgets.QInputDialog.getMultiLineText(self, "Добавить заметку", "Введите текст заметки")
        if ok:
            self.plainTextEdit.setPlainText(text)

    # QFileDialog
    def show_file_directory(self) -> None:
        """
        Работа с окном QtWidgets.QFileDialog.getExistingDirectory

        :return: None
        """

        selected_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if selected_dir:
            self.plainTextEdit.setPlainText(selected_dir)

    def show_file_directory_url(self) -> None:
        """
        Работа с окном QtWidgets.QFileDialog.getExistingDirectoryUrl

        :return: None
        """

        selected_dir = QtWidgets.QFileDialog.getExistingDirectoryUrl(self, "Выберите папку")
        print(selected_dir)  # Возвращается QtCore.QUrl
        if selected_dir:
            self.plainTextEdit.setPlainText(selected_dir.toString())

    def show_file_file_url(self) -> None:
        """
        Работа с окном QtWidgets.QFileDialog.getOpenFileUrl

        :return: None
        """

        selected_file, mask = QtWidgets.QFileDialog.getOpenFileUrl(self, "Выберите файл")
        print(selected_file)
        print(mask)
        if selected_file:
            self.plainTextEdit.setPlainText(selected_file.toString())

    def show_file_file_urls(self) -> None:
        """
        Работа с окном QtWidgets.QFileDialog.getOpenFileUrls

        :return: None
        """

        selected_files, mask = QtWidgets.QFileDialog.getOpenFileUrls(self, "Выберите файлы", filter="*.MD *.py")
        print(selected_files)
        print(mask)
        self.plainTextEdit.clear()
        for file in selected_files:
            self.plainTextEdit.appendPlainText(file.toString())

    def show_file_file_name(self) -> None:
        """
        Работа с окном QtWidgets.QFileDialog.getOpenFileName

        :return: None
        """

        selected_file, mask = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        print(selected_file)
        print(mask)
        if selected_file:
            self.plainTextEdit.setPlainText(selected_file)

    def show_file_file_names(self) -> None:
        """
        Работа с окном QtWidgets.QFileDialog.getOpenFileNames

        :return: None
        """

        selected_files, mask = QtWidgets.QFileDialog.getOpenFileNames(self, "Выберите файлы", filter="*.MD *.py")
        print(selected_files)
        print(mask)
        self.plainTextEdit.clear()
        for file in selected_files:
            self.plainTextEdit.appendPlainText(file)

    def show_file_save_name(self) -> None:
        """
        Работа с окном QtWidgets.QFileDialog.getSaveFileName

        :return: None
        """

        selected_file, mask = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить")

        print(selected_file)
        print(mask)
        if selected_file:
            self.plainTextEdit.setPlainText(selected_file)

    def show_file_save_url(self) -> None:
        """
        Работа с окном QtWidgets.QFileDialog.getSaveFileUrl

        :return: None
        """

        selected_file, mask = QtWidgets.QFileDialog.getSaveFileUrl(self, "Сохранить")

        print(selected_file)
        print(mask)
        if selected_file:
            self.plainTextEdit.setPlainText(selected_file.toString())

    # OTHER
    def show_color(self) -> None:
        """
        Работа с окном QtWidgets.QColorDialog.getColor

        :return: None
        """

        color = QtWidgets.QColorDialog.getColor(parent=self, title="Выбор цвета")
        print(color)
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(f"HSL:   {str(color.toHsl())}")
        self.plainTextEdit.appendPlainText(f"HSV:   {str(color.toHsv())}")
        self.plainTextEdit.appendPlainText(f"RGB:   {str(color.toRgb())}")
        self.plainTextEdit.appendPlainText(f"CMYK:  {str(color.toCmyk())}")
        self.plainTextEdit.appendPlainText(f"TUPLE: {str(color.toTuple())}")
        self.plainTextEdit.appendPlainText(f"ExRGB: {str(color.toExtendedRgb())}")

    def show_font(self) -> None:
        """
        Работа с окном QtWidgets.QFontDialog.getFont

        :return: None
        """

        ok, font = QtWidgets.QFontDialog.getFont(parent=self)
        if ok:
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText(f"Шрифт:        {str(font.family())}")
            self.plainTextEdit.appendPlainText(f"Размер:       {str(font.pointSize())}")
            self.plainTextEdit.appendPlainText(f"Жирный:       {str(font.weight())}")
            self.plainTextEdit.appendPlainText(f"Курсив:       {str(font.italic())}")
            self.plainTextEdit.appendPlainText(f"Подчёркнутый: {str(font.underline())}")

    def show_progress(self) -> None:
        """
        Работа с окном QtWidgets.QProgressDialog

        :return: None
        """

        pb = QtWidgets.QProgressDialog(self)
        pb.setLabelText("Прогресс")

        pb.setMinimum(0)
        pb.setValue(0)
        pb.setMaximum(100)
        pb.show()

        for i in range(100):
            if pb.wasCanceled():
                break

            pb.setValue(i)
            time.sleep(1)
            QtWidgets.QApplication.processEvents()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Window()
    myapp.show()

    app.exec()
