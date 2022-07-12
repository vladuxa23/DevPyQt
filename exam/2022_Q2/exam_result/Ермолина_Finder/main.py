import sys
import os
import subprocess
import re

from PySide2 import QtWidgets
from ui import searchingform


class MyFirstWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        """
        создание конструктора класса
        :param parent: None
        """
        super().__init__(parent)

        """инициализируем форму"""

        self.ui = searchingform.Ui_Form()
        self.ui.setupUi(self)
        self.initUi()
        self.maximumSize()

        self.ui.checkBox.isTristate = False
        self.ui.lineEdit_3.text()

    def initUi(self):
        """
        Назначение функций элементам управления (кнопкам)
        :return:
        """

        self.ui.pushButton.clicked.connect(self.browse_the_folder)
        self.ui.pushButton_2.clicked.connect(self.search_main)
        self.ui.pushButton_3.clicked.connect(self.open_directory)

    def browse_the_folder(self):
        """
        Осуществляется выбор папки для дальнейшего поиска
        :return: адрес выбранной папки выводится в lineEdit
        """
        self.ui.lineEdit.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Enter the folder")
        for _ in os.listdir(directory):
            self.ui.lineEdit.setText(directory)

    def search_main(self):
        """
        Основной поиск подкрепленный к кнопке Искать
        :return: в зависимости от выбранного значения combobox задействует
        соответствующий метод поиска
        """
        if self.ui.comboBox.currentText() == "Строковый поиск":
            self.str_search()
        elif self.ui.comboBox.currentText() == "Поиск по байтам":
            self.byte_sign_search()

        else:
            self.binary_sign_search()

    def str_search(self):
        """
        Поиск по формату файла
        :return: Список расположений файлов
        """
        start_folder = self.ui.lineEdit.text()   # определение начальной папки поиска, отраженной в lineEdit
        search = self.ui.lineEdit_2.text()
        self.ui.listWidget.clear()

        for root, dirs, files in os.walk(start_folder):
            for file in files:
                file_path: str = os.path.join(root, file)
                if file_path.endswith(search):
                    directories = os.path.abspath(file_path)
                    self.ui.listWidget.addItem(directories)

    def byte_sign_search(self):
        """
        Байтовый поиск
        :return: выводит расположения файлов с обнаруженными данными
        """
        start_folder = self.ui.lineEdit.text()
        search = self.ui.lineEdit_2.text()
        self.ui.listWidget.clear()
        for root, dirs, files in os.walk(start_folder):
            for file in files:
                file_path: str = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    if search.encode('utf-8') in f.read():
                        directories = os.path.abspath(file_path)
                        self.ui.listWidget.addItem(directories)

    def binary_sign_search(self):
        """
        Поиск по бинарным сигнатурам
        :return: выводит расположения файлов с обнаруженными данными
        """
        start_folder = self.ui.lineEdit.text()
        search = self.ui.lineEdit_2.text()
        self.ui.listWidget.clear()

        for root, dirs, files in os.walk(start_folder):
            for file in files:
                file_path: str = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    search_file = re.compile(search)
                    search_file.findall(file)
                    if search_file.findall(file) is not None:
                        directories = os.path.abspath(file_path)
                        self.ui.listWidget.addItem(directories)
                    else:
                        self.ui.listWidget.addItem("None")

    def open_directory(self):
        """
        Открывает расположение файла
        :return:
        """
        directory = self.ui.listWidget.currentItem().text()
        pr = subprocess.Popen(['open', directory])
        return


def main():

    app = QtWidgets.QApplication()
    myWindow = MyFirstWindow()
    myWindow.show()
    app.exec_()


if __name__ == "__main__":
    main()
