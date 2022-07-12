from PySide2 import QtWidgets

import frontend as wt
import backend as app


def main():
    """- Точка входа """
    application = QtWidgets.QApplication()
    application.setStyle('Windows')

    # wt.Application(app=app.Manager())
    win = wt.LevelApp(app=app.Manager())
    win.show()

    application.exec_()


if __name__ == '__main__':
    main()
