"""
Демонстрация применения флагов Qt.WindowType
"""

from PySide6 import QtWidgets, QtCore


class PreviewWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PreviewWindow, self).__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)

        self.closeButton = QtWidgets.QPushButton("&Close")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.closeButton)
        self.setLayout(layout)

        self.setWindowTitle("Preview")

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.closeButton.clicked.connect(self.close)

    def setWindowFlags(self, flags: QtCore.Qt.WindowType) -> None:
        """
        Установка флагов приложения

        :param flags: флаги для установки
        :return: None
        """

        super().setWindowFlags(flags)

        flag_type = (flags & QtCore.Qt.WindowType_Mask)

        if flag_type == QtCore.Qt.Window:
            text = "Qt.Window"
        elif flag_type == QtCore.Qt.Dialog:
            text = "Qt.Dialog"
        elif flag_type == QtCore.Qt.Sheet:
            text = "Qt.Sheet"
        elif flag_type == QtCore.Qt.Drawer:
            text = "Qt.Drawer"
        elif flag_type == QtCore.Qt.Popup:
            text = "Qt.Popup"
        elif flag_type == QtCore.Qt.Tool:
            text = "Qt.Tool"
        elif flag_type == QtCore.Qt.ToolTip:
            text = "Qt.ToolTip"
        elif flag_type == QtCore.Qt.SplashScreen:
            text = "Qt.SplashScreen"
        else:
            text = ""

        if flags & QtCore.Qt.MSWindowsFixedSizeDialogHint:
            text += "\n| Qt.MSWindowsFixedSizeDialogHint"
        if flags & QtCore.Qt.X11BypassWindowManagerHint:
            text += "\n| Qt.X11BypassWindowManagerHint"
        if flags & QtCore.Qt.FramelessWindowHint:
            text += "\n| Qt.FramelessWindowHint"
        if flags & QtCore.Qt.WindowTitleHint:
            text += "\n| Qt.WindowTitleHint"
        if flags & QtCore.Qt.WindowSystemMenuHint:
            text += "\n| Qt.WindowSystemMenuHint"
        if flags & QtCore.Qt.WindowMinimizeButtonHint:
            text += "\n| Qt.WindowMinimizeButtonHint"
        if flags & QtCore.Qt.WindowMaximizeButtonHint:
            text += "\n| Qt.WindowMaximizeButtonHint"
        if flags & QtCore.Qt.WindowCloseButtonHint:
            text += "\n| Qt.WindowCloseButtonHint"
        if flags & QtCore.Qt.WindowContextHelpButtonHint:
            text += "\n| Qt.WindowContextHelpButtonHint"
        if flags & QtCore.Qt.WindowShadeButtonHint:
            text += "\n| Qt.WindowShadeButtonHint"
        if flags & QtCore.Qt.WindowStaysOnTopHint:
            text += "\n| Qt.WindowStaysOnTopHint"
        if flags & QtCore.Qt.WindowStaysOnBottomHint:
            text += "\n| Qt.WindowStaysOnBottomHint"
        if flags & QtCore.Qt.CustomizeWindowHint:
            text += "\n| Qt.CustomizeWindowHint"

        self.textEdit.setPlainText(text)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.previewWindow = PreviewWindow(self)

        self.initUi()
        self.initSignals()

    def initUi(self):
        """
        Инициализация Ui
        :return:
        """

        self.createTypeGroupBox()
        self.createHintsGroupBox()

        self.quitButton = QtWidgets.QPushButton("&Quit")

        bottomLayout = QtWidgets.QHBoxLayout()
        bottomLayout.addStretch()
        bottomLayout.addWidget(self.quitButton)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.typeGroupBox)
        mainLayout.addWidget(self.hintsGroupBox)
        mainLayout.addLayout(bottomLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle("Window Flags")
        self.updatePreview()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.quitButton.clicked.connect(self.close)

    def updatePreview(self) -> None:
        """
        Установка флагов в окно Preview

        :return: None
        """

        flags = QtCore.Qt.WindowFlags()

        if self.windowRadioButton.isChecked():
            flags = QtCore.Qt.Window
        elif self.dialogRadioButton.isChecked():
            flags = QtCore.Qt.Dialog
        elif self.sheetRadioButton.isChecked():
            flags = QtCore.Qt.Sheet
        elif self.drawerRadioButton.isChecked():
            flags = QtCore.Qt.Drawer
        elif self.popupRadioButton.isChecked():
            flags = QtCore.Qt.Popup
        elif self.toolRadioButton.isChecked():
            flags = QtCore.Qt.Tool
        elif self.toolTipRadioButton.isChecked():
            flags = QtCore.Qt.ToolTip
        elif self.splashScreenRadioButton.isChecked():
            flags = QtCore.Qt.SplashScreen

        if self.msWindowsFixedSizeDialogCheckBox.isChecked():
            flags |= QtCore.Qt.MSWindowsFixedSizeDialogHint
        if self.x11BypassWindowManagerCheckBox.isChecked():
            flags |= QtCore.Qt.X11BypassWindowManagerHint
        if self.framelessWindowCheckBox.isChecked():
            flags |= QtCore.Qt.FramelessWindowHint
        if self.windowTitleCheckBox.isChecked():
            flags |= QtCore.Qt.WindowTitleHint
        if self.windowSystemMenuCheckBox.isChecked():
            flags |= QtCore.Qt.WindowSystemMenuHint
        if self.windowMinimizeButtonCheckBox.isChecked():
            flags |= QtCore.Qt.WindowMinimizeButtonHint
        if self.windowMaximizeButtonCheckBox.isChecked():
            flags |= QtCore.Qt.WindowMaximizeButtonHint
        if self.windowCloseButtonCheckBox.isChecked():
            flags |= QtCore.Qt.WindowCloseButtonHint
        if self.windowContextHelpButtonCheckBox.isChecked():
            flags |= QtCore.Qt.WindowContextHelpButtonHint
        if self.windowShadeButtonCheckBox.isChecked():
            flags |= QtCore.Qt.WindowShadeButtonHint
        if self.windowStaysOnTopCheckBox.isChecked():
            flags |= QtCore.Qt.WindowStaysOnTopHint
        if self.windowStaysOnBottomCheckBox.isChecked():
            flags |= QtCore.Qt.WindowStaysOnBottomHint
        if self.customizeWindowHintCheckBox.isChecked():
            flags |= QtCore.Qt.CustomizeWindowHint

        self.previewWindow.setWindowFlags(flags)

        self.previewWindow.show()

    def createTypeGroupBox(self) -> None:
        """
        Создание groupBox с типами окон

        :return: None
        """

        self.typeGroupBox = QtWidgets.QGroupBox("Type")

        self.windowRadioButton = self.createRadioButton("Window")
        self.dialogRadioButton = self.createRadioButton("Dialog")
        self.sheetRadioButton = self.createRadioButton("Sheet")
        self.drawerRadioButton = self.createRadioButton("Drawer")
        self.popupRadioButton = self.createRadioButton("Popup")
        self.toolRadioButton = self.createRadioButton("Tool")
        self.toolTipRadioButton = self.createRadioButton("Tooltip")
        self.splashScreenRadioButton = self.createRadioButton("Splash screen")
        self.windowRadioButton.setChecked(True)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.windowRadioButton, 0, 0)
        layout.addWidget(self.dialogRadioButton, 1, 0)
        layout.addWidget(self.sheetRadioButton, 2, 0)
        layout.addWidget(self.drawerRadioButton, 3, 0)
        layout.addWidget(self.popupRadioButton, 0, 1)
        layout.addWidget(self.toolRadioButton, 1, 1)
        layout.addWidget(self.toolTipRadioButton, 2, 1)
        layout.addWidget(self.splashScreenRadioButton, 3, 1)
        self.typeGroupBox.setLayout(layout)

    def createHintsGroupBox(self) -> None:
        """
        Создание groupBox со свойствами окон

        :return: None
        """

        self.hintsGroupBox = QtWidgets.QGroupBox("Hints")

        self.msWindowsFixedSizeDialogCheckBox = self.createCheckBox("MS Windows fixed size dialog")
        self.x11BypassWindowManagerCheckBox = self.createCheckBox("X11 bypass window manager")
        self.framelessWindowCheckBox = self.createCheckBox("Frameless window")
        self.windowTitleCheckBox = self.createCheckBox("Window title")
        self.windowSystemMenuCheckBox = self.createCheckBox("Window system menu")
        self.windowMinimizeButtonCheckBox = self.createCheckBox("Window minimize button")
        self.windowMaximizeButtonCheckBox = self.createCheckBox("Window maximize button")
        self.windowCloseButtonCheckBox = self.createCheckBox("Window close button")
        self.windowContextHelpButtonCheckBox = self.createCheckBox("Window context help button")
        self.windowShadeButtonCheckBox = self.createCheckBox("Window shade button")
        self.windowStaysOnTopCheckBox = self.createCheckBox("Window stays on top")
        self.windowStaysOnBottomCheckBox = self.createCheckBox("Window stays on bottom")
        self.customizeWindowHintCheckBox = self.createCheckBox("Customize window")

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.msWindowsFixedSizeDialogCheckBox, 0, 0)
        layout.addWidget(self.x11BypassWindowManagerCheckBox, 1, 0)
        layout.addWidget(self.framelessWindowCheckBox, 2, 0)
        layout.addWidget(self.windowTitleCheckBox, 3, 0)
        layout.addWidget(self.windowSystemMenuCheckBox, 4, 0)
        layout.addWidget(self.windowMinimizeButtonCheckBox, 0, 1)
        layout.addWidget(self.windowMaximizeButtonCheckBox, 1, 1)
        layout.addWidget(self.windowCloseButtonCheckBox, 2, 1)
        layout.addWidget(self.windowContextHelpButtonCheckBox, 3, 1)
        layout.addWidget(self.windowShadeButtonCheckBox, 4, 1)
        layout.addWidget(self.windowStaysOnTopCheckBox, 5, 1)
        layout.addWidget(self.windowStaysOnBottomCheckBox, 6, 1)
        layout.addWidget(self.customizeWindowHintCheckBox, 5, 0)
        self.hintsGroupBox.setLayout(layout)

    def createCheckBox(self, text: str) -> QtWidgets.QCheckBox:
        """
        Инициализация множественных checkBox

        :param text: текст на checkBox
        :return: QtWidgets.QCheckBox
        """

        checkBox = QtWidgets.QCheckBox(text)
        checkBox.clicked.connect(self.updatePreview)
        return checkBox

    def createRadioButton(self, text: str) -> QtWidgets.QRadioButton:
        """
        Инициализация множественных radioButton

        :param text: текст на radioButton
        :return: QtWidgets.QRadioButton
        """

        button = QtWidgets.QRadioButton(text)
        button.clicked.connect(self.updatePreview)
        return button


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    controller = Window()
    controller.show()

    app.exec()
