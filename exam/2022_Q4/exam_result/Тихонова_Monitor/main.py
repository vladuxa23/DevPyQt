from logic.one_window_mode import Window

from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()