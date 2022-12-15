"""
Демонстрация создания и удаления виджетов
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.pushButtonAddWidget = QtWidgets.QPushButton("Добавить элемент")
        self.pushButtonGetData = QtWidgets.QPushButton("Получить данные")
        self.pushButtonDelWidget = QtWidgets.QPushButton("Удалить элемент")

        self.verticalLayoutDynamicWidgets = QtWidgets.QVBoxLayout()

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(self.verticalLayoutDynamicWidgets)
        layout.addSpacerItem(
            QtWidgets.QSpacerItem(
                10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
            )
        )
        layout.addWidget(self.pushButtonAddWidget)
        layout.addWidget(self.pushButtonGetData)
        layout.addWidget(self.pushButtonDelWidget)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.pushButtonAddWidget.clicked.connect(self.onPushButtonAddWidgetClicked)
        self.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)
        self.pushButtonDelWidget.clicked.connect(self.onPushButtonDelWidgetClicked)

    def onPushButtonAddWidgetClicked(self) -> None:
        """
        Динамическое добавление виджета на layout

        :return: None
        """

        new_widget = QtWidgets.QLineEdit()
        new_widget.setObjectName(f"lineEdit_{self.verticalLayoutDynamicWidgets.count()}")

        self.verticalLayoutDynamicWidgets.addWidget(new_widget)

    def onPushButtonGetDataClicked(self) -> None:
        """
        Получение данных из виджетов

        :return: None
        """

        result = []
        for i in range(self.verticalLayoutDynamicWidgets.count()):
            widget_link = self.verticalLayoutDynamicWidgets.itemAt(i).widget()
            result.append(widget_link.text())

        print(result)

    def onPushButtonDelWidgetClicked(self) -> None:
        """
        Удаление динамически добавленного виджета

        :return: None
        """

        last_widget = self.verticalLayoutDynamicWidgets.count() - 1

        widget_link = self.verticalLayoutDynamicWidgets.itemAt(last_widget)
        if not widget_link:
            return

        widget_link = widget_link.widget()

        print(widget_link)
        widget_link.deleteLater()
        # аналогичное действие
        # widget_link.setParent(None)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
