import sys

from PyQt5 import QtWidgets

from gui import Gui
from controller import Controller


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = Gui()
    controller = Controller(window)

    controller.time_signal.connect(window.update_timer)
    controller.player_number_signal.connect(window.update_player_color)
    controller.player_symbol_signal.connect(window.update_player_symbol)
    controller.game_result_signal.connect(window.show_game_result)

    window.finish_signal.connect(controller.finish_game)

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
