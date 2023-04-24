from datetime import datetime as dt

from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QPushButton


class Controller(QObject):

    time_signal = pyqtSignal(str)
    player_number_signal = pyqtSignal(str)
    player_symbol_signal = pyqtSignal(QObject, str)
    game_result_signal = pyqtSignal(str)

    game_timer = QTimer()

    SYMBOLS = {'1': 'X', '2': 'O'}
    VICTORY_COMBINATIONS = [[1, 2, 3],  # horizontal combination
                            [4, 5, 6],  # horizontal combination
                            [7, 8, 9],  # horizontal combination
                            [1, 4, 7],  # vertical combination
                            [2, 5, 8],  # vertical combination
                            [3, 6, 9],  # vertical combination
                            [1, 5, 9],  # diagonal combination
                            [3, 5, 7]]  # diagonal combination

    def __init__(self, gui):
        super().__init__()

        self.gui = gui

        self.counter = 0
        self.player = ''
        self.step_buffer = {'1': [], '2': []}
        self.game_started_flag = False
        self.start_game_time = None

        self.buttons = self.gui.findChildren(QPushButton)

        self._connect_signals()

    def _define_start_time(self) -> None:
        """
        Запуск таймера отсчета игрового времени
        :return: None
        """
        if not self.game_started_flag:
            self.start_game_time = dt.now()
            self.game_started_flag = True
            self.game_timer.start(1000)

    def _define_player(self) -> str:
        """
        Определение текущего и следующего по очереди игрока
        :return: Номер следующего по очереди игрока в формате str
        """
        self.player = '1' if self.counter % 2 == 0 else '2'
        next_player = '2' if self.counter % 2 == 0 else '1'
        self.counter += 1
        return next_player

    def _connect_signals(self):
        """
        Подключение сигналов
        :return: None
        """
        self.game_timer.timeout.connect(self._send_time)

        for btn in self.buttons:
            btn.clicked.connect(self._define_start_time)
            btn.clicked.connect(self._send_player_number)
            btn.clicked.connect(self._send_player_symbol)
            btn.clicked.connect(self._add_player_step)
            btn.clicked.connect(self._check_winner)

    def _send_time(self) -> None:
        """
        Отправляет игровое время в формате str
        :return: None
        """
        delta = dt.now() - self.start_game_time
        self.time_signal.emit(str(delta).split('.')[0])

    def _send_player_number(self) -> None:
        """
        Отправляет номер следующего игрока в формате str
        :return: None
        """
        next_player = self._define_player()
        self.player_number_signal.emit(next_player)

    def _send_player_symbol(self) -> None:
        """
        Отправляет символ, соответствующий игроку: 1 - Х, 2 - О
        :return: None
        """
        sender = self.sender()
        symbol = self.SYMBOLS.get(self.player)
        self.player_symbol_signal.emit(sender, symbol)

    def _add_player_step(self) -> None:
        """
        Сохраняет в буфер ход игрока
        :return: None
        """
        sender = self.sender()
        self.step_buffer[self.player].append(int(sender.accessibleName()))

    def _check_winner(self) -> None:
        """
        Проверка победной комбинации или ничьи
        :return: None
        """
        for combination in self.step_buffer.values():
            if sorted(combination) in self.VICTORY_COMBINATIONS:
                self.game_result_signal.emit(f'Player {self.player} wins!')

        if self.counter == 9:
            self.game_result_signal.emit('Tie!')

    def finish_game(self) -> None:
        """
        Обнуляет счетчик ходов, останавливает таймер игрового времени, сбрасывает флаг начала игры и очищает буфер ходов
        :return: None
        """
        self.counter = 0
        self.game_timer.stop()
        self.game_started_flag = False

        for buffer in self.step_buffer.values():
            buffer.clear()
