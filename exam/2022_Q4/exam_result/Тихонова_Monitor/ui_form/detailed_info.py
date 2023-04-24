# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailed_info.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.action_9 = QAction(MainWindow)
        self.action_9.setObjectName(u"action_9")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.processes = QWidget()
        self.processes.setObjectName(u"processes")
        self.verticalLayout_3 = QVBoxLayout(self.processes)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.processes)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        self.tabWidget.addTab(self.processes, "")
        self.tab_services = QWidget()
        self.tab_services.setObjectName(u"tab_services")
        self.verticalLayout_4 = QVBoxLayout(self.tab_services)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableView_2 = QTableView(self.tab_services)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_4.addWidget(self.tableView_2)

        self.tabWidget.addTab(self.tab_services, "")
        self.tasks_plan = QWidget()
        self.tasks_plan.setObjectName(u"tasks_plan")
        self.verticalLayout_5 = QVBoxLayout(self.tasks_plan)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableView_3 = QTableView(self.tasks_plan)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_5.addWidget(self.tableView_3)

        self.tabWidget.addTab(self.tasks_plan, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menu_2)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu_3.addAction(self.action_8)
        self.menu_3.addAction(self.action_9)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u043f\u0435\u0442\u0447\u0435\u0440 \u0437\u0430\u0434\u0430\u0447", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u0435\u0439\u0447\u0430\u0441", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044b\u0447\u043d\u0430\u044f", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u043a\u0430\u044f", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0437\u043a\u0430\u044f", None))
        self.action_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.processes), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_services), QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0436\u0431\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tasks_plan), QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a \u0437\u0430\u0434\u0430\u0447", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None))
    # retranslateUi

