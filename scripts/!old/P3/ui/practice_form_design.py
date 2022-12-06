# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'practice_form_design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1116, 504)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.spinBoxTimerCount = QSpinBox(self.frame)
        self.spinBoxTimerCount.setObjectName(u"spinBoxTimerCount")

        self.horizontalLayout_2.addWidget(self.spinBoxTimerCount)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButtonStartTimer = QPushButton(self.frame)
        self.pushButtonStartTimer.setObjectName(u"pushButtonStartTimer")

        self.verticalLayout.addWidget(self.pushButtonStartTimer)

        self.pushButtonStopTimer = QPushButton(self.frame)
        self.pushButtonStopTimer.setObjectName(u"pushButtonStopTimer")

        self.verticalLayout.addWidget(self.pushButtonStopTimer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEditTimerEnd = QLineEdit(self.frame)
        self.lineEditTimerEnd.setObjectName(u"lineEditTimerEnd")
        self.lineEditTimerEnd.setMaximumSize(QSize(50, 16777215))
        self.lineEditTimerEnd.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEditTimerEnd)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 329, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.lineEditURL = QLineEdit(self.frame_2)
        self.lineEditURL.setObjectName(u"lineEditURL")
        self.lineEditURL.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.lineEditURL)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.spinBoxUrlCheckTime = QSpinBox(self.frame_2)
        self.spinBoxUrlCheckTime.setObjectName(u"spinBoxUrlCheckTime")
        self.spinBoxUrlCheckTime.setMinimum(5)
        self.spinBoxUrlCheckTime.setMaximum(6000)

        self.horizontalLayout_7.addWidget(self.spinBoxUrlCheckTime)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.pushButtonUrlCheckStart = QPushButton(self.frame_2)
        self.pushButtonUrlCheckStart.setObjectName(u"pushButtonUrlCheckStart")
        self.pushButtonUrlCheckStart.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButtonUrlCheckStart)

        self.pushButtonUrlCheckStop = QPushButton(self.frame_2)
        self.pushButtonUrlCheckStop.setObjectName(u"pushButtonUrlCheckStop")

        self.verticalLayout_2.addWidget(self.pushButtonUrlCheckStop)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.plainTextEditUrlCheckLog = QPlainTextEdit(self.frame_2)
        self.plainTextEditUrlCheckLog.setObjectName(u"plainTextEditUrlCheckLog")
        self.plainTextEditUrlCheckLog.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEditUrlCheckLog)

        self.verticalSpacer_2 = QSpacerItem(20, 121, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_8.addWidget(self.label_16)

        self.spinBoxSystemInfoDelay = QSpinBox(self.frame_3)
        self.spinBoxSystemInfoDelay.setObjectName(u"spinBoxSystemInfoDelay")
        self.spinBoxSystemInfoDelay.setMinimum(1)
        self.spinBoxSystemInfoDelay.setMaximum(6000)

        self.horizontalLayout_8.addWidget(self.spinBoxSystemInfoDelay)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_8.addWidget(self.label_17)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_3.addWidget(self.label_4)

        self.progressBarCPU = QProgressBar(self.frame_3)
        self.progressBarCPU.setObjectName(u"progressBarCPU")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBarCPU.sizePolicy().hasHeightForWidth())
        self.progressBarCPU.setSizePolicy(sizePolicy1)
        self.progressBarCPU.setMaximumSize(QSize(150, 16777215))
        self.progressBarCPU.setValue(0)
        self.progressBarCPU.setAlignment(Qt.AlignCenter)
        self.progressBarCPU.setOrientation(Qt.Vertical)
        self.progressBarCPU.setInvertedAppearance(False)
        self.progressBarCPU.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_3.addWidget(self.progressBarCPU)

        self.labelCPUPercent = QLabel(self.frame_3)
        self.labelCPUPercent.setObjectName(u"labelCPUPercent")
        self.labelCPUPercent.setMaximumSize(QSize(150, 16777215))
        self.labelCPUPercent.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelCPUPercent)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_4.addWidget(self.label_15)

        self.progressBarRAM = QProgressBar(self.frame_3)
        self.progressBarRAM.setObjectName(u"progressBarRAM")
        sizePolicy1.setHeightForWidth(self.progressBarRAM.sizePolicy().hasHeightForWidth())
        self.progressBarRAM.setSizePolicy(sizePolicy1)
        self.progressBarRAM.setMaximumSize(QSize(150, 16777215))
        self.progressBarRAM.setValue(0)
        self.progressBarRAM.setOrientation(Qt.Vertical)

        self.verticalLayout_4.addWidget(self.progressBarRAM)

        self.labelRAMPercent = QLabel(self.frame_3)
        self.labelRAMPercent.setObjectName(u"labelRAMPercent")
        self.labelRAMPercent.setMaximumSize(QSize(150, 16777215))
        self.labelRAMPercent.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelRAMPercent)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0439\u043c\u0435\u0440:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u044f:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0441\u0435\u043a.", None))
        self.pushButtonStartTimer.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.pushButtonStopTimer.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u043f", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u0438:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0441\u0435\u043a.", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u0441\u0430\u0439\u0442\u0430:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"URL:", None))
        self.lineEditURL.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u0441\u0430\u0439\u0442\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435: http://www.google.com", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c \u043a\u0430\u0436\u0434\u044b\u0435:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u0441\u0435\u043a.", None))
        self.pushButtonUrlCheckStart.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.pushButtonUrlCheckStop.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u043f", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0441\u0438\u0441\u0442\u0435\u043c\u044b:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u043b\u044f\u0442\u044c \u043a\u0430\u0436\u0434\u044b\u0435:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u0441\u0435\u043a.", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"CPU", None))
        self.labelCPUPercent.setText(QCoreApplication.translate("Form", u"X%", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"RAM", None))
        self.labelRAMPercent.setText(QCoreApplication.translate("Form", u"X%", None))
    # retranslateUi

