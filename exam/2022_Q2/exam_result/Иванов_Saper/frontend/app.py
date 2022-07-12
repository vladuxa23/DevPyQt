from PySide2 import QtWidgets

from backend import Manager, Cell


class Application(QtWidgets.QWidget):

    def __init__(self, app, level, parent=None):
        super().__init__(parent)
        self.app: Manager = app
        self.level: str = level
        self.zero: int = 0

        self.grid = QtWidgets.QGridLayout()

        self.initUi()

    def initUi(self):
        """- инициализация интерфейса """
        self.setWindowTitle('Сапёр')

        self.initApp()
        self.initGrid()

    def initApp(self):
        """- инициализация backend """
        self.app.field.init_field(level=self.level)

    def initGrid(self):
        """- инициализация сетки """
        # задать интервал между кнопками, на поле
        self.grid.setSpacing(self.zero)
        # Заполнить сетку значениями
        self.setGrid()
        # добавляем сетку в главный слой
        self.setLayout(self.grid)

    def onClick(self):
        """- Событие по кнопке """
        # получить экземпляр класса по которому было проведено событие
        instance = self.sender()
        # передать координаты объекта в сетке
        self.handlerApp(instance.coord)

    def setGrid(self, disabled=False):
        """- Заполнить сетку значениями
        disabled - Если значение True то все кнопки перевести в режим отключения, и отобразить значение
        """
        for cells in self.app.field.cells:
            for obj in cells:
                # Передать кнопкам объект поля
                btn = AppBtn(obj=obj, disabled=disabled)
                # создаем событие по кнопки
                btn.clicked.connect(self.onClick)
                # Заполнить сетку значениями
                self.grid.addWidget(btn, obj.row, obj.column)

    def handlerApp(self, args):
        """- Перебрать данные в матрицы """
        # передать координаты в обработчик
        self.app.handler(args)
        # флаг поражения или победы
        success = self.app.field.is_disabled
        # проверка победы
        if success is True:
            # блокировать все ячейки и отобразить все значения кнопок
            self.setGrid(True)
            QtWidgets.QMessageBox.information(self, "Победа", "ВЫ ПОБЕЛИ УРА! :) ")
        # проверка победы
        elif success is False:
            # блокировать все ячейки и отобразить все значения кнопок
            QtWidgets.QMessageBox.warning(self, "Поражение", "ВЫ ПРОИГРАЛИ :( ")
            self.setGrid(True)
        else:
            # перезаписать сетку, обновленными данными из свойства self.app.field.cells
            self.setGrid()


class AppBtn(QtWidgets.QPushButton):
    """- Переопределяем виджет кнопки """

    def __init__(self, obj, disabled):
        super().__init__()
        self.disabled: bool = disabled
        self.obj: Cell = obj
        self.width: int = 35
        self.height: int = 35

        self.initBtn()

    def initBtn(self):
        """- инициализируем свойства по умолчанию """
        # устанавливаем размер кнопки
        self.setFixedSize(self.width, self.height)
        # запустить обработчик
        self.handlerBtn()

    def handlerBtn(self):
        """- обработчик представления кнопки в сетке """

        # проверка на блокировку всех кнопок
        if self.disabled:
            self.setDisabled(self.disabled)
            self.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
            # Если ячейка мина
            if self.obj.is_mine:
                self.setText(f'M')
                self.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
            # Если есть информация о минах поблизости
            elif self.obj.is_count_mine:
                self.setText(f'{self.obj.count_mine_near}')

        else:
            # Если ячейка была открыта
            if self.obj.is_open:
                self.setEnabled(self.disabled)
                self.setStyleSheet('QPushButton {background-color: #A3C1DA; color: blue;}')
                # Если ячейка мина
                if self.obj.is_mine:
                    self.setText(f'M')
                    self.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
                # проверка на присутствие мин поблизости
                elif self.obj.is_count_mine:
                    self.setText(f'{self.obj.count_mine_near}')

    @property
    def coord(self) -> tuple:
        """- передать координаты кнопки в сетке """
        return self.obj.row, self.obj.column


class LevelApp(QtWidgets.QWidget):
    """- Выбор сложности """

    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app: Manager = app
        self.easy: str = 'Легкий'
        self.medium: str = 'Средний'
        self.hard: str = 'Сложный'
        self.instance = None
        self.level = None

        self.box = QtWidgets.QHBoxLayout()
        self.btnEasy = QtWidgets.QPushButton()
        self.btnMedium = QtWidgets.QPushButton()
        self.btnHard = QtWidgets.QPushButton()

        self.initUi()

    def initUi(self):
        """- инициализация интерфейса """
        # задаем заголовок окну
        self.setWindowTitle('Уровень сложности')

        # именуем кнопки
        self.btnEasy.setText(self.easy)
        self.btnMedium.setText(self.medium)
        self.btnHard.setText(self.hard)

        # размещаем кнопки в вертикальном слое
        self.box.addWidget(self.btnEasy)
        self.box.addWidget(self.btnMedium)
        self.box.addWidget(self.btnHard)

        # передаем в основной слой
        self.setLayout(self.box)

        # коннект события с обработчиком
        self.btnEasy.clicked.connect(self.onClickHandler)
        self.btnMedium.clicked.connect(self.onClickHandler)
        self.btnHard.clicked.connect(self.onClickHandler)

    def onClickHandler(self):
        """- Событие по кнопке """
        # получить текст кнопки
        text = self.sender().text()
        # передать значение уровня сложности
        if text == self.easy:
            self.level = 'EASY'
        elif text == self.medium:
            self.level = 'MEDIUM'
        elif text == self.hard:
            self.level = 'HARD'

        # Создаем экземпляр приложения
        self.instance = Application(app=self.app, level=self.level)
        self.instance.show()

        self.close()
