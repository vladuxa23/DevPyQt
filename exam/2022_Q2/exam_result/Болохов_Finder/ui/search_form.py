# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide2.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QTableView, QTreeView,
    QVBoxLayout, QWidget, QAction)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1041, 893)
        self.exit_action = QAction(MainWindow)
        self.exit_action.setObjectName(u"exit_action")
        self.about_action = QAction(MainWindow)
        self.about_action.setObjectName(u"about_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.treeView = QTreeView(self.layoutWidget)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_3.addWidget(self.treeView)

        self.selectedDir_lineEdit = QLineEdit(self.layoutWidget)
        self.selectedDir_lineEdit.setObjectName(u"selectedDir_lineEdit")

        self.verticalLayout_3.addWidget(self.selectedDir_lineEdit)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.settingSearchLabel = QLabel(self.layoutWidget1)
        self.settingSearchLabel.setObjectName(u"settingSearchLabel")
        self.settingSearchLabel.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.settingSearchLabel)

        self.chooseSettingComboBox = QComboBox(self.layoutWidget1)
        self.chooseSettingComboBox.addItem("")
        self.chooseSettingComboBox.addItem("")
        self.chooseSettingComboBox.addItem("")
        self.chooseSettingComboBox.setObjectName(u"chooseSettingComboBox")

        self.verticalLayout.addWidget(self.chooseSettingComboBox)

        self.entringStringLabel = QLabel(self.layoutWidget1)
        self.entringStringLabel.setObjectName(u"entringStringLabel")
        self.entringStringLabel.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.entringStringLabel)

        self.entringStringlineEdit = QLineEdit(self.layoutWidget1)
        self.entringStringlineEdit.setObjectName(u"entringStringlineEdit")

        self.verticalLayout.addWidget(self.entringStringlineEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_4.addWidget(self.splitter)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_4.addWidget(self.tableView)

        self.startSearchpushButton = QPushButton(self.centralwidget)
        self.startSearchpushButton.setObjectName(u"startSearchpushButton")
        self.startSearchpushButton.setMinimumSize(QSize(150, 80))
        self.startSearchpushButton.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_4.addWidget(self.startSearchpushButton)

        self.stopSearchpushButton = QPushButton(self.centralwidget)
        self.stopSearchpushButton.setObjectName(u"stopSearchpushButton")
        self.stopSearchpushButton.setMinimumSize(QSize(150, 80))

        self.verticalLayout_4.addWidget(self.stopSearchpushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.mainMenumenubar = QMenuBar(MainWindow)
        self.mainMenumenubar.setObjectName(u"mainMenumenubar")
        self.mainMenumenubar.setGeometry(QRect(0, 0, 1041, 22))
        self.file_menu = QMenu(self.mainMenumenubar)
        self.file_menu.setObjectName(u"file_menu")
        self.help_menu = QMenu(self.mainMenumenubar)
        self.help_menu.setObjectName(u"help_menu")
        MainWindow.setMenuBar(self.mainMenumenubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.mainMenumenubar.addAction(self.file_menu.menuAction())
        self.mainMenumenubar.addAction(self.help_menu.menuAction())
        self.file_menu.addAction(self.exit_action)
        self.help_menu.addAction(self.about_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.exit_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.about_action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.settingSearchLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e:", None))
        self.chooseSettingComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043f\u043e \u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u044e", None))
        self.chooseSettingComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u043f\u043e \u0431\u0438\u043d\u0430\u0440\u043d\u044b\u043c \u0441\u0438\u0433\u043d\u0430\u0442\u0443\u0440\u0430\u043c", None))
        self.chooseSettingComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u043f\u043e \u0441\u0442\u0440\u043e\u043a\u0435", None))

        self.entringStringLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 ", None))
        self.startSearchpushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043f\u043e\u0438\u0441\u043a", None))
        self.stopSearchpushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.help_menu.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

