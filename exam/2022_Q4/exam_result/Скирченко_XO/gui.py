from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QPushButton

import form


class Gui(QWidget, form.Ui_TicTacToe):

    finish_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._default()

    def _default(self) -> None:
        """
        Устанавливает стартовые параметры окна
        :return: None
        """
        self.setWindowTitle('Tic-Tac-Toe')
        self.lbl_player_1.setStyleSheet('color: green')

    def update_timer(self, time_: str) -> None:
        """
        Обновляет значение времени в GUI
        :param time_: время
        :return: None
        """
        self.lbl_timer.setText(time_)

    def update_player_color(self, player_number: str) -> None:
        """
        Обновляет цвет активного игрова в GUI
        :param player_number: номер игрока
        :return: None
        """
        for player in self.players_frame.findChildren(QLabel):
            if player.accessibleName() == player_number:
                player.setStyleSheet('color: green')
            else:
                player.setStyleSheet('color: black')

    @staticmethod
    def update_player_symbol(object_, symbol: str) -> None:
        """
        Обновляет символ в поле, на которое нажимает игрок
        :param object_: поле (кнопка)
        :param symbol: символ
        :return: None
        """
        object_.setText(symbol)
        object_.setDisabled(True)

    def show_game_result(self, result_msg: str) -> None:
        """
        Отображает диалоговое окно с результатом игры
        :param result_msg: сообщение для отображения
        :return: None
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(result_msg)
        msg_box.setWindowTitle('Game result')
        msg_box.exec()

        self._update_playground()

    def _update_playground(self) -> None:
        """
        Обновление игрового поля для повторной игры
        :return: None
        """
        for btn in self.findChildren(QPushButton):
            btn.setText('')
            btn.setEnabled(True)

        self.finish_signal.emit()
