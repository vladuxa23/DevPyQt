from PySide2 import QtCore, QtWidgets, QtGui
import os
import random
import time


class MyStandardItemModel(QtGui.QStandardItemModel):
    """
    Кастомная модель для работы с данными. Реализует возможность различного
    отображения данных в столбцах.
    """

    def __init__(self, parent=None):
        super(MyStandardItemModel, self).__init__(parent)

    def data(self, item, role):
        """
        Функция переопределения выдачи данных для отображения

        :param item: элемент модели
        :param role: роль элемента в модели
        :return:
        """

        # отбор отображаемых элементов
        if role == QtCore.Qt.DisplayRole:
            # по колонке определяем то как отображать данные
            if item.column() == 2:
                try:
                    size = QtGui.QStandardItemModel.data(self, item, QtCore.Qt.DisplayRole)
                    return int(size)/1024
                except Exception as err:
                    print(err)

            if item.column() == 3:
                try:
                    number = QtGui.QStandardItemModel.data(self, item, QtCore.Qt.DisplayRole)
                    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(number)))
                except ValueError:
                    pass

        # отбор фона строк
        if role == QtCore.Qt.BackgroundRole:
            if item.row() % 2:
                # возврат нового цвета фона
                return QtGui.QColor(QtCore.Qt.lightGray)

        return QtGui.QStandardItemModel.data(self, item, role)


class ComboboxWithCheckBox(QtWidgets.QComboBox):
    """
    Кастомный комбобокс, реализует возможность множественного выбора элементов
    """

    def addItem(self, item) -> None:
        """
        Переопределённая функция добавления элемента в чекбокс

        :param item: добавляемый элемент
        :return: None
        """

        # вызов стандартной функции addItem
        super(ComboboxWithCheckBox, self).addItem(item)
        # создание кастомного элемента
        item = self.model().item(self.count() - 1, 0)
        # установка флага
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        # установка статуса чекбокса
        item.setCheckState(QtCore.Qt.Unchecked)

    def itemChecked(self, index) -> bool:
        """
        Функция проверки статуса элемента

        :param index: номер элемента
        :return: True если Checked иначе False
        """

        # получение item'a
        item = self.model().item(index, 0)
        # получение его состояния
        return item.checkState() == QtCore.Qt.Checked

    def checkItems(self) -> list:
        """
        Функция проверки всего виджета на состояние объектов

        :return: Список выбранных элементов
        """

        # куда складывать checked
        checkedItems = []
        for i in range(self.count()):
            # получение статуса i-ого элемента
            if self.itemChecked(i):
                # добавление в результирующий список
                checkedItems.append(self.model().item(i, 0).text())
        return checkedItems

    def paintEvent(self, event):

        # Создание объекта для рисования
        painter = QtWidgets.QStylePainter(self)  # Отрисовка на "самом себе"
        # Устанавливаем чем будем рисовать
        painter.setPen(self.palette().color(QtGui.QPalette.Text))
        # Используем класс для отрисовки комбобокса
        opt = QtWidgets.QStyleOptionComboBox()
        self.initStyleOption(opt)  # Инициализируем параметры
        # Отрисовка на комбобоксе выбранных элементов
        opt.currentText = ", ".join(self.checkItems())
        # Отрисовка самого комбобокса
        painter.drawComplexControl(QtWidgets.QStyle.CC_ComboBox, opt)
        painter.drawControl(QtWidgets.QStyle.CE_ComboBoxLabel, opt)
        # Добавление всплывающей подсказки
        self.setToolTip("\n".join(self.checkItems()))


class DoubleDelegate(QtWidgets.QStyledItemDelegate):
    """
    Делегат, позволяющий использовать QDoubleSpinBox в таблице
    """

    def createEditor(self, parent, option, index):
        """
        Создание элемента для редактирования данных

        :param parent: Родитель
        :param option: Настройки
        :param index: Индекс где будет находиться
        :return:
        """

        # создание и настройка делегата
        editor = QtWidgets.QDoubleSpinBox(parent, decimals=2)
        editor.setFrame(False)
        editor.setMinimum(-40)
        editor.setMaximum(40)

        editor.valueChanged.connect(lambda: print(editor.value()))

        return editor

    def updateEditorGeometry(self, editor, option, index) -> None:
        """
        Обновление размера
        """

        # установка размеров по размеру родителя
        editor.setGeometry(option.rect)


class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, parent=None):
        super(ComboBoxDelegate, self).__init__(parent)
        self.items = []

    def setItems(self, items):
        """
        Установка данных в делегат

        :param items:
        :return:
        """
        self.items = items

    def createEditor(self, widget, option, index):
        """
        Создание редактора

        :param widget:
        :param option:
        :param index:
        :return:
        """
        editor = QtWidgets.QComboBox(widget)
        editor.addItems(self.items)
        editor.currentIndexChanged.connect(lambda: print(editor.currentText()))

        return editor

    def setModelData(self, editor, model, index):
        """
        Установка данных из делегата в модель

        :param editor:
        :param model:
        :param index:
        :return:
        """

        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class PushButtonDelegate(QtWidgets.QStyledItemDelegate):
    clicked = QtCore.Signal(QtCore.QModelIndex)

    def createEditor(self, parent, option, index):
        button = QtWidgets.QPushButton(parent)
        button.clicked.connect(lambda *args, ix=index: self.clicked.emit(ix))

        return button

    def setEditorData(self, editor, index):
        editor.setText("...")

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class MyDelegateWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyDelegateWindow, self).__init__(parent)

        self.initUi()

        self.loadTable()

    def initUi(self):

        self.resize(1200, 500)

        self.tableView = QtWidgets.QTableView()
        self.tableView.resizeColumnsToContents()

        self.comboBox = ComboboxWithCheckBox()
        self.comboBox.addItem("Один")
        self.comboBox.addItem("Два")
        self.comboBox.addItem("Три")

        self.pb = QtWidgets.QPushButton("...")
        self.pb.clicked.connect(self.onPBClicked)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tableView)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.pb)

        self.setLayout(layout)

        # init delegates
        self.doubleDelegate = DoubleDelegate()

        self.openDelegate = PushButtonDelegate()
        self.openDelegate.clicked.connect(self.getDataFromRow)

        self.comboBoxDelegate = ComboBoxDelegate()
        self.comboBoxDelegate.setItems(['1', '2', '3'])

    def getDataFromRow(self, push_row):

        row = push_row.row()
        column = push_row.column()
        print(row, column)

    def onPBClicked(self):
        print(self.comboBox.checkItems())

    def loadTable(self):
        headers = ["Путь", "Число", "Размер", "Время"]

        # stm = QtGui.QStandardItemModel()
        stm = MyStandardItemModel()
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


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = MyDelegateWindow()
    win.show()
    app.exec_()