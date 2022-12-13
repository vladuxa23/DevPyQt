"""
Демонстрация создания "кастомной" модели с данными и модели для фильтрации
"""

from typing import Union, Any

from PySide6 import QtCore, QtWidgets
from random_word import RandomWords


class MyModel(QtCore.QAbstractListModel):

    def __init__(self, data: list, parent=None):
        super().__init__(parent)

        self.model_data = data
        self.filtered_data = self.model_data

    def data(self, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex], role: int = ...) -> Any:
        """
        Отображение данных модели

        :param index: индекс элемента
        :param role: вид отображения элемента
        :return: любой элемент
        """

        if role == QtCore.Qt.DisplayRole:
            return self.filtered_data[index.row()]

    def rowCount(self, parent: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex] = ...) -> int:
        """
        Количество строк в модели

        :param parent: родитель
        :return: число строк
        """

        return len(self.filtered_data)


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._filter = ""

    def filterAcceptsRow(self, source_row: int,
                         source_parent: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> bool:
        """
        Применяет фильтрацию к модели

        :param source_row: исходная строка
        :param source_parent: исходный родитель
        :return: True | False
        """

        index = self.sourceModel().index(source_row, 0, source_parent)
        if self.filter:
            return self.filter in index.data()
        return True

    @property
    def filter(self) -> str:
        """
        Геттер для фильтра

        :return: строка фильтрации
        """

        return self._filter

    @filter.setter
    def filter(self, text: str) -> None:
        """
        Геттер фильтра

        :param text: строка фильтрации

        :return: None
        """

        self._filter = text
        self.invalidateFilter()


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initModel()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.lineEdit = QtWidgets.QLineEdit()

        self.listView = QtWidgets.QListView()
        self.listView.setModel(self.proxyModel)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.listView)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.lineEdit.textChanged.connect(self.text_changed)

    def text_changed(self) -> None:
        """
        Действие при изменении текста фильтрации

        :return: None
        """

        self.proxyModel.filter = self.lineEdit.text()

    def initModel(self) -> None:
        """
        Инициализация модели для QListView

        :return: None
        """

        model = MyModel(RandomWords().get_random_words())
        self.proxyModel = SortFilterProxyModel()
        self.proxyModel.setSourceModel(model)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
