# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_window_mode.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 573)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(1000, 800))
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setLineWidth(8)
        self.label.setMidLineWidth(8)
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(1)

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.CPU_info = QPlainTextEdit(self.centralwidget)
        self.CPU_info.setObjectName(u"CPU_info")
        self.CPU_info.setEnabled(False)
        self.CPU_info.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout.addWidget(self.CPU_info)

        self.disks_info = QListWidget(self.centralwidget)
        self.disks_info.setObjectName(u"disks_info")

        self.verticalLayout.addWidget(self.disks_info)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setLineWidth(8)
        self.label_2.setMidLineWidth(8)
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setValue(1)

        self.horizontalLayout_2.addWidget(self.spinBox_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.processes = QWidget()
        self.processes.setObjectName(u"processes")
        self.horizontalLayout_3 = QHBoxLayout(self.processes)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.processes_view = QTableView(self.processes)
        self.processes_view.setObjectName(u"processes_view")
        self.processes_view.horizontalHeader().setCascadingSectionResizes(True)
        self.processes_view.horizontalHeader().setHighlightSections(False)
        self.processes_view.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_3.addWidget(self.processes_view)

        self.tabWidget.addTab(self.processes, "")
        self.services = QWidget()
        self.services.setObjectName(u"services")
        self.horizontalLayout_4 = QHBoxLayout(self.services)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.services_view = QTableView(self.services)
        self.services_view.setObjectName(u"services_view")

        self.horizontalLayout_4.addWidget(self.services_view)

        self.tabWidget.addTab(self.services, "")
        self.tasks = QWidget()
        self.tasks.setObjectName(u"tasks")
        self.verticalLayout_3 = QVBoxLayout(self.tasks)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget = QTableWidget(self.tasks)
        self.tableWidget.setObjectName(u"tableWidget")
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)


        self.verticalLayout_3.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tasks, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 775, 22))
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
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_3.addAction(self.action_2)
        self.menu_3.addAction(self.action_3)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u043f\u0435\u0442\u0447\u0435\u0440 \u0437\u0430\u0434\u0430\u0447", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.processes), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.services), QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tasks), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440", None))
    # retranslateUi

