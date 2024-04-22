# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'a_add_ui_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolBox, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1199, 834)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(924, 705))
        self.action_Qt = QAction(MainWindow)
        self.action_Qt.setObjectName(u"action_Qt")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        font = QFont()
        font.setPointSize(12)
        self.action_3.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_14 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1199, 783))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font)

        self.verticalLayout_9.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font)

        self.verticalLayout_9.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font)

        self.verticalLayout_9.addWidget(self.radioButton_3)


        self.horizontalLayout_6.addWidget(self.groupBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)

        self.verticalLayout_8.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)

        self.verticalLayout_8.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font)

        self.verticalLayout_8.addWidget(self.checkBox_3)


        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.toolBox = QToolBox(self.tab)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(330, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 195, 178))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.page)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_2.addWidget(self.lineEdit_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"QLineEdit")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 472, 453))
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textEdit = QTextEdit(self.page_3)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_6.addWidget(self.textEdit)

        self.toolBox.addItem(self.page_3, u"QTextEdit")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 109, 109))
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.plainTextEdit = QPlainTextEdit(self.page_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_7.addWidget(self.plainTextEdit)

        self.toolBox.addItem(self.page_4, u"QPlainTextEdit")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 510, 318))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.calendarWidget = QCalendarWidget(self.page_2)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_5.addWidget(self.calendarWidget)

        self.toolBox.addItem(self.page_2, u"QCalendarWidget")

        self.horizontalLayout_8.addWidget(self.toolBox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonOpen = QPushButton(self.tab)
        self.pushButtonOpen.setObjectName(u"pushButtonOpen")

        self.horizontalLayout.addWidget(self.pushButtonOpen)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButtonAccept = QPushButton(self.tab)
        self.pushButtonAccept.setObjectName(u"pushButtonAccept")

        self.horizontalLayout.addWidget(self.pushButtonAccept)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.groupBox_4 = QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setMaximumSize(QSize(16777215, 181))
        font1 = QFont()
        font1.setPointSize(10)
        self.groupBox_4.setFont(font1)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(160, 0))
        self.label_5.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_5)

        self.lineEditOrbita = QLineEdit(self.groupBox_4)
        self.lineEditOrbita.setObjectName(u"lineEditOrbita")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEditOrbita.sizePolicy().hasHeightForWidth())
        self.lineEditOrbita.setSizePolicy(sizePolicy2)
        self.lineEditOrbita.setMaximumSize(QSize(80, 16777215))
        self.lineEditOrbita.setFont(font1)
        self.lineEditOrbita.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.lineEditOrbita)


        self.verticalLayout_18.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(160, 0))
        self.label_6.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.lineEditSpeedRotation = QLineEdit(self.groupBox_4)
        self.lineEditSpeedRotation.setObjectName(u"lineEditSpeedRotation")
        sizePolicy2.setHeightForWidth(self.lineEditSpeedRotation.sizePolicy().hasHeightForWidth())
        self.lineEditSpeedRotation.setSizePolicy(sizePolicy2)
        self.lineEditSpeedRotation.setMaximumSize(QSize(80, 16777215))
        self.lineEditSpeedRotation.setFont(font1)
        self.lineEditSpeedRotation.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEditSpeedRotation)


        self.verticalLayout_18.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMinimumSize(QSize(160, 0))
        self.label_18.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_18)

        self.lineEditSpeedSA = QLineEdit(self.groupBox_4)
        self.lineEditSpeedSA.setObjectName(u"lineEditSpeedSA")
        sizePolicy2.setHeightForWidth(self.lineEditSpeedSA.sizePolicy().hasHeightForWidth())
        self.lineEditSpeedSA.setSizePolicy(sizePolicy2)
        self.lineEditSpeedSA.setMaximumSize(QSize(80, 16777215))
        self.lineEditSpeedSA.setFont(font1)
        self.lineEditSpeedSA.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.lineEditSpeedSA)


        self.verticalLayout_18.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_26 = QLabel(self.groupBox_4)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)
        self.label_26.setMinimumSize(QSize(160, 0))
        self.label_26.setFont(font1)

        self.horizontalLayout_30.addWidget(self.label_26)

        self.lineEdit_11 = QLineEdit(self.groupBox_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy2.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy2)
        self.lineEdit_11.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_11.setFont(font1)
        self.lineEdit_11.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.lineEdit_11)


        self.verticalLayout_18.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)
        self.label_27.setMinimumSize(QSize(160, 0))
        self.label_27.setFont(font1)

        self.horizontalLayout_31.addWidget(self.label_27)

        self.lineEdit_12 = QLineEdit(self.groupBox_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy2.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy2)
        self.lineEdit_12.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_12.setFont(font1)
        self.lineEdit_12.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.lineEdit_12)


        self.verticalLayout_18.addLayout(self.horizontalLayout_31)


        self.horizontalLayout_37.addWidget(self.groupBox_4)

        self.groupBox_10 = QGroupBox(self.groupBox_5)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMaximumSize(QSize(16777215, 181))
        self.groupBox_10.setFont(font1)
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_28 = QLabel(self.groupBox_10)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(120, 0))
        self.label_28.setFont(font1)

        self.horizontalLayout_32.addWidget(self.label_28)

        self.textEdit_6 = QTextEdit(self.groupBox_10)
        self.textEdit_6.setObjectName(u"textEdit_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy3)
        self.textEdit_6.setMinimumSize(QSize(85, 0))
        self.textEdit_6.setMaximumSize(QSize(90, 22))
        font2 = QFont()
        font2.setPointSize(11)
        self.textEdit_6.setFont(font2)
        self.textEdit_6.setFrameShape(QFrame.WinPanel)
        self.textEdit_6.setFrameShadow(QFrame.Sunken)
        self.textEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_32.addWidget(self.textEdit_6)


        self.verticalLayout_19.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_29 = QLabel(self.groupBox_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(120, 0))
        self.label_29.setFont(font1)

        self.horizontalLayout_33.addWidget(self.label_29)

        self.textEdit_7 = QTextEdit(self.groupBox_10)
        self.textEdit_7.setObjectName(u"textEdit_7")
        sizePolicy3.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy3)
        self.textEdit_7.setMinimumSize(QSize(85, 0))
        self.textEdit_7.setMaximumSize(QSize(90, 22))
        self.textEdit_7.setFont(font2)
        self.textEdit_7.setFrameShape(QFrame.WinPanel)
        self.textEdit_7.setFrameShadow(QFrame.Sunken)
        self.textEdit_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_33.addWidget(self.textEdit_7)


        self.verticalLayout_19.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_30 = QLabel(self.groupBox_10)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(120, 0))
        self.label_30.setFont(font1)

        self.horizontalLayout_34.addWidget(self.label_30)

        self.textEdit_8 = QTextEdit(self.groupBox_10)
        self.textEdit_8.setObjectName(u"textEdit_8")
        sizePolicy3.setHeightForWidth(self.textEdit_8.sizePolicy().hasHeightForWidth())
        self.textEdit_8.setSizePolicy(sizePolicy3)
        self.textEdit_8.setMinimumSize(QSize(85, 0))
        self.textEdit_8.setMaximumSize(QSize(90, 22))
        self.textEdit_8.setFont(font2)
        self.textEdit_8.setFrameShape(QFrame.WinPanel)
        self.textEdit_8.setFrameShadow(QFrame.Sunken)
        self.textEdit_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_34.addWidget(self.textEdit_8)


        self.verticalLayout_19.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_31 = QLabel(self.groupBox_10)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(120, 0))
        self.label_31.setFont(font1)

        self.horizontalLayout_35.addWidget(self.label_31)

        self.textEdit_9 = QTextEdit(self.groupBox_10)
        self.textEdit_9.setObjectName(u"textEdit_9")
        sizePolicy3.setHeightForWidth(self.textEdit_9.sizePolicy().hasHeightForWidth())
        self.textEdit_9.setSizePolicy(sizePolicy3)
        self.textEdit_9.setMinimumSize(QSize(85, 0))
        self.textEdit_9.setMaximumSize(QSize(90, 22))
        self.textEdit_9.setFont(font2)
        self.textEdit_9.setFrameShape(QFrame.WinPanel)
        self.textEdit_9.setFrameShadow(QFrame.Sunken)
        self.textEdit_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_35.addWidget(self.textEdit_9)


        self.verticalLayout_19.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_32 = QLabel(self.groupBox_10)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(120, 0))
        self.label_32.setFont(font1)

        self.horizontalLayout_36.addWidget(self.label_32)

        self.textEdit_10 = QTextEdit(self.groupBox_10)
        self.textEdit_10.setObjectName(u"textEdit_10")
        sizePolicy3.setHeightForWidth(self.textEdit_10.sizePolicy().hasHeightForWidth())
        self.textEdit_10.setSizePolicy(sizePolicy3)
        self.textEdit_10.setMinimumSize(QSize(85, 0))
        self.textEdit_10.setMaximumSize(QSize(90, 22))
        self.textEdit_10.setFont(font2)
        self.textEdit_10.setFrameShape(QFrame.WinPanel)
        self.textEdit_10.setFrameShadow(QFrame.Sunken)
        self.textEdit_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_36.addWidget(self.textEdit_10)


        self.verticalLayout_19.addLayout(self.horizontalLayout_36)


        self.horizontalLayout_37.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.groupBox_5)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMaximumSize(QSize(16777215, 181))
        self.groupBox_11.setFont(font1)
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tableWidget = QTableWidget(self.groupBox_11)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        brush = QBrush(QColor(0, 255, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setBackground(brush);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setBackground(brush);
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setBackground(brush);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_20.addWidget(self.tableWidget)


        self.horizontalLayout_37.addWidget(self.groupBox_11)


        self.verticalLayout_21.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.groupBox_9 = QGroupBox(self.groupBox_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMaximumSize(QSize(16777215, 185))
        self.groupBox_9.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.groupBox_9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_19 = QLabel(self.groupBox_9)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_16.addWidget(self.label_19)

        self.textEdit_2 = QTextEdit(self.groupBox_9)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 22))
        self.textEdit_2.setFrameShape(QFrame.WinPanel)
        self.textEdit_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.textEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_20 = QLabel(self.groupBox_9)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_17.addWidget(self.label_20)

        self.textEdit_3 = QTextEdit(self.groupBox_9)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 22))
        self.textEdit_3.setFrameShape(QFrame.WinPanel)
        self.textEdit_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.textEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_21 = QLabel(self.groupBox_9)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_23.addWidget(self.label_21)

        self.textEdit_4 = QTextEdit(self.groupBox_9)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(16777215, 22))
        self.textEdit_4.setFrameShape(QFrame.WinPanel)
        self.textEdit_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_23.addWidget(self.textEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_22 = QLabel(self.groupBox_9)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_24.addWidget(self.label_22)

        self.textEdit_5 = QTextEdit(self.groupBox_9)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(16777215, 22))
        self.textEdit_5.setFrameShape(QFrame.WinPanel)
        self.textEdit_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_24.addWidget(self.textEdit_5)


        self.verticalLayout.addLayout(self.horizontalLayout_24)


        self.verticalLayout_16.addWidget(self.groupBox_9)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font1)
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSlider = QSlider(self.groupBox_7)
        self.verticalSlider.setObjectName(u"verticalSlider")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy4)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSlider)

        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)


        self.horizontalLayout_12.addLayout(self.verticalLayout_3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSlider_2 = QSlider(self.groupBox_7)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        sizePolicy4.setHeightForWidth(self.verticalSlider_2.sizePolicy().hasHeightForWidth())
        self.verticalSlider_2.setSizePolicy(sizePolicy4)
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.verticalLayout_12.addWidget(self.verticalSlider_2)

        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_12.addWidget(self.label_8)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSlider_3 = QSlider(self.groupBox_7)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        sizePolicy4.setHeightForWidth(self.verticalSlider_3.sizePolicy().hasHeightForWidth())
        self.verticalSlider_3.setSizePolicy(sizePolicy4)
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.verticalLayout_13.addWidget(self.verticalSlider_3)

        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(77, 13))

        self.verticalLayout_13.addWidget(self.label_15)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSlider_4 = QSlider(self.groupBox_7)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        sizePolicy4.setHeightForWidth(self.verticalSlider_4.sizePolicy().hasHeightForWidth())
        self.verticalSlider_4.setSizePolicy(sizePolicy4)
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.verticalLayout_14.addWidget(self.verticalSlider_4)

        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_14.addWidget(self.label_16)


        self.horizontalLayout_12.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSlider_5 = QSlider(self.groupBox_7)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        sizePolicy4.setHeightForWidth(self.verticalSlider_5.sizePolicy().hasHeightForWidth())
        self.verticalSlider_5.setSizePolicy(sizePolicy4)
        self.verticalSlider_5.setOrientation(Qt.Vertical)

        self.verticalLayout_15.addWidget(self.verticalSlider_5)

        self.label_17 = QLabel(self.groupBox_7)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_15.addWidget(self.label_17)


        self.horizontalLayout_12.addLayout(self.verticalLayout_15)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)


        self.verticalLayout_16.addWidget(self.groupBox_7)


        self.horizontalLayout_25.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font1)
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.progressBar = QProgressBar(self.groupBox_6)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy4.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy4)
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Vertical)

        self.verticalLayout_22.addWidget(self.progressBar)

        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_22.addWidget(self.label_9)


        self.horizontalLayout_19.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.progressBar_2 = QProgressBar(self.groupBox_6)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy4.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy4)
        self.progressBar_2.setValue(78)
        self.progressBar_2.setOrientation(Qt.Vertical)

        self.verticalLayout_23.addWidget(self.progressBar_2)

        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_23.addWidget(self.label_10)


        self.horizontalLayout_19.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.progressBar_3 = QProgressBar(self.groupBox_6)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy4.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy4)
        self.progressBar_3.setMinimum(0)
        self.progressBar_3.setValue(100)
        self.progressBar_3.setOrientation(Qt.Vertical)

        self.verticalLayout_24.addWidget(self.progressBar_3)

        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_24.addWidget(self.label_11)


        self.horizontalLayout_19.addLayout(self.verticalLayout_24)


        self.verticalLayout_17.addWidget(self.groupBox_6)

        self.groupBox_3 = QGroupBox(self.groupBox_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font1)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_13 = QPushButton(self.groupBox_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(75, 75))
        self.pushButton_13.setMaximumSize(QSize(75, 75))
        font3 = QFont()
        font3.setPointSize(20)
        self.pushButton_13.setFont(font3)

        self.horizontalLayout_22.addWidget(self.pushButton_13)


        self.verticalLayout_28.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(75, 75))
        self.pushButton_6.setMaximumSize(QSize(75, 75))
        self.pushButton_6.setFont(font3)

        self.horizontalLayout_9.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(75, 75))
        self.pushButton_5.setMaximumSize(QSize(75, 75))
        self.pushButton_5.setFont(font3)

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(75, 75))
        self.pushButton_4.setMaximumSize(QSize(75, 75))
        self.pushButton_4.setFont(font3)

        self.horizontalLayout_9.addWidget(self.pushButton_4)


        self.verticalLayout_28.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_15.addLayout(self.verticalLayout_28)


        self.verticalLayout_17.addWidget(self.groupBox_3)


        self.horizontalLayout_25.addLayout(self.verticalLayout_17)


        self.verticalLayout_21.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_18.addWidget(self.groupBox_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_14.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1199, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.action)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_Qt)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Qt.setText(QCoreApplication.translate("MainWindow", u"\u041e Qt", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"QRadioButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton 1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton 2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton 3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"QCheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0443 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"QLineEdit", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043f\u043e\u043b\u0443\u0436\u0438\u0440\u043d\u044b\u043c</span>. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043a\u0443\u0440\u0441\u0438\u0432\u043e\u043c.</span><br />\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u043d\u043e"
                        " <span style=\" text-decoration: underline;\">\u043f\u043e\u0434\u0447\u0435\u0440\u043a\u043d\u0443\u0442\u044c</span>. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c <span style=\" vertical-align:super;\">\u043d\u0430\u0434\u0441\u0442\u0440\u043e\u0447\u043d\u044b\u043c</span>. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c <span style=\" vertical-align:sub;\">\u043f\u043e\u0434\u0441\u0442\u0440\u043e\u0447\u043d\u044b\u043c</span>.</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"QTextEdit", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in semper nulla, sed feugiat turpis. Cras blandit suscipit pharetra. Aliquam vitae mollis magna. Curabitur a tortor nec risus venenatis vehicula. Proin a metus eu arcu tempus iaculis ut sed dui. Sed bibendum convallis tellus, eu viverra arcu pulvinar sit amet. Proin vitae lorem in tellus imperdiet rhoncus sed eget elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec efficitur molestie elit ac facilisis. Morbi ac volutpat dui, ut scelerisque lectus. Nunc dapibus eros sem, vitae molestie augue bibendum eu. Ut neque diam, ornare eu ligula eget, sagittis faucibus augue. Mauris tristique volutpat porta. Nunc eget nulla in leo viverra mattis. Proin malesuada enim quis scelerisque finibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"QPlainTextEdit", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"QCalendarWidget", None))
        self.pushButtonOpen.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButtonAccept.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u043e\u043b\u044c \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u041a\u0410", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043e\u0440\u0431\u0438\u0442\u044b", None))
        self.lineEditOrbita.setText(QCoreApplication.translate("MainWindow", u"10256 \u043a\u043c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f", None))
        self.lineEditSpeedRotation.setText(QCoreApplication.translate("MainWindow", u"0,2 \u043c/\u0441", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u041a\u0410", None))
        self.lineEditSpeedSA.setText(QCoreApplication.translate("MainWindow", u"364 \u043a\u043c/\u0447", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"60,00000", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"30,00000", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#efb328;\">22 \u0421</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#50ff05;\">\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#50ff05;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#50ff05;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#50ff05;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u043e\u0432", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0435\u0441\u0441", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"36,6", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"140/70", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"36,8", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"120/60", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"36,5", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"130/70", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#fdc149;\">\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0430\u0440\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043f\u043b\u0438\u0432\u043e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0430\u043d\u0435\u0432\u0440\u043e\u0432\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

