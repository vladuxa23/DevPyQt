# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KadrPrikaz_1.ui'
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
        Form.resize(965, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(700, 500))
        Form.setMaximumSize(QSize(1200, 800))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QSize(25, 25))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_3 = QVBoxLayout(self.tab1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableView = QTableView(self.groupBox)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_5.addWidget(self.tableView)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        font1 = QFont()
        font1.setPointSize(10)
        self.radioButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMaximumSize(QSize(1111111, 25))

        self.horizontalLayout_2.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMaximumSize(QSize(10000000, 25))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_6 = QVBoxLayout(self.tab2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tableView_2 = QTableView(self.tab2)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_6.addWidget(self.tableView_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_4 = QPushButton(self.tab2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.tab2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.tabWidget.addTab(self.tab4, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043a\u0430\u0MDMP“§a            ¾OÈb¤        „       h&  ˜     <    /     Ä  Þg     ¨   `     8   Ô      T        3  0F    ì  </     ˜   (1                                                              	  -
       dJ     À1     Lw² ñ                  T  ÷  ”T  ¹OÈb                                       @5<O  2  D>@<0B5  U T C                                               @5<O  2  D>@<0B5  U T C                                               1 9 0 4 1 . 1 . a m d 6 4 f r e . v b _ r e l e a s e . 1 9 1 2 0 6 - 1 4 0 6                                                                                                                                                                                                                                                                                                                                                                                                                                                           d b g c o r e . a m d 6 4 , 1 0 . 0 . 1 9 0 4 1 . 7 8 9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         t	,
ä	        À            66ñÎú                                                                                                                                 Ð  Ž<     ä	               Àß   X>ß   ¨r  Š  Ð  ^A  (              àß   (ú]ß   Ø  
 Ð  .F                  ß   ¨÷|ß   X  * Ð  þJ  ¨               ß   ¨ø›ß   X  ’ Ð  ÎO  X;              @ß   ˜õºß   h
  
! Ð  žT  „C              `ß   øÙß   è  ªl  Ð  nY  @;              €ß   ¨õøß   X
  ªt  Ð  >^  t)              Àß   ˆòß   x  
  Ð  c              [     Ûö     õ¼ ¯O[aÆ1  ½ïþ   
  õ– 
  õ– ?                         7               `                }Jû   P ‹ã ìT{à1  ½ïþ     
 ’aJ  
 ’aJ?                        "               `A                dIû   Ð ¥ Ï'\Nø1  ½ïþ     
 ªaJ  
 ªaJ?                        %               `A                IHû   Ð, í¡- [ËŠE2  ½ïþ     
 ªaJ  
 ªaJ?                        '               `A                Hû     V> ¿H×+82  ½ïþ     
 aJ  
 aJ?                        %               `A                dÏú    E á”D pO[aV2  ½ïþ   
  õ– 
  õ– ?                         :               `                æ.û   ° ´Æ Ì(ÿ`v2  ½ïþ       µu    µu?                         ^               `A                ÆHû   ° KÏ [1ó¯œ2  ½ïþ     
 "aJ  
 "aJ?                        #               `A                Jû   P Ì îüZ±¶2  ½ïþ     
 ªaJ  
 ªaJ?                        #               `A                ²Bû      v×  SÐ2  ½ïþ     
 "aJ  
 "aJ?                        $               `A                =Jû   à
 ?Ò
 4e8Aì2  ½ïþ     
 ’aJ  
 ’aJ?                        %               `A                ”Hû   à	 ]è	 9ŸOV
3  ½ïþ      "aJ  
 "aJ?                        #               `A                ãHû   À	 Ãë	 !tÕS$3  ½ïþ     
 2aJ  
 2aJ?                        $               `A                ‰Gû   € ¾Ò æzÙ@3  ½ïþ     
 "aJ  
 "aJ?                        $      