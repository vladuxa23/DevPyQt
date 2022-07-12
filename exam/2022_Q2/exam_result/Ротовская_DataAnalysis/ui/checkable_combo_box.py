from PySide2 import QtWidgets, QtCore, QtGui


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

    def addItems(self, items):
        super(ComboboxWithCheckBox, self).addItems(items)

        for elem in items:
            self.addItem(elem)

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
        opt.currentText = ",".join(self.checkItems())
        # Отрисовка самого комбобокса
        painter.drawComplexControl(QtWidgets.QStyle.CC_ComboBox, opt)
        painter.drawControl(QtWidgets.QStyle.CE_ComboBoxLabel, opt)
        # Добавление всплывающей подсказки
        self.setToolTip("\n".join(self.checkItems()))
