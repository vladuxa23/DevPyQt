"""
Демонстрация работы с делегатами
"""

import os
import random
import time
from typing import Union

from PySide6 import QtWidgets, QtGui, QtCore


class DoubleSpinBoxDelegate(QtWidgets.QStyledItemDelegate):
    """
    Класс для создания DoubleSpinbox делегата
    """

    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                     index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> QtWidgets.QWidget:
        """
        Создание элемента для редактирования данных

        :param parent: родитель
        :param option: настройки
        :param index: индекс где будет находиться
        :return: doubleSpinBox
        """

        # создание и настройка делегата
        editor = QtWidgets.QDoubleSpinBox(parent, decimals=2)
        editor.setFrame(False)
        editor.setMinimum(-40)
        editor.setMaximum(40)

        editor.valueChanged.connect(lambda: print(editor.value()))

        return editor

    def updateEditorGeometry(self, editor: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                             index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> None:
        """
        Обновление размера

        :param editor: виджет который настраиваем
        :param option: опции отображения
        :param index: индекс выбранного виджета
        :return: None
        """

        # установка размеров по размеру родителя
        editor.setGeometry(option.rect)


class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = []

    def setItems(self, items: list) -> None:
        """
        Установка данных в делегат

        :param items: список элементов
        :return: None
        """

        self.items = items

    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                     index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> QtWidgets.QWidget:
        """
        Создание элемента для редактирования данных

        :param parent: родитель
        :param option: настройки
        :param index: индекс где будет находиться
        :return: doubleSpinBox
        """

        editor = QtWidgets.QComboBox(parent)
        editor.addItems(self.items)
        editor.currentIndexChanged.connect(lambda: print(editor.currentText()))

        return editor

    def setModelData(self, editor: QtWidgets.QWidget, model: QtCore.QAbstractItemModel,
                     index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> None:
        """
        Установка данных из делегата в модель

        :param editor: выбранный элемент в представлении
        :param model: модель представления
        :param index: индекс выбранного элемента
        :return: None
        """

        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                             index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> None:
        """
        Обновление размера

        :param editor: виджет который настраиваем
        :param option: опции отображения
        :param index: индекс выбранного виджета
        :return: None
        """

        editor.setGeometry(option.rect)


class PushButtonDelegate(QtWidgets.QStyledItemDelegate):
    clicked = QtCore.Signal(QtCore.QModelIndex)

    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                     index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> QtWidgets.QWidget:
        """
        Создание элемента для редактирования данных

        :param parent: родитель
        :param option: настройки
        :param index: индекс где будет находиться
        :return: doubleSpinBox
        """

        button = QtWidgets.QPushButton(parent)
        button.clicked.connect(lambda *args, ix=index: self.clicked.emit(ix))

        return button

    def setEditorData(self, editor: QtWidgets.QWidget,
                      index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> None:
        """
        Установка данных в делегат при инициализации

        :param editor: выбранный делегат
        :param index: индекс выбранного делегата
        :return: None
        """

        editor.setText("...")

    def updateEditorGeometry(self, editor: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                             index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> None:
        """
        Обновление размера

        :param editor: виджет который настраиваем
        :param option: опции отображения
        :param index: индекс выбранного виджета
        :return: None
        """

        editor.setGeometry(option.rect)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initDelegates()

        self.createTableModel()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.tableView = QtWidgets.QTableView()
        self.tableView.resizeColumnsToContents()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tableView)

        self.setLayout(layout)

    def initDelegates(self) -> None:
        """
        Инициализация делегатов

        :return: None
        """

        self.doubleDelegate = DoubleSpinBoxDelegate()

        self.openDelegate = PushButtonDelegate()
        self.openDelegate.clicked.connect(self.getDataFromRow)

        self.comboBoxDelegate = ComboBoxDelegate()
        self.comboBoxDelegate.setItems(['1', '2', '3'])

    def createTableModel(self) -> None:
        """
        Создание табличной модели

        :return: None
        """

        headers = ["Путь", "Число", "Размер", "Время"]

        stm = QtGui.QStandardItemModel()
        stm.setHorizontalHeaderLabels(headers)

        data = [x for x in os.listdir()]

        stm.setRowCount(len(data))

        for row in range(len(data)):
            stm.setItem(row, 0, QtGui.QStandardItem(data[row]))
            stm.setItem(row, 1, QtGui.QStandardItem(str(random.randint(-30, 30))))
            stm.setItem(row, 2, QtGui.QStandardItem(str(os.path.getsize(data[row]))))
            stm.setItem(row, 3, QtGui.QStandardItem(str(int(time.time() + random.randint(0, 400)))))
            stm.setItem(row, 4, QtGui.QStandardItem(str(random.randint(-30, 30))))
            stm.setItem(row, 5, QtGui.QStandardItem(""))

        self.tableView.setModel(stm)
        self.tableView.setItemDelegateForColumn(1, self.doubleDelegate)
        self.tableView.setItemDelegateForColumn(4, self.openDelegate)
        self.tableView.setItemDelegateForColumn(5, self.comboBoxDelegate)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.resizeColumnsToContents()

    @staticmethod
    def getDataFromRow(push_row: QtCore.QModelIndex) -> None:
        """
        Получение данных из выделенной строки

        :param push_row: выделенная строка
        :return: None
        """

        print(type(push_row))
        row = push_row.row()
        column = push_row.column()
        print(row, column)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = Window()
    win.show()
    
    app.exec()
