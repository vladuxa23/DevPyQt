import sys
import os
import copy
import random

from PySide2 import QtWidgets
from PySide2.QtCore import QRect, Qt
from PySide2.QtGui import QPainter, QFont, QColor, QPen
from PySide2.QtWidgets import QMainWindow, QMessageBox, QSizePolicy


class GameForm(QMainWindow):
    """
    Colors отпределяют цвет каждого числа.
    """
    def __init__(self, parent=None):
        super(GameForm, self).__init__(parent)
        self.initUi()
        self.colors = {0: (204, 192, 179), 2: (238, 228, 218), 4: (237, 224, 200),
                       8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
                       64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 207, 114),
                       512: (237, 207, 114), 1024: (237, 207, 114), 2048: (237, 207, 114)}
        self.initGameData()

    def initUi(self) -> None:
        """
        Инициализация окна.
        :return: None
        """
        self.setWindowTitle("2048")
        self.resize(720, 840)
        # self.setFixedSize(self.width(), self.height())
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.setSizePolicy(sizePolicy)
        self.initGameOpt()

    def initGameOpt(self) -> None:
        """
        Инициализация конфигурации игры.
        :return: None
        """
        self.lbFont = QFont('Arial', 12)  # Шрифт текста на окне
        self.lgFont = QFont('Arial', 50)  # Шрифт названия
        self.nmFont = QFont('Arial', 36)  # Шрифт цифр

    def initGameData(self) -> None:
        """
        Инициализация стартового игрового поля.
        :return: None
        """

        button = QMessageBox.warning(self, "Вопрос", u"Выбираем размер поля?",
                                     QMessageBox.Ok | QMessageBox.No,
                                     QMessageBox.Ok)
        if button == QMessageBox.Ok:
            button2 = QMessageBox.warning(self, "Вопрос", u"Ok - 5x5, No - 3x3?",
                                         QMessageBox.Ok | QMessageBox.No,
                                         QMessageBox.Ok)
            if button2 == QMessageBox.Ok:
                self.data = [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]
                self.range = 5

            elif button2 == QMessageBox.No:
                self.data = [[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]
                self.range = 3
        else:
            self.data = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]
            self.range = 4
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
        # Загрузка рекордного счёта.
        if os.path.exists("score.txt"):
            with open("score.txt", "r") as f:
                self.bstScore = int(f.read())


    def paintEvent(self, event) -> None:
        """
        Событие отрисовки.
        :param event: event
        :return: None
        """
        qp = QPainter()
        qp.begin(self)
        self.drawGameGraph(qp)
        qp.end()

    def keyPressEvent(self, event) -> None:
        """
        Действие при нажатии клавиш.
        :param event: event
        :return: None
        """
        keyCode = event.key()
        ret = False
        if keyCode == Qt.Key_Left:
            ret = self.move("Left")
        elif keyCode == Qt.Key_Right:
            ret = self.move("Right")
        elif keyCode == Qt.Key_Up:
            ret = self.move("Up")
        elif keyCode == Qt.Key_Down:
            ret = self.move("Down")
        else:
            pass

        if ret:
            self.repaint()

    def closeEvent(self, event) -> None:
        """
        Сохранение рекорда.
        :param event: event
        :return: None
        """
        with open("score.txt", "w") as f:
            f.write(str(self.bstScore))

    def drawGameGraph(self, qp) -> None:
        """
        Рисуем игровую графику
        :param qp: QPainter()
        :return: None
        """
        self.drawLog(qp)
        self.drawLabel(qp)
        self.drawScore(qp)
        self.drawBackground(qp)
        self.drawTiles(qp)

    def drawScore(self, qp) -> None:
        """
        Отображение счёта.
        :param qp: QPainter()
        :return: None
        """
        qp.setFont(self.lbFont)
        fontsize = self.lbFont.pointSize()
        scoreLabelSize = len(u"SCORE") * fontsize
        bestLabelSize = len(u"BEST") * fontsize
        currentScoreBoardMinWidht = 15 * 2 + scoreLabelSize  # Минимальная ширина столбца SCORE
        bestScoreBoardMinWidht = 15 * 2 + bestLabelSize  # Минимальная ширина столбца BEST SCORE
        currentScoreSize = len(str(self.curScore)) * fontsize
        bestScoreSize = len(str(self.bstScore)) * fontsize
        currentScoreBoardNedW = 10 + currentScoreSize
        bestScoreBoardNedW = 10 + bestScoreSize
        currentScoreBoardW = max(currentScoreBoardMinWidht, currentScoreBoardNedW)
        bestScoreBoardW = max(bestScoreBoardMinWidht, bestScoreBoardNedW)
        qp.setBrush(QColor(187, 173, 160))
        qp.setPen(QColor(187, 173, 160))
        qp.drawRect(505 - 15 - bestScoreBoardW, 40, bestScoreBoardW, 50)
        qp.drawRect(505 - 15 - bestScoreBoardW - 5 - currentScoreBoardW, 40, currentScoreBoardW, 50)

        bestLabelRect = QRect(505 - 15 - bestScoreBoardW, 40, bestScoreBoardW, 25)
        bestScoreRect = QRect(505 - 15 - bestScoreBoardW, 65, bestScoreBoardW, 25)
        scoreLabelRect = QRect(505 - 15 - bestScoreBoardW - 5 - currentScoreBoardW, 40, currentScoreBoardW, 25)
        curScoreRect = QRect(505 - 15 - bestScoreBoardW - 5 - currentScoreBoardW, 65, currentScoreBoardW, 25)

        qp.setPen(QColor(238, 228, 218))
        qp.drawText(bestLabelRect, Qt.AlignCenter, u"BEST")
        qp.drawText(scoreLabelRect, Qt.AlignCenter, u"SCORE")

        qp.setPen(QColor(255, 255, 255))
        qp.drawText(bestScoreRect, Qt.AlignCenter, str(self.bstScore))
        qp.drawText(curScoreRect, Qt.AlignCenter, str(self.curScore))

    def drawBackground(self, qp) -> None:
        """
        Отображение фона.
        :param qp: QPainter()
        :return: None
        """
        col = QColor(187, 173, 160)
        qp.setPen(col)

        qp.setBrush(QColor(187, 173, 160))
        if self.range == 4:
            qp.drawRect(15, 150, 475, 475)  # Отрисовка игрового поля
        elif self.range == 3:
            qp.drawRect(15, 150, 360, 360)
        elif self.range == 5:
            qp.drawRect(15, 150, 590, 590)

    def drawLog(self, qp) -> None:
        """
        Отображение названия игры.
        :param qp: QPainter()
        :return: None
        """
        pen = QPen(QColor(255, 93, 29), 15)
        qp.setFont(self.lgFont)
        qp.setPen(pen)
        qp.drawText(QRect(10, 0, 150, 130), Qt.AlignCenter, "2048")

    def drawLabel(self, qp) -> None:
        """
        Отображение информации как играть.
        :param qp: QPainter()
        :return: None
        """
        qp.setFont(self.lbFont)
        qp.setPen(QColor(119, 110, 101))
        qp.drawText(5, 134, u"Совмещайте таблички с одинаковыми числами, чтобы получить 2048!")
        qp.drawText(5, 760, u"Как играть:")
        qp.drawText(15, 780, u"Используйте клавиши со стрелками, чтобы переместить \n квадрат")
        qp.drawText(15, 800, u"Два квадрата с одинаковым числом объединяются в один")

    def drawTiles(self, qp) -> None:
        """
        Отрисовка игрового фона.
        :param qp: QPainter()
        :return: None
        """
        qp.setFont(self.nmFont)
        for row in range(self.range):
            for col in range(self.range):
                value = self.data[row][col]
                color = self.colors[value]

                qp.setPen(QColor(*color))
                qp.setBrush(QColor(*color))
                qp.drawRect(30 + col * 115, 165 + row * 115, 100, 100)  # Отрисовка табличек с цифрами
                size = self.nmFont.pointSize() * len(str(value))  # Получить длину числа, отображаемого текущим шрифтом
                # Изменение размера шрифта в соответствии с длинной строки
                while size > 100 - 15 * 2:
                    self.nmFont = QFont('Arial', self.nmFont.pointSize() * 4 // 5)
                    qp.setFont(self.nmFont)
                    size = self.nmFont.pointSize() * len(str(value))  # Получить длину строки с числом, отображаемым текущим шрифтом
                print("[%d][%d]: value[%d] weight: %d" % (row, col, value, size))

                # Отображение ненулевых значений
                if value == 2 or value == 4:
                    qp.setPen(QColor(119, 110, 101))  # Установка цвета фона для чисел 2 и 4
                else:
                    qp.setPen(QColor(255, 255, 255))  # Установка цвета фона для других чисел
                if value != 0:
                    rect = QRect(30 + col * 115, 165 + row * 115, 100, 100)
                    qp.drawText(rect, Qt.AlignCenter, str(value))

    def putTile(self) -> bool:
        """
        Заполнение пустой позиции 2 или 4.
        :return: bool
        """
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

    def merge(self, row) -> list:
        """
        Объединение строк и столбцов.
        :param row:
        :return: list
        """
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

    def slideUpDown(self, isUp) -> bool:
        """
        Перемещение сетки с числами вверх - вниз.
        :param isUp: True если нажата кнопка вверх, False если нажата кнопка вниз
        :return: bool
        """
        numRows = len(self.data)
        numCols = len(self.data[0])
        oldData = copy.deepcopy(self.data)

        for col in range(numCols):
            cvl = []
            for row in range(numRows):
                if self.data[row][col] != 0:
                    cvl.append(self.data[row][col])  # Извлекаем ненулевые элементы в столбце

            if len(cvl) >= 2:
                cvl = self.merge(cvl)  # Объединение одинаковых чисел

            # Заполнение 0 в соответствии с направлением движения
            for i in range(numRows - len(cvl)):
                if isUp:
                    cvl.append(0)
                else:
                    cvl.insert(0, 0)
            for row in range(numRows):
                self.data[row][col] = cvl[row]

        return oldData != self.data  # Возвращаем, изменились ли данные

    def slideLeftRight(self, isLeft) -> bool:
        """
        Перемещение сетки с числами вправо - влево.
        :param isLeft: True если нажата кнопка налево, False если нажата кнопка направо
        :return: bool
        """
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
            for col in range(numCols):
                self.data[row][col] = rvl[col]

        return oldData != self.data

    def move(self, direction) -> bool:
        """
        Перемещение числовой сетки.
        :param direction: self.move
        :return: bool
        """
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

        self.putTile()  # Заполнение пустой позиции.
        if self.curScore > self.bstScore:
            self.bstScore = self.curScore

        if self.isGameOver():
            button = QMessageBox.warning(self, "Warning", u"Игра окончена. Заново?",
                                         QMessageBox.Ok | QMessageBox.No,
                                         QMessageBox.Ok)

            if button == QMessageBox.Ok:
                self.initGameOpt()
                bstScore = self.bstScore
                self.initGameData()
                self.bstScore = bstScore
                return True
            else:
                return False
        else:
            return True

    def isGameOver(self) -> bool:
        """
        Определение возможности продолжить игру.
        :return: bool
        """
        copyData = copy.deepcopy(self.data)  # Сначала временно сохраняем значения данных
        curScore = self.curScore

        flag = False
        if not self.slideUpDown(True) and not self.slideUpDown(False) and \
                not self.slideLeftRight(True) and not self.slideLeftRight(False):
            flag = True  # Больше не может двигаться во всех направлениях
        self.curScore = curScore
        if not flag:
            self.data = copyData  # Все еще можно переместить, а затем восстановить исходные данные
        return flag


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    form = GameForm()
    form.show()
    sys.exit(app.exec_())