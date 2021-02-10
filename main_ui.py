# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(372, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(372, 350))
        MainWindow.setMaximumSize(QSize(394, 350))
        icon = QIcon()
        icon.addFile(u"icon/masjid.xpm", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(18, 62, 100);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnHide = QPushButton(self.frame)
        self.btnHide.setObjectName(u"btnHide")
        self.btnHide.setStyleSheet(u"background-color: rgb(18, 62, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.btnHide)

        self.btnExit = QPushButton(self.frame)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(100, 25))
        self.btnExit.setMaximumSize(QSize(100, 25))
        self.btnExit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnExit.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btnExit)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(18, 62, 100);\n"
"color: rgb(255, 255, 255);")
        self.tab_pray_info = QWidget()
        self.tab_pray_info.setObjectName(u"tab_pray_info")
        self.gridLayout_3 = QGridLayout(self.tab_pray_info)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 7, 0, 1, 4)

        self.txFajr = QLabel(self.tab_pray_info)
        self.txFajr.setObjectName(u"txFajr")
        self.txFajr.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setPointSize(20)
        self.txFajr.setFont(font)
        self.txFajr.setLayoutDirection(Qt.LeftToRight)
        self.txFajr.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txFajr.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txFajr, 0, 0, 1, 4)

        self.txDhuhr = QLabel(self.tab_pray_info)
        self.txDhuhr.setObjectName(u"txDhuhr")
        self.txDhuhr.setMinimumSize(QSize(0, 25))
        self.txDhuhr.setFont(font)
        self.txDhuhr.setLayoutDirection(Qt.LeftToRight)
        self.txDhuhr.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txDhuhr.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txDhuhr, 2, 0, 1, 4)

        self.txAshr = QLabel(self.tab_pray_info)
        self.txAshr.setObjectName(u"txAshr")
        self.txAshr.setMinimumSize(QSize(0, 25))
        self.txAshr.setFont(font)
        self.txAshr.setLayoutDirection(Qt.LeftToRight)
        self.txAshr.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txAshr.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txAshr, 4, 0, 1, 4)

        self.txMaghrib = QLabel(self.tab_pray_info)
        self.txMaghrib.setObjectName(u"txMaghrib")
        self.txMaghrib.setMinimumSize(QSize(0, 25))
        self.txMaghrib.setFont(font)
        self.txMaghrib.setLayoutDirection(Qt.LeftToRight)
        self.txMaghrib.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txMaghrib.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txMaghrib, 5, 0, 1, 4)

        self.txIsya = QLabel(self.tab_pray_info)
        self.txIsya.setObjectName(u"txIsya")
        self.txIsya.setMinimumSize(QSize(0, 25))
        self.txIsya.setFont(font)
        self.txIsya.setLayoutDirection(Qt.LeftToRight)
        self.txIsya.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txIsya.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txIsya, 6, 0, 1, 4)

        self.tabWidget.addTab(self.tab_pray_info, "")
        self.tab_setting = QWidget()
        self.tab_setting.setObjectName(u"tab_setting")
        self.gridLayout_2 = QGridLayout(self.tab_setting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 10, 2, 1, 1)

        self.txLong = QLineEdit(self.tab_setting)
        self.txLong.setObjectName(u"txLong")

        self.gridLayout_2.addWidget(self.txLong, 3, 2, 1, 1)

        self.cbMethod = QComboBox(self.tab_setting)
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.setObjectName(u"cbMethod")

        self.gridLayout_2.addWidget(self.cbMethod, 6, 2, 1, 1)

        self.cbMathhab = QComboBox(self.tab_setting)
        self.cbMathhab.addItem("")
        self.cbMathhab.addItem("")
        self.cbMathhab.setObjectName(u"cbMathhab")

        self.gridLayout_2.addWidget(self.cbMathhab, 7, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnPlay = QPushButton(self.tab_setting)
        self.btnPlay.setObjectName(u"btnPlay")

        self.horizontalLayout_2.addWidget(self.btnPlay)

        self.btnStop = QPushButton(self.tab_setting)
        self.btnStop.setObjectName(u"btnStop")

        self.horizontalLayout_2.addWidget(self.btnStop)

        self.btnSave = QPushButton(self.tab_setting)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 9, 2, 1, 1)

        self.label = QLabel(self.tab_setting)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.txUtc = QLineEdit(self.tab_setting)
        self.txUtc.setObjectName(u"txUtc")

        self.gridLayout_2.addWidget(self.txUtc, 5, 2, 1, 1)

        self.label_3 = QLabel(self.tab_setting)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_4 = QLabel(self.tab_setting)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_2 = QLabel(self.tab_setting)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_6 = QLabel(self.tab_setting)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)

        self.txLat = QLineEdit(self.tab_setting)
        self.txLat.setObjectName(u"txLat")

        self.gridLayout_2.addWidget(self.txLat, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 9, 0, 2, 1)

        self.ckStartTray = QCheckBox(self.tab_setting)
        self.ckStartTray.setObjectName(u"ckStartTray")

        self.gridLayout_2.addWidget(self.ckStartTray, 8, 2, 1, 1)

        self.label_5 = QLabel(self.tab_setting)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 8, 0, 1, 1)

        self.tabWidget.addTab(self.tab_setting, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btnExit.setDefault(False)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AyoShalat", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"AyoShalat", None))
#endif // QT_CONFIG(tooltip)
        self.btnHide.setText(QCoreApplication.translate("MainWindow", u"Hide me !", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.txFajr.setText(QCoreApplication.translate("MainWindow", u"txtFajr", None))
        self.txDhuhr.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.txAshr.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.txMaghrib.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.txIsya.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pray_info), QCoreApplication.translate("MainWindow", u"Prayer Times", None))
        self.cbMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Egyptian General Authority of Survey", None))
        self.cbMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"University of Islamic Sciences, Karachi (Shaf'i)", None))
        self.cbMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"University of Islamic Sciences, Karachi (Hanafi)", None))
        self.cbMethod.setItemText(3, QCoreApplication.translate("MainWindow", u"Islamic Society of North America", None))
        self.cbMethod.setItemText(4, QCoreApplication.translate("MainWindow", u"Muslim World League (MWL)", None))
        self.cbMethod.setItemText(5, QCoreApplication.translate("MainWindow", u"Umm Al-Qurra University", None))
        self.cbMethod.setItemText(6, QCoreApplication.translate("MainWindow", u"Fixed Isha Angle Interval (always 90)", None))
        self.cbMethod.setItemText(7, QCoreApplication.translate("MainWindow", u"Egyptian General Authority of Survey (Egypt)", None))

        self.cbMathhab.setItemText(0, QCoreApplication.translate("MainWindow", u"Shafi'i", None))
        self.cbMathhab.setItemText(1, QCoreApplication.translate("MainWindow", u"Hanafi", None))

        self.btnPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"UTC", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mathab", None))
        self.ckStartTray.setText(QCoreApplication.translate("MainWindow", u"Start in Tray", None))
        self.label_5.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setting), QCoreApplication.translate("MainWindow", u"Setting", None))
    # retranslateUi

