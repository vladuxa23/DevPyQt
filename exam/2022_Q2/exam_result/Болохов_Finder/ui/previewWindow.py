import sys
import os

from PySide2 import QtCore, QtWidgets, QtGui


class PrevieWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name
        self.initUi()

    def initUi(self):
        self.setMinimumSize(640, 480)
        self.setWindowTitle(self.file_name)

        layout = QtWidgets.QVBoxLayout()
        self.memo = QtWidgets.QTextBrowser()
        layout.addWidget(self.memo)
        self.setLayout(layout)

        self.messegeErr = QtWidgets.QErrorMessage()

    def read_file(self):
        """
        чтение файла и вывод его на форму
        """
        try:
            with open(self.file_name, 'r', encoding=self.detect_code(self.file_name, os.stat(self.file_name).st_size)) as fh:
                self.memo.setText(fh.read())

        except (PermissionError, IOError) as err:
            self.messegeErr.showMessage(str(err))


    @staticmethod
    def detect_code(fname: str, size: int) -> str:
        """
        получение кодировки файла (не 100% решение)
        :param fname: имя файла (полный путь)
        :return: название кодировки
        """
        encoding = [
            'utf-8',
            'cp500',
            'utf-16',
            'GBK',
            'windows-1251',
            'ASCII',
            'US-ASCII',
            'Big5'
        ]

        if size > 1024:
            size = 1024
        for enc in encoding:
            try:
                with open(fname, 'r', encoding=enc) as fr:
                    fr.read(size)
            except (UnicodeDecodeError, LookupError):
                pass
            except PermissionError:
                print('Отказано в доступе')
            else:
                return enc
            return None