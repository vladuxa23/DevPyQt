import random


class Game:
    """Класс описывающий игру 2048 и её основные методы"""
    def __init__(self):
        self.field = [[0 for _ in range(4)] for _ in range(4)]  # Инициализируем поле для игры.

    def print_field(self) -> None:   # Метод печатающий поле в консоль, нужен только в консольной версии игры.
        for line in self.field:
            print(line)
        print("-" * 12)

    def clear_fild(self) -> None:  # Метод создающий новое, чистое поле.
        self.field = [[0 for _ in range(4)] for _ in range(4)]

    def check_add(self) -> bool:  # Метод проверяющий наличие доступных для хода клеток.
        for line in self.field:
            if 0 in line:
                return True
        return False

    def check_win(self) -> bool:  # Метод проверяющий победил ли игрок.
        for line in self.field:
            if 32 in line:
                return True
        return False

    def add_two(self) -> None:  # Метод создающий список возможных клеток для добавления двойки и добавляющий её.
        list_of_moves = []
        for index_line, line in enumerate(self.field):
            for index_value, value in enumerate(line):
                if value == 0:
                    list_of_moves.append([index_line, index_value])
        place_for_add = list_of_moves[random.randint(0, len(list_of_moves) - 1)]
        self.field[place_for_add[0]][place_for_add[1]] = 2

    def tern_left(self, x=1) -> None:  # Метод осуществляющий поворот поля против часовой стрелки на 90 градусов x раз.
        for _ in range(x):
            new_field = [[], [], [], []]
            for line in self.field:
                for index_value, value in enumerate(line):
                    new_field[(len(self.field) - 1) - index_value].append(value)
            self.field = new_field

    def merge_left(self) -> None:  # Метод складывающий одинаковые значения не равные 0, в отсортированных списках.
        self.sort_for_merge()
        for index_line in range(4):
            for index_elem in range(3):
                if self.field[index_line][index_elem] == 0:
                    break
                if self.field[index_line][index_elem] == self.field[index_line][index_elem + 1]:
                    self.field[index_line][index_elem] *= 2
                    self.field[index_line].pop(index_elem + 1)
                    self.field[index_line].append(0)

    def merge_right(self) -> None:  # Метод правого слияния через повороты поля и левое слияние.
        self.tern_left(2)
        self.merge_left()
        self.tern_left(2)

    def merge_up(self) -> None:  # Метод верхнего слияния через повороты поля и левое слияние.
        self.tern_left()
        self.merge_left()
        self.tern_left(3)

    def merge_down(self) -> None:  # Метод нижнего слияния через повороты поля и левое слияние.
        self.tern_left(3)
        self.merge_left()
        self.tern_left()

    def sort_for_merge(self) -> None:  # Метод создающий отсортированную копию поля и заменяющий на неё поле.
        sorted_field = [[], [], [], []]
        for index_line, line in enumerate(self.field):
            count = 0
            for value in line:
                if value == 0:
                    sorted_field[index_line].append(0)
                else:
                    sorted_field[index_line].insert(count, value)
                    count += 1
        self.field = sorted_field

    def input_play(self, input_) -> None:  # Метод вызывающий слияние в сторону, выбранную игроком.
        if input_ == 'w':
            self.merge_up()
        if input_ == 's':
            self.merge_down()
        if input_ == 'a':
            self.merge_left()
        if input_ == 'd':
            self.merge_right()

    def show_score(self) -> int:  # Метод возвращающий максимальное значение на игровом поле.
        max_value = 0
        for line in self.field:
            for value in line:
                if value > max_value:
                    max_value = value
        return max_value

    @staticmethod
    def start():
        x = Game()
        print("Начинаем игру")
        while x.check_add():
            x.add_two()
            x.print_field()
            x.input_play(input())
            if x.check_win():
                print('Поздравляю!!!')
                break


if __name__ == '__main__':
    Game.start()
