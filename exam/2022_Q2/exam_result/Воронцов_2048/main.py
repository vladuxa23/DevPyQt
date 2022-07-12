import sys
from random import choice
import random
from PySide2.QtWidgets import *
from window import Ui_MainWindow


class MyGame2048(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.show()
        self.win_value = 2048
        self.game_list_functions = [[self.position1, self.position2, self.position3, self.position4],

                                   [self.position5, self.position6, self.position7, self.position8],

                                   [self.position9, self.position10, self.position11, self.position12],

                                   [self.position13, self.position14, self.position15, self.position16]]
        self.game_restart()

    def game_restart(self):
        """
        Начало игры
        """
        self.field = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        QApplication.processEvents()
        #for pbtn in self.pbtn_img.buttons():
            #pbtn.setText("")
        self.spawn()
        self.left.setEnabled(True)
        self.right.setEnabled(True)
        self.up.setEnabled(True)
        self.down.setEnabled(True)
        self.display(self.field)

    def game_ruls(self):
        dialog = QDialog()
        dialog.setWindowTitle("ПРАВИЛА ИГРЫ")
        dialog.resize(500, 500)
        dialog.exec_()

    def game_exit(self):
        message = 'ЗАКРЫТЬ ПРИЛОЖЕНИЕ?'
        reply = QMessageBox.question(self, 'Уведомление', message, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            print('cancel')

    def spawn(self):
        """
        Функция, генерирующая 2 или 4 на свободном месте
        """
        new_element = random.choice([2, 4])
        try:
            (i, j) = choice([(i, j) for i in range(4) for j in range(4) if self.field[i][j] == 0])
            self.field[i][j] = new_element
        except:
            pass
        return self.field

    def init(self):
        """
        Функция, отвечающая за нажатие кнопок
        """
        self.left.clicked.connect(self.move_left)
        self.right.clicked.connect(self.move_right)
        self.up.clicked.connect(self.move_up)
        self.down.clicked.connect(self.move_down)
        self.restart.clicked.connect(self.game_restart)
        self.ruls.clicked.connect(self.game_ruls)
        self.exit.clicked.connect(self.game_exit)

    def display(self,field):
        QApplication.processEvents()
        for pbtn in self.pbtn_img.buttons():
            pbtn.setText("")
        for i in range(4):
            for j in range(4):
                if field[i][j] != 0:
                    self.game_list_functions[i][j].setText(str(field[i][j]))

    """
    Обработка ходов
    """
    def invert(self,field):
        return [row[::-1] for row in field]

    def transpose(self,field):
        return [list(row) for row in zip(*field)]

    def row_is_movable(self,row):
        """
        Функция, определяющая возможность слияния
        """
        def change(i):
            """
            Функция, определяющая возможность движения
            """
            if row[i] == 0 and row[i + 1] != 0:
                return True
            # есть возможность объединения
            if row[i] != 0 and row[i + 1] == row[i]:
                return True
            return False
        return any(change(i) for i in range(len(row) - 1))

    def all_is_movable(self, filed):
        left = any([self.row_is_movable(row) for row in filed])
        right = any([self.row_is_movable(row) for row in self.invert(filed)])
        up = any([self.row_is_movable(row) for row in self.transpose(filed)])
        down = any([self.row_is_movable(row) for row in self.invert(self.transpose(filed))])

        return left or right or up or down

    def tight(self,row):
        return sorted(row, key=lambda x:x == 0)

    def merge(self,row):
        """
        Функция, складывающая значения
        """
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0
        return row

    def move_left(self):
        """
        Функция, отвечающая за движение влево
        """
        if self.all_is_movable(self.field):
            self.field = [self.tight(self.merge(self.tight(row))) for row in self.field]
            self.field = self.spawn()
            field = self.field
            self.display(field)
            if not self.all_is_movable(field):
                QMessageBox.warning(self, "Внимание", "Это неудача!!!")
                self.left.setEnabled(False)
                self.right.setEnabled(False)
                self.up.setEnabled(False)
                self.down.setEnabled(False)
                return
            else:
                if any(any(i >= self.win_value for i in row) for row in field):
                    QMessageBox.warning(self, "Внимание", "Это победа!!!")
                    self.left.setEnabled(False)
                    self.right.setEnabled(False)
                    self.up.setEnabled(False)
                    self.down.setEnabled(False)

    def move_right(self):
        """
        Функция, отвечающая за движение вправо
        """
        self.field = self.invert(self.field)
        if self.all_is_movable(self.field):
            self.field = [self.tight(self.merge(self.tight(row))) for row in self.field]
            self.field = self.invert(self.field)
            self.field = self.spawn()
            field = self.field
            self.display(field)
            if not self.all_is_movable(self.field):
                QMessageBox.warning(self, "Внимание", "Это неудача!!!")
                self.left.setEnabled(False)
                self.right.setEnabled(False)
                self.up.setEnabled(False)
                self.down.setEnabled(False)
                return
            else:
                if any(any(i >= self.win_value for i in row) for row in self.field):
                    QMessageBox.warning(self, "Внимание", "Это победа!!!")
                    self.left.setEnabled(False)
                    self.right.setEnabled(False)
                    self.up.setEnabled(False)
                    self.down.setEnabled(False)


    def move_up(self):
        """
        Функция, отвечающая за движение вверх
        """
        self.field=self.transpose(self.field)
        if self.all_is_movable(self.field):
            self.field = [self.tight(self.merge(self.tight(row))) for row in self.field]
            self.field = self.transpose(self.field)
            self.field = self.spawn()

            field=self.field
            self.display(field)
            if not self.all_is_movable(self.field):
                QMessageBox.warning(self, "Внимание", "Это неудача!!!")
                self.left.setEnable(False)
                self.right.setEnable(False)
                self.up.setEnable(False)
                self.down.setEnable(False)
                return
            else:
                if any(any(i >= self.win_value for i in row) for row in self.field):
                    QMessageBox.warning(self, "Внимание", "Это победа!!!")
                    self.left.setEnabled(False)
                    self.right.setEnabled(False)
                    self.up.setEnabled(False)
                    self.down.setEnabled(False)

    def move_down(self):
        """
        Функция, отвечающая за движение вниз
        """
        self.field = self.invert(self.transpose(self.field))
        if self.all_is_movable(self.field):
            self.field = [self.tight(self.merge(self.tight(row))) for row in self.field]
            self.field = self.transpose(self.invert(self.field))
            self.field = self.spawn()
            field=self.field
            self.display(field)

            if not self.all_is_movable(self.field):
                QMessageBox.warning(self, "Внимание", "Это неудача!!!")
                self.left.setEnabled(False)
                self.right.setEnabled(False)
                self.up.setEnabled(False)
                self.down.setEnabled(False)
                return
            else:
                if any(any(i >= self.win_value for i in row) for row in self.field):
                    QMessageBox.warning(self, "Внимание", "Это победа!!!")
                    self.left.setEnabled(False)
                    self.right.setEnabled(False)
                    self.up.setEnabled(False)
                    self.down.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myapp = MyGame2048()
    myapp.show()
    app.exec_()