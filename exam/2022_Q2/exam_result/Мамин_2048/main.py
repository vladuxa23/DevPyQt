from PySide2 import QtCore, QtGui, QtWidgets
import pickle
import sys

from GameClass2048 import Game2048
from ui.Game2048_window import Ui_MainWindow


def size_button(n):
    return int((430 - (n - 1) * 10) / n)


class MyWindow(QtWidgets.QMainWindow):
    """
    Класс для создания окна для игры 2048
    """

    padding = 10
    layout_up = 40
    width = 450
    height = 515
    n_cells = 4
    points = 0
    settings_name = 'settings'
    best_record = None
    settings = None
    labels = None
    game = None
    color_db = {
        '2': '#fef200',
        '4': '#ffc90d',
        '8': '#fe7f27',
        '16': '#b5e51d',
        '32': '#a349a3',
        '64': '#3f47cc',
        '128': '#880016',
        '256': '#2dde86',
        '512': '#e71a81',
        '1024': '#f00e0f',
        '2048': '#f00e0f',
        '4096': '#f98484',
        '8192': '#53abac',
        '16384': '#43c55b',
        '32768': '#fcafc1',
        '65536': '#c7bfe6',
    }

    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        try:
            self.settings = pickle.load(open(self.settings_name, 'rb'))
        except:
            best_record = {}
            for i in range(3, 6):
                best_record[i] = 0
            self.settings = {
                'best_record': best_record.copy(),
                'n_cells': 4,
                'points': 0,
                'game': Game2048(4, 4),
            }
            with open('set.pic', 'wb') as f:
                pickle.dump(self.settings, f)

        self.best_record = self.settings['best_record']
        self.n_cells = self.settings['n_cells']
        self.points = self.settings['points']
        self.game = self.settings['game']

        # Активирование действий через Меню (Qmenu.QAction)
        self.ui.action.triggered.connect(self.restart_game)
        self.ui.action3_3.triggered.connect(lambda: self.set_n_cells(3))
        self.ui.action4_4.triggered.connect(lambda: self.set_n_cells(4))
        self.ui.action5_5.triggered.connect(lambda: self.set_n_cells(5))
        self.ui.action_reset_record.triggered.connect(self.reset_best_record)
        self.create_window_labels(1)


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        """
        Сохранение результатов игры по событию закрытия окна
        :param a0:
        :return:
        """
        self.settings['best_record'] = self.best_record
        self.settings['n_cells'] = self.n_cells
        self.settings['points'] = self.points
        self.settings['game'] = self.game
        with open(self.settings_name, 'wb') as f:
            pickle.dump(self.settings, f)

    def set_n_cells(self, n):
        """
        Метод выбора поля игры
        :param n:
        :return:
        """
        self.n_cells = n
        self.restart_game()

    def reset_best_record(self):
        """
        Метод обнуления лучших результатов
        :return:
        """
        self.best_record[self.n_cells] = 0
        self.ui.label.setText(str(self.best_record[self.n_cells]))

    def create_window_labels(self, first=0):
        """
        # Метод создания поля для игры
        :param first:
        :return:
        """
        first_pixel_x = self.padding
        first_pixel_y = self.layout_up + self.padding

        size_button_value = size_button(self.n_cells)

        self.labels = []
        for i in range(self.n_cells):
            self.labels.append([])
            for j in range(self.n_cells):
                self.labels[i].append(QtWidgets.QLabel(self.centralWidget())) # Класс объекта надпись (QLabel)
                self.labels[i][j].setStyleSheet("""background-color: rgb(255,255,255);
                                                   border: 1px solid;""")
                # Изменение положение компонента и его размера ( <X>, <Y>, <Ширина>, <Высота> )
                self.labels[i][j].setGeometry(QtCore.QRect(first_pixel_x + (size_button_value + self.padding) * j,
                                                       first_pixel_y + (size_button_value + self.padding) * i,
                                                       size_button_value, size_button_value))
                self.labels[i][j].setFont(QtGui.QFont('Sitka Text', size_button_value // 6))
                self.labels[i][j].setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.labels[i][j].show()

        self.ui.label.setText(str(self.best_record[self.n_cells]))

        if first == 0:
            self.game = Game2048(self.n_cells, self.n_cells)
            self.points = 0
        self.show_grid(0)


    def restart_game(self):
        """
        Метод рестарта игры
        :return:
        """
        for i in range(len(self.labels)):
            for j in range(len(self.labels[i])):
                self.labels[i][j].deleteLater()
             
        self.create_window_labels()


    def show_grid(self, return_value):
        """
        Метод заполнения данных и проверка окончания игры
        :param return_value:
        :return:
        """
        for i in range(self.n_cells):
            for j in range(self.n_cells):
                value = str(self.game.grid[i][j])
                if value == '0':
                    self.labels[i][j].setStyleSheet("""background-color: rgb(255,255,255);
                                                       border: 1px solid;""")
                    self.labels[i][j].setText('')
                    continue
                self.labels[i][j].setText(value)
                self.labels[i][j].setStyleSheet(f"background-color: {self.color_db[value]};\
                                                    border: 1px solid;")
        self.points += return_value
        self.ui.label_2.setText(str(self.points))

        if int(return_value) % 2 == 1:
            self.points += 1
            self.ui.label_2.setText(str(self.points))
            msg = QtWidgets.QMessageBox()
            msg.setText(f'Вы проиграли с количеством очков {self.points}.\nПопробуйте еще раз.')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.setWindowTitle('Поражение')
            msg.show()
            if msg.exec_() == QtWidgets.QMessageBox.Ok:
                self.restart_game()

        if self.points > self.best_record[self.n_cells]:
            self.best_record[self.n_cells] = self.points
            self.ui.label.setText(str(self.best_record[self.n_cells]))


    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        """
        Метод обработки нажатия клавиш
        :param e:
        :return:
        """

        if e.key() == QtCore.Qt.Key_S:
            self.show_grid(self.game.swap_down())
        elif e.key() == QtCore.Qt.Key_W:
            self.show_grid(self.game.swap_up())
        elif e.key() == QtCore.Qt.Key_A:
            self.show_grid(self.game.swap_left())
        elif e.key() == QtCore.Qt.Key_D:
            self.show_grid(self.game.swap_right())
        elif e.key() == QtCore.Qt.Key_Down:
            self.show_grid(self.game.swap_down())
        elif e.key() == QtCore.Qt.Key_Up:
            self.show_grid(self.game.swap_up())
        elif e.key() == QtCore.Qt.Key_Left:
            self.show_grid(self.game.swap_left())
        elif e.key() == QtCore.Qt.Key_Right:
            self.show_grid(self.game.swap_right())
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    app.exec_()