"""
Демонстрация использования древовидной модели
"""

from PySide6 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.initTreeModel()
        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.resize(520, 360)

        treeView = QtWidgets.QTreeView(self)
        treeView.setModel(self.treeModel)
        treeView.header().resizeSection(0, 200)
        treeView.expandAll()

        treeView.selectionModel().currentChanged.connect(self.onCurrentChanged)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(treeView)

        self.setLayout(layout)

    def initTreeModel(self) -> None:
        """
        Инициализация древовидной модели

        :return: None
        """

        self.treeModel = QtGui.QStandardItemModel()
        self.treeModel.setHorizontalHeaderLabels(['Проект', 'Информация'])

        # Добавление root элемента
        itemProject = QtGui.QStandardItem('Проект')
        self.treeModel.appendRow(itemProject)
        self.treeModel.setItem(0, 1, QtGui.QStandardItem('Описание проекта'))

        # Добавление subroot элемента
        itemChild = QtGui.QStandardItem('Папка 1')
        itemProject.appendRow(itemChild)
        itemProject.setChild(0, 1, QtGui.QStandardItem('Описание'))

        # Продолжаем добавлять элементы
        itemFolder = QtGui.QStandardItem('Папка 2')
        itemProject.appendRow(itemFolder)

        for group in range(5):
            itemGroup = QtGui.QStandardItem(f'Группа_{group + 1}')
            itemFolder.appendRow(itemGroup)

        for ch in range(group + 1):
            itemCh = QtGui.QStandardItem(f'Элемент_{ch + 1}')
            itemCh.setCheckable(True)

            itemGroup.appendRow(itemCh)
            itemGroup.setChild(itemCh.index().row(), 1, QtGui.QStandardItem(f'Элемент_{ch + 1} описание'))

            itemProject.setChild(itemFolder.index().row(), 1, QtGui.QStandardItem('Папка 2 описание'))

    @staticmethod
    def onCurrentChanged(current) -> None:
        """
        Обработка нажатия на элемент в treeView

        :param current: текущий выбранный элемент
        :return: None
        """

        txt = f'Родитель:[{str(current.parent().data())}]\n'
        txt += f'Текущий элемент: [(строка: {current.row()}, столбец {current.column()})]\n'

        if current.column() == 0:
            name = str(current.data())
            info = str(current.sibling(current.row(), 1).data())
        else:
            name = str(current.sibling(current.row(), 0).data())
            info = str(current.data())

        txt += f'Имя:[{name}] Информация:[{info}]\n'

        print(txt)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
