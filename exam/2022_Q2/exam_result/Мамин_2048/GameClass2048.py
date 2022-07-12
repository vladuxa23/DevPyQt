from random import randint

class Game2048(object):
    """
    Класс описывающий логику игры 2048 и её основные методы
    """

    def __init__(self, xn, yn):
        self.width = xn
        self.height = yn
        self.grid = []
        self.start = 0
        self.end = 0
        self.start_value = 0
        self.end_value = 0
        self.cnt = 0


        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append(0)
        self.add_one()

    def add_one(self) -> int:
        """
        Метод добавления в список рандомных значений
        :return:
        """
        not_filled = []
        random_values = [2, 4]
        for e in range(self.height):
            for j in range(self.width):
                if self.grid[e][j] == 0:
                    not_filled.append((e, j))
        random_cell = not_filled[randint(0, len(not_filled) - 1)]
        self.grid[random_cell[0]][random_cell[1]] = random_values[randint(0, len(random_values) - 1)]
        if len(not_filled) == 1:
            return self.check_gameover()
        return 0

    def check_gameover(self) -> int:
        """
        Метод определения финиша игры
        :return:
        """
        for i in range(self.height):
            for j in range(self.width-1):
                if self.grid[i][j] == self.grid[i][j+1]:
                    return 0
        for i in range(self.height-1):
            for j in range(self.width):
                if self.grid[i][j] == self.grid[i+1][j]:
                    return 0
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    return 0
        return -1

    def equal_value_1(self):
        self.grid[self.cnt][self.start] *= 2
        self.grid[self.cnt][self.end] = 0

    def equal_value_2(self):
        self.grid[self.cnt][self.start] = self.end_value
        self.grid[self.cnt][self.end] = 0

    def print_error(self):
        print('Произошла ошибка')
        print(f'start_value = {self.start_value}')
        print(f'end_value = {self.end_value}')
        print(f'start = {self.start}')
        print(f'end = {self.end}')
        return -1

    def swap_left(self) -> int:
        """
        Метод слияния полей в левую сторону
        :return:
        """

        edit = False
        point = 0
        for i in range(self.height):
            self.start, self.end, self.cnt = 0, 1, i
            while self.end < self.width:
                self.start_value = self.grid[i][self.start]
                self.end_value = self.grid[i][self.end]
                if self.start_value == self.end_value and self.start_value > 0:
                    self.equal_value_1()
                    point += self.grid[self.start][i]
                    edit = True
                    self.start += 1
                    self.end += 1
                elif self.start_value == 0 and self.end_value > 0:
                    self.equal_value_2()
                    edit = True
                    self.end += 1
                elif self.start_value == self.end_value == 0:
                    self.end += 1
                elif self.start_value > 0 and self.end_value == 0:
                    self.end += 1
                elif 0 < self.start_value != self.end_value > 0:
                    self.start += 1
                else:
                    self.print_error()
                while self.start >= self.end:
                    self.end += 1
        return self.add_one() + point if edit else self.check_gameover()

    def swap_right(self) -> int:
        """
        Метод слияния полей в правую сторону
        :return:
        """

        edit = False
        point = 0
        for u in range(self.height):
            self.start, self.end, self.cnt = self.width-1, self.width-2, u
            while self.end > -1:
                self.start_value = self.grid[u][self.start]
                self.end_value = self.grid[u][self.end]
                if self.start_value == self.end_value and self.start_value > 0:
                    self.equal_value_1()
                    point += self.grid[self.start][u]
                    edit = True
                    self.start -= 1
                    self.end -= 1
                elif self.start_value == 0 and self.end_value > 0:
                    self.equal_value_2()
                    edit = True
                    self.end -= 1
                elif self.start_value == self.end_value == 0:
                    self.end -= 1
                elif self.start_value > 0 and self.end_value == 0:
                    self.end -= 1
                elif 0 < self.start_value != self.end_value > 0:
                    self.start -= 1
                else:
                    self.print_error()
                while self.start <= self.end:
                    self.end -= 1
        return self.add_one() + point if edit else self.check_gameover()

    def swap_down(self) -> int:
        """
        Метод слияния полей вниз
        :return:
        """

        edit = False
        point = 0
        for l in range(self.width):
            self.start, self.end, self.cnt = self.height-1, self.height-2, l
            while self.end > -1:
                self.start_value = self.grid[l][self.start]
                self.end_value = self.grid[l][self.end]
                if self.start_value == self.end_value and self.start_value > 0:
                    self.equal_value_1()
                    point += self.grid[self.start][l]
                    edit = True
                    self.start -= 1
                    self.end -= 1
                elif self.start_value == 0 and self.end_value > 0:
                    self.equal_value_2()
                    edit = True
                    self.end -= 1
                elif self.start_value == self.end_value == 0:
                    self.end -= 1
                elif self.start_value > 0 and self.end_value == 0:
                    self.end -= 1
                elif 0 < self.start_value != self.end_value > 0:
                    self.start -= 1
                else:
                    self.print_error()
                while self.start <= self.end:
                    self.end -= 1
        return self.add_one() + point if edit else self.check_gameover()

    def swap_up(self) -> int:
        """
        Метод слияния полей вверх
        :return:
        """

        edit = False
        point = 0
        for i in range(self.width):
            self.start, self.end = 0, 1
            while self.end < self.height:
                self.start_value = self.grid[self.start][i]
                self.end_value = self.grid[self.end][i]
                if self.start_value == self.end_value and self.start_value > 0:
                    self.grid[self.start][i] *= 2
                    self.grid[self.end][i] = 0
                    point += self.grid[self.start][i]
                    edit = True
                    self.start += 1
                    self.end += 1
                elif self.start_value == 0 and self.end_value > 0:
                    self.grid[self.start][i] = self.end_value
                    self.grid[self.end][i] = 0
                    edit = True
                    self.end += 1
                elif self.start_value == self.end_value == 0:
                    self.end += 1
                elif self.start_value > 0 and self.end_value == 0:
                    self.end += 1
                elif 0 < self.start_value != self.end_value > 0:
                    self.start += 1
                else:
                    self.print_error()
                while self.start >= self.end:
                    self.end += 1
        return self.add_one() + point if edit else self.check_gameover()

    def __str__(self) -> str:
        """
        Метод str
        :return:
        """

        string_ = ''
        for i in range(self.height):
            for j in range(self.width):
                string_ += f'{self.grid[i][j]}  '
            string_ += '\n'
        return string_


if __name__ == '__main__':
    game = Game2048(4, 4)
    random_functions = [game.swap_right, game.swap_left, game.swap_up, game.swap_down]
    # for i in range(10):
    #     game.swap_down()
    game.swap_down()
    print(game)
    game.swap_left()
    print(game)
    game.swap_left()
    print(game)
    game.swap_right()
    print(game)
    game.swap_up()
    print(game)
    print('Конец игры')