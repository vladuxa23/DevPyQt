from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton
from PySide2.QtGui import QPainter, QColor, QFont, QPen, QIcon
from PySide2.QtCore import Qt, QRect
import sys
import os
import copy
import random


class GameForm(QMainWindow):
    def __init__(self, parent=None):
        super(GameForm, self).__init__(parent)
        self.initUi()
        # Цвет, соответствующий каждому числу в игре, все по канону классического 2048
        self.colors = {0: (204, 192, 179), 2: (238, 228, 218), 4: (237, 224, 200),
                       8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
                       64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 207, 114),
                       512: (237, 207, 114), 1024: (237, 207, 114), 2048: (237, 207, 114),
                       4096: (237, 207, 114), 8192: (237, 207, 114), 16384: (237, 207, 114),
                       32768: (237, 207, 114), 65536: (237, 207, 114), 131072: (237, 207, 114),
                       262144: (237, 207, 114), 524288: (237, 207, 114), 1048576: (237, 207, 114)}
        self.initGameData()
        self.grid
    def initUi(self):
        """Инициализация интерфейса"""
        self.setWindowTitle("2048")
        self.setWindowIcon(QIcon('2048.png'))
        self.initGameOpt()
        self.grid = 0
        msg = QMessageBox()
        msg.setWindowTitle("Добро пожаловать")
        msg.setWindowIcon(QIcon('2048.png'))
        msg.setText("Выберите размер поля")
        Button3 = msg.addButton("3X3", QMessageBox.AcceptRole)
        Button4 = msg.addButton("4X4", QMessageBox.AcceptRole)
        Button5 = msg.addButton("5X5", QMessageBox.AcceptRole)
        msg.setDefaultButton(Button4)
        msg.exec_()
        if msg.clickedButton() == Button3:
            self.grid = 3
            self.resize(550, 550)
        elif msg.clickedButton() == Button4:
            self.grid = 4
            self.resize(520, 670)
        elif msg.clickedButton() == Button5:
            self.grid = 5
            self.resize(620, 760)

    def initGameOpt(self):
        """Инициализация шрифтов"""
        self.lbFont = QFont('Colibri', 8)  # текст
        self.lgFont = QFont('Times', 38)  # логотип
        self.nmFont = QFont('SimSun', 36)  # числа на фишках


    def initGameData(self):
        """Инициализация данных игры"""

        if self.grid == 3:
            self.data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        elif self.grid == 4:
            self.data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        else:
            self.data = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        count = 0
        while count < 2:
            row = random.randint(0, len(self.data) - 1)
            col = random.randint(0, len(self.data[0]) - 1)
            if self.data[row][col] != 0:
                continue
            self.data[row][col] = 2 if random.randint(0, 1) else 4
            count += 1

        self.curScore = 0
        self.bstScore = 0
        # Загрузить рекорд
        if os.path.exists("bestscore.ini"):
            with open("bestscore.ini", "r") as f:
                self.bstScore = int(f.read())


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawGameGraph(qp)
        qp.end()

    def keyPressEvent(self, e):
        """
        нажатие клавиш на клавиатуре
        """
        keyCode = e.key()
        ret = False
        if keyCode == Qt.Key_Left:
            ret = self.move("Left")
        elif keyCode == Qt.Key_A:
            ret = self.move("Left")
        elif keyCode == Qt.Key_Right:
            ret = self.move("Right")
        elif keyCode == Qt.Key_D:
            ret = self.move("Right")
        elif keyCode == Qt.Key_Up:
            ret = self.move("Up")
        elif keyCode == Qt.Key_W:
            ret = self.move("Up")
        elif keyCode == Qt.Key_Down:
            ret = self.move("Down")
        elif keyCode == Qt.Key_S:
            ret = self.move("Down")
        else:
            pass

        if ret:
            self.repaint()

    def closeEvent(self, e):
        # Сохранить рекорд в игре
        with open("bestscore.ini", "w") as f:
            f.write(str(self.bstScore))

    def drawGameGraph(self, qp):
        """Графика игры"""
        self.drawLog(qp)
        self.drawLabel(qp)
        self.drawScore(qp)
        self.draw_bg(qp)
        self.drawTiles(qp)

    def drawScore(self, qp):
        """Окно со счётом в игре"""
        qp.setFont(self.lbFont)
        fontsize = self.lbFont.pointSize()
        scoreLabelSize = len(u"СЧЁТ") * fontsize
        bestLabelSize = len(u"РЕКОРД") * fontsize
        curScoreBoardMinW = 15 * 2 + scoreLabelSize  # минимальная ширина столбца "Счет"
        bstScoreBoardMinW = 15 * 2 + bestLabelSize  # ширина столбца "рекорд"
        curScoreSize = len(str(self.curScore)) * fontsize
        bstScoreSize = len(str(self.bstScore)) * fontsize
        curScoreBoardNedW = 10 + curScoreSize
        bstScoreBoardNedW = 10 + bstScoreSize
        curScoreBoardW = max(curScoreBoardMinW, curScoreBoardNedW)
        bstScoreBoardW = max(bstScoreBoardMinW, bstScoreBoardNedW)
        qp.setBrush(QColor(187, 173, 160))
        qp.setPen(QColor(187, 173, 160))
        qp.drawRect(505 - 15 - bstScoreBoardW, 40, bstScoreBoardW, 50)
        qp.drawRect(505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 40, curScoreBoardW, 50)

        bstLabelRect = QRect(505 - 15 - bstScoreBoardW, 40, bstScoreBoardW, 25)
        bstScoreRect = QRect(505 - 15 - bstScoreBoardW, 65, bstScoreBoardW, 25)
        scoerLabelRect = QRect(505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 40, curScoreBoardW, 25)
        curScoreRect = QRect(505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 65, curScoreBoardW, 25)

        qp.setPen(QColor(238, 228, 218))
        qp.drawText(bstLabelRect, Qt.AlignCenter, u"РЕКОРД")
        qp.drawText(scoerLabelRect, Qt.AlignCenter, u"СЧЁТ")

        qp.setPen(QColor(255, 255, 255))
        qp.drawText(bstScoreRect, Qt.AlignCenter, str(self.bstScore))
        qp.drawText(curScoreRect, Qt.AlignCenter, str(self.curScore))

    def draw_bg(self, qp):

        """Игровое поле"""
        col = QColor(187, 173, 160)
        qp.setPen(col)

        qp.setBrush(QColor(187, 173, 160))
        if self.grid == 3:
            qp.drawRect(15, 150, 360, 360)
        elif self.grid == 4:
            qp.drawRect(15, 150, 475, 475)
        elif self.grid == 5:
            qp.drawRect(15, 150, 590, 590)

    def drawLog(self, qp):
        """Лого игры"""
        pen = QPen(QColor(255, 93, 29), 15)
        qp.setFont(self.lgFont)
        qp.setPen(pen)
        qp.drawText(QRect(45, 0, 185, 130), Qt.AlignCenter, "2048")

    def drawLabel(self, qp):
        """Текст к игре"""
        qp.setFont(self.lbFont)
        qp.setPen(QColor(119, 110, 101))
        qp.drawText(15, 134, u"Цель игры - получить фишку с максимальной степенью двойки")

    def drawTiles(self, qp):
        """Нарисовать клетки"""
        qp.setFont(self.nmFont)
        for row in range(self.grid):
            for col in range(self.grid):
                value = self.data[row][col]
                color = self.colors[value]

                qp.setPen(QColor(*color))
                qp.setBrush(QColor(*color))
                qp.drawRect(30 + col * 115, 165 + row * 115, 100, 100)
                size = self.nmFont.pointSize() * len(str(value))  # Получить длину числа
                # Подгоняем размер шрифта в соответствии с размером числа
                while size > 100 - 15 * 2:
                    self.nmFont = QFont('SimSun', self.nmFont.pointSize() * 4 // 5)
                    qp.setFont(self.nmFont)
                    size = self.nmFont.pointSize() * len(str(value))   # Получить длину числа в текущем шрифте
                print("[%d][%d]: value[%d] weight: %d" % (row, col, value, size))

                if value == 2 or value == 4:
                    qp.setPen(QColor(119, 110, 101))  # Установим цвет чисел 2 и 4 (из-за фона)
                else:
                    qp.setPen(QColor(255, 255, 255))  # Установим цвет остальных чисел
                # Рисуем все числа, кроме нулей
                if value != 0:
                    rect = QRect(30 + col * 115, 165 + row * 115, 100, 100)
                    qp.drawText(rect, Qt.AlignCenter, str(value))

    def putTile(self):
        """Найти пустую клетку и рандомно вставить '2' или '4'"""
        available = []
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                if self.data[row][col] == 0:
                    available.append((row, col))
        if available:
            row, col = available[random.randint(0, len(available) - 1)]
            self.data[row][col] = 2 if random.randint(0, 1) else 4
            return True
        return False

    def merge(self, row):
        """соединение ряда или столбца"""
        pair = False
        newRow = []
        for i in range(len(row)):
            if pair:
                newRow.append(2 * row[i])
                self.curScore += 2 * row[i]
                pair = False
            else:
                if i + 1 < len(row) and row[i] == row[i + 1]:
                    pair = True
                else:
                    newRow.append(row[i])
        return newRow

    def slideUpDown(self, isUp):
        """перемещение чисел вверх и вниз"""
        numRows = len(self.data)
        numCols = len(self.data[0])
        oldData = copy.deepcopy(self.data)

        for col in range(numCols):
            cvl = []
            for row in range(numRows):
                if self.data[row][col] != 0:
                    cvl.append(self.data[row][col])  # извлекаем ненулевые элементы

            if len(cvl) >= 2:
                cvl = self.merge(cvl)  # Соединить одинаковые числа

            # Заполняем нули в соответствии с передвижением
            for i in range(numRows - len(cvl)):
                if isUp:
                    cvl.append(0)
                else:
                    cvl.insert(0, 0)

            row = 0
            print("row=%d" % row)

            for row in range(numRows):
                self.data[row][col] = cvl[row]

        return oldData != self.data  # проверка изменения данных

    def slideLeftRight(self, isLeft):
        """Перемещение чисел влево и вправо"""
        numRows = len(self.data)
        numCols = len(self.data[0])
        oldData = copy.deepcopy(self.data)

        for row in range(numRows):
            rvl = []
            for col in range(numCols):
                if self.data[row][col] != 0:
                    rvl.append(self.data[row][col])

            if len(rvl) >= 2:
                rvl = self.merge(rvl)

            for i in range(numCols - len(rvl)):
                if isLeft:
                    rvl.append(0)
                else:
                    rvl.insert(0, 0)

            col = 0
            for col in range(numCols):
                self.data[row][col] = rvl[col]

        return oldData != self.data

    def move(self, direction):
        """Перемещение сетки чисел"""
        isMove = False
        if direction == "Up":
            isMove = self.slideUpDown(True)
        elif direction == "Down":
            isMove = self.slideUpDown(False)
        elif direction == "Left":
            isMove = self.slideLeftRight(True)
        elif direction == "Right":
            isMove = self.slideLeftRight(False)
        else:
            pass

        if not isMove:
            return False

        self.putTile()  # Вставить новую фишку с новым ходом
        if self.curScore > self.bstScore:
            self.bstScore = self.curScore

        if self.isGameOver():
            button = QMessageBox.information(self, "Игра окончена",
                                             f"Ваш счёт: {self.curScore}, начать заново?",
                                             QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok)

            if button == QMessageBox.Ok:
                self.initGameOpt()
                bstScore = self.bstScore
                self.initGameData()
                self.bstScore = bstScore
                return True
            else:
                self.close()
                return False

        else:
            return True

    def isGameOver(self) -> bool:
        """Функция, определяющая, можно ли продолжать игру"""
        copyData = copy.deepcopy(self.data)  # временно сохраняем данные игры
        curScore = self.curScore

        flag = False
        if not self.slideUpDown(True) and not self.slideUpDown(False) and \
                not self.slideLeftRight(True) and not self.slideLeftRight(False):
            flag = True  # Больше невозможно двигаться ни в одном направлении
        self.curScore = curScore
        if not flag:
            self.data = copyData  # Можно двигаться дальше, восстанавливаем исходные данные
        return flag



if __name__ == '__main__':
    app = QApplication(sys.argv)   # Создаем  объект приложения
    form = GameForm()   # Создание формы
    form.show()    # показ формы
    sys.exit(app.exec_())    # выход если exit
