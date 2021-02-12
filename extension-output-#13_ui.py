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
        MainWindow.resize(320, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(320, 500))
        MainWindow.setMaximumSize(QSize(320, 500))
        icon = QIcon()
        icon.addFile(u"icon/masjid.xpm", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	padding:0;\n"
"	margin:0;\n"
"background-color:#f6f6f6;\n"
"}")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(340, 340, 354, 446))
        self.tabWidget.setStyleSheet(u"")
        self.tab_pray_info = QWidget()
        self.tab_pray_info.setObjectName(u"tab_pray_info")
        self.gridLayout_3 = QGridLayout(self.tab_pray_info)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 0, 1, 2)

        self.tabWidget.addTab(self.tab_pray_info, "")
        self.tab_setting = QWidget()
        self.tab_setting.setObjectName(u"tab_setting")
        self.gridLayout_2 = QGridLayout(self.tab_setting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget.addTab(self.tab_setting, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-10, 0, 391, 271))
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"	background-image:url('icon/bg6-3.jpg');\n"
"	background-position:center;\n"
"	background-size:cover;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(30, 50, 171, 17))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"#label_31{\n"
"	color:white;\n"
"}")
        self.lblUpcomingWaktu = QLabel(self.frame_5)
        self.lblUpcomingWaktu.setObjectName(u"lblUpcomingWaktu")
        self.lblUpcomingWaktu.setGeometry(QRect(30, 74, 71, 18))
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblUpcomingWaktu.setFont(font1)
        self.lblUpcomingWaktu.setStyleSheet(u"#label_32{\n"
"	color:white;\n"
"	font-weight:bold;\n"
"}")
        self.lblUpcomingJam = QLabel(self.frame_5)
        self.lblUpcomingJam.setObjectName(u"lblUpcomingJam")
        self.lblUpcomingJam.setGeometry(QRect(101, 75, 61, 17))
        self.lblUpcomingJam.setFont(font)
        self.lblUpcomingJam.setStyleSheet(u"#label_33{\n"
"	color:white;\n"
"}")
        self.lblUpcomingRemaining = QLabel(self.frame_5)
        self.lblUpcomingRemaining.setObjectName(u"lblUpcomingRemaining")
        self.lblUpcomingRemaining.setGeometry(QRect(30, 96, 141, 41))
        font2 = QFont()
        font2.setFamily(u"Ubuntu")
        font2.setPointSize(10)
        self.lblUpcomingRemaining.setFont(font2)
        self.lblUpcomingRemaining.setStyleSheet(u"#label_34{\n"
"	color:white;\n"
"}")
        self.lblUpcomingRemaining.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblUpcomingRemaining.setWordWrap(True)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(200, 59, 20, 61))
        self.frame_6.setStyleSheet(u"#frame_6{\n"
"	border-style:outer;\n"
"	border-left:3px solid white;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.lblCurrentWaktu = QLabel(self.frame_5)
        self.lblCurrentWaktu.setObjectName(u"lblCurrentWaktu")
        self.lblCurrentWaktu.setGeometry(QRect(210, 60, 171, 61))
        font3 = QFont()
        font3.setFamily(u"Ubuntu")
        font3.setPointSize(18)
        font3.setBold(True)
        self.lblCurrentWaktu.setFont(font3)
        self.lblCurrentWaktu.setStyleSheet(u"#label_35{\n"
"	color:white;\n"
"}")
        self.lblCurrentWaktu.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblLocation = QLabel(self.frame_5)
        self.lblLocation.setObjectName(u"lblLocation")
        self.lblLocation.setGeometry(QRect(30, 13, 21, 21))
        self.lblLocation.setFont(font)
        self.lblLocation.setStyleSheet(u"#lblLocation{\n"
"	color:white;\n"
"	background-image:url('icon/location_on-24px.svg');\n"
"background-position:center;\n"
"}")
        self.lblCity = QLabel(self.frame_5)
        self.lblCity.setObjectName(u"lblCity")
        self.lblCity.setGeometry(QRect(52, 10, 101, 21))
        self.lblCity.setFont(font2)
        self.lblCity.setStyleSheet(u"#lblCity{\n"
"	color:white;\n"
"}")
        self.lblCity.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 130, 51, 32))
        self.label_10.setStyleSheet(u".QLabel{\n"
"	background-image:url('icon/noun_Sea Sunset_395675.svg');\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")
        self.label_36 = QLabel(self.frame_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(60, 157, 51, 16))
        self.label_36.setFont(font2)
        self.label_36.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.label_36.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_36.setWordWrap(True)
        self.lblSunset = QLabel(self.frame_5)
        self.lblSunset.setObjectName(u"lblSunset")
        self.lblSunset.setGeometry(QRect(60, 170, 51, 16))
        font4 = QFont()
        font4.setFamily(u"Ubuntu")
        font4.setPointSize(11)
        font4.setBold(True)
        self.lblSunset.setFont(font4)
        self.lblSunset.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.lblSunset.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lblSunset.setWordWrap(True)
        self.label_46 = QLabel(self.frame_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(230, 157, 51, 16))
        self.label_46.setFont(font2)
        self.label_46.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.label_46.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_46.setWordWrap(True)
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(230, 130, 51, 32))
        self.label_16.setStyleSheet(u".QLabel{\n"
"	background-image:url('icon/noun_Sunrise _395417.svg');\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")
        self.lblSunrise = QLabel(self.frame_5)
        self.lblSunrise.setObjectName(u"lblSunrise")
        self.lblSunrise.setGeometry(QRect(230, 170, 51, 16))
        self.lblSunrise.setFont(font4)
        self.lblSunrise.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.lblSunrise.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lblSunrise.setWordWrap(True)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(15, 195, 291, 251))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10;\n"
"	box-shadow: 10px 10px 5px darkgray;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 311, 41))
        self.frame_3.setStyleSheet(u"border-radius:0;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lblTodayName = QLabel(self.frame_3)
        self.lblTodayName.setObjectName(u"lblTodayName")
        self.lblTodayName.setGeometry(QRect(47, 0, 221, 20))
        font5 = QFont()
        font5.setFamily(u"Ubuntu")
        font5.setPointSize(10)
        font5.setBold(True)
        self.lblTodayName.setFont(font5)
        self.lblTodayName.setStyleSheet(u"color:black;")
        self.lblTodayName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblTodayDate = QLabel(self.frame_3)
        self.lblTodayDate.setObjectName(u"lblTodayDate")
        self.lblTodayDate.setGeometry(QRect(47, 20, 221, 20))
        font6 = QFont()
        font6.setFamily(u"Ubuntu")
        font6.setPointSize(9)
        font6.setBold(False)
        font6.setItalic(True)
        self.lblTodayDate.setFont(font6)
        self.lblTodayDate.setStyleSheet(u"color:grey;")
        self.lblTodayDate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(13, 0, 31, 41))
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"	background-image:url('icon/today-24px.svg');\n"
"	background-repeat:no-repeat;\n"
"	background-position:center;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frameFajr = QFrame(self.frame_2)
        self.frameFajr.setObjectName(u"frameFajr")
        self.frameFajr.setGeometry(QRect(10, 50, 271, 31))
        self.frameFajr.setStyleSheet(u"#frameFajr{\n"
"    border-style: outset;\n"
"	border-bottom:1px solid whitesmoke;\n"
"	border-radius:0;\n"
"}")
        self.frameFajr.setFrameShape(QFrame.NoFrame)
        self.frameFajr.setFrameShadow(QFrame.Plain)
        self.label_9 = QLabel(self.frameFajr)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 5, 71, 17))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color:black;")
        self.label_11 = QLabel(self.frameFajr)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 2, 21, 20))
        self.label_11.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txFajr = QLabel(self.frameFajr)
        self.txFajr.setObjectName(u"txFajr")
        self.txFajr.setGeometry(QRect(120, 3, 111, 20))
        self.txFajr.setMinimumSize(QSize(0, 17))
        self.txFajr.setFont(font2)
        self.txFajr.setLayoutDirection(Qt.LeftToRight)
        self.txFajr.setStyleSheet(u"color:black;")
        self.txFajr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frameDhuhr = QFrame(self.frame_2)
        self.frameDhuhr.setObjectName(u"frameDhuhr")
        self.frameDhuhr.setGeometry(QRect(10, 84, 271, 31))
        self.frameDhuhr.setFont(font2)
        self.frameDhuhr.setStyleSheet(u"#frameDhuhr{\n"
"	color:black;\n"
"	border-style: outset;\n"
"	border-bottom:1px solid whitesmoke;\n"
"	border-radius:0;\n"
"\n"
"}")
        self.frameDhuhr.setFrameShape(QFrame.StyledPanel)
        self.frameDhuhr.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frameDhuhr)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 5, 71, 17))
        font7 = QFont()
        font7.setFamily(u"Ubuntu")
        font7.setPointSize(10)
        font7.setBold(False)
        self.label_12.setFont(font7)
        self.label_12.setStyleSheet(u"color:black;")
        self.label_14 = QLabel(self.frameDhuhr)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(240, 2, 21, 20))
        self.label_14.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txDhuhr = QLabel(self.frameDhuhr)
        self.txDhuhr.setObjectName(u"txDhuhr")
        self.txDhuhr.setGeometry(QRect(120, 3, 111, 25))
        self.txDhuhr.setMinimumSize(QSize(0, 17))
        self.txDhuhr.setFont(font2)
        self.txDhuhr.setLayoutDirection(Qt.LeftToRight)
        self.txDhuhr.setStyleSheet(u"color:black;")
        self.txDhuhr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 118, 271, 31))
        self.frame_7.setFont(font2)
        self.frame_7.setStyleSheet(u"#frame_7{\n"
"	color:black;\n"
"	border-style: outset;\n"
"	border-bottom:1px solid whitesmoke;\n"
"	border-radius:0;\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 5, 71, 17))
        self.label_15.setFont(font7)
        self.label_15.setStyleSheet(u"")
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(240, 2, 21, 20))
        self.label_17.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txAshr = QLabel(self.frame_7)
        self.txAshr.setObjectName(u"txAshr")
        self.txAshr.setGeometry(QRect(120, 3, 111, 17))
        self.txAshr.setMinimumSize(QSize(0, 17))
        self.txAshr.setFont(font2)
        self.txAshr.setLayoutDirection(Qt.LeftToRight)
        self.txAshr.setStyleSheet(u"color:black;")
        self.txAshr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 152, 271, 31))
        self.frame_8.setFont(font2)
        self.frame_8.setStyleSheet(u"#frame_8{\n"
"	color:black;\n"
"	border-style: outset;\n"
"	border-bottom:1px solid whitesmoke;\n"
"	border-radius:0;\n"
"\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 5, 71, 17))
        self.label_18.setFont(font7)
        self.label_18.setStyleSheet(u"")
        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(240, 2, 21, 20))
        self.label_20.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txMaghrib = QLabel(self.frame_8)
        self.txMaghrib.setObjectName(u"txMaghrib")
        self.txMaghrib.setGeometry(QRect(120, 3, 110, 17))
        self.txMaghrib.setMinimumSize(QSize(0, 17))
        self.txMaghrib.setFont(font2)
        self.txMaghrib.setLayoutDirection(Qt.LeftToRight)
        self.txMaghrib.setStyleSheet(u"color:black;")
        self.txMaghrib.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 186, 271, 31))
        self.frame_9.setFont(font2)
        self.frame_9.setStyleSheet(u"#frame_9{\n"
"	color:black;\n"
"	border-style: outset;\n"
"	border-bottom:1px solid whitesmoke;\n"
"	border-radius:0;\n"
"\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 5, 71, 17))
        self.label_21.setFont(font7)
        self.label_21.setStyleSheet(u"")
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(240, 2, 21, 20))
        self.label_23.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txIsya = QLabel(self.frame_9)
        self.txIsya.setObjectName(u"txIsya")
        self.txIsya.setGeometry(QRect(120, 3, 110, 17))
        self.txIsya.setMinimumSize(QSize(0, 17))
        self.txIsya.setFont(font2)
        self.txIsya.setLayoutDirection(Qt.LeftToRight)
        self.txIsya.setStyleSheet(u"color: black;")
        self.txIsya.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_15 = QFrame(self.centralwidget)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 455, 321, 45))
        self.frame_15.setStyleSheet(u"#frame_15{\n"
"	border-style:outline;\n"
"	border-top: 1px solid #bdbdbd;\n"
"}")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.frame_15.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnTimeTable = QPushButton(self.frame_15)
        self.btnTimeTable.setObjectName(u"btnTimeTable")
        self.btnTimeTable.setMinimumSize(QSize(0, 45))
        self.btnTimeTable.setFont(font2)
        self.btnTimeTable.setStyleSheet(u".QPushButton{\n"
"	color:#626262;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icon/date_range-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btnTimeTable.setIcon(icon1)
        self.btnTimeTable.setIconSize(QSize(24, 24))
        self.btnTimeTable.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnTimeTable)

        self.btnSetting = QPushButton(self.frame_15)
        self.btnSetting.setObjectName(u"btnSetting")
        self.btnSetting.setMinimumSize(QSize(0, 45))
        self.btnSetting.setFont(font2)
        self.btnSetting.setStyleSheet(u".QPushButton{\n"
"	color:#626262;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icon/settings-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btnSetting.setIcon(icon2)
        self.btnSetting.setIconSize(QSize(24, 24))
        self.btnSetting.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnSetting)

        self.btnHide = QPushButton(self.frame_15)
        self.btnHide.setObjectName(u"btnHide")
        self.btnHide.setMinimumSize(QSize(0, 45))
        self.btnHide.setFont(font2)
        self.btnHide.setStyleSheet(u".QPushButton{\n"
"	color:#626262;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icon/hide_source-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btnHide.setIcon(icon3)
        self.btnHide.setIconSize(QSize(24, 24))
        self.btnHide.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnHide)

        self.btnExit = QPushButton(self.frame_15)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(0, 45))
        self.btnExit.setFont(font2)
        self.btnExit.setStyleSheet(u".QPushButton{\n"
"	color:#626262;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icon/exit_to_app-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btnExit.setIcon(icon4)
        self.btnExit.setIconSize(QSize(24, 24))
        self.btnExit.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnExit)

        self.frameSetting = QFrame(self.centralwidget)
        self.frameSetting.setObjectName(u"frameSetting")
        self.frameSetting.setEnabled(True)
        self.frameSetting.setGeometry(QRect(0, 0, 374, 455))
        self.frameSetting.setStyleSheet(u"#frameSetting{\n"
"	background-color:#22355d;\n"
"}")
        self.frameSetting.setFrameShape(QFrame.StyledPanel)
        self.frameSetting.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameSetting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.frameSetting)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnPlay = QPushButton(self.frameSetting)
        self.btnPlay.setObjectName(u"btnPlay")

        self.horizontalLayout_2.addWidget(self.btnPlay)

        self.btnStop = QPushButton(self.frameSetting)
        self.btnStop.setObjectName(u"btnStop")

        self.horizontalLayout_2.addWidget(self.btnStop)

        self.btnSave = QPushButton(self.frameSetting)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 1, 1, 2)

        self.cbMathhab = QComboBox(self.frameSetting)
        self.cbMathhab.addItem("")
        self.cbMathhab.addItem("")
        self.cbMathhab.setObjectName(u"cbMathhab")

        self.gridLayout.addWidget(self.cbMathhab, 5, 2, 1, 1)

        self.label_5 = QLabel(self.frameSetting)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 175, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 2, 1, 1)

        self.label_3 = QLabel(self.frameSetting)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.label_2 = QLabel(self.frameSetting)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.txLong = QLineEdit(self.frameSetting)
        self.txLong.setObjectName(u"txLong")

        self.gridLayout.addWidget(self.txLong, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 175, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.label = QLabel(self.frameSetting)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.cbMethod = QComboBox(self.frameSetting)
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.setObjectName(u"cbMethod")

        self.gridLayout.addWidget(self.cbMethod, 4, 2, 1, 1)

        self.label_41 = QLabel(self.frameSetting)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 40))
        font8 = QFont()
        font8.setFamily(u"Ubuntu")
        font8.setPointSize(16)
        self.label_41.setFont(font8)
        self.label_41.setStyleSheet(u"#label_41{\n"
"	color:white;\n"
"}")
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_41, 0, 0, 1, 1)

        self.txLat = QLineEdit(self.frameSetting)
        self.txLat.setObjectName(u"txLat")
        self.txLat.setMinimumSize(QSize(0, 0))
        self.txLat.setMaximumSize(QSize(220, 16777215))
        self.txLat.setFrame(False)

        self.gridLayout.addWidget(self.txLat, 1, 2, 1, 1)

        self.ckStartTray = QCheckBox(self.frameSetting)
        self.ckStartTray.setObjectName(u"ckStartTray")

        self.gridLayout.addWidget(self.ckStartTray, 6, 2, 1, 1)

        self.label_4 = QLabel(self.frameSetting)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 2)

        self.txUtc = QLineEdit(self.frameSetting)
        self.txUtc.setObjectName(u"txUtc")

        self.gridLayout.addWidget(self.txUtc, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.frameSetting.raise_()
        self.tabWidget.raise_()
        self.frame_5.raise_()
        self.frame_15.raise_()
        self.frame_2.raise_()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AyoShalat", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"AyoShalat", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pray_info), QCoreApplication.translate("MainWindow", u"Prayer Times", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setting), QCoreApplication.translate("MainWindow", u"Setting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Page", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"UPCOMING PRAYER", None))
        self.lblUpcomingWaktu.setText(QCoreApplication.translate("MainWindow", u"Maghrib", None))
        self.lblUpcomingJam.setText(QCoreApplication.translate("MainWindow", u"12:00", None))
        self.lblUpcomingRemaining.setText(QCoreApplication.translate("MainWindow", u"2 hours and 25 minutes to go", None))
        self.lblCurrentWaktu.setText(QCoreApplication.translate("MainWindow", u"Magrib", None))
        self.lblLocation.setText("")
        self.lblCity.setText(QCoreApplication.translate("MainWindow", u"Sidoarjo", None))
        self.label_10.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"sunset", None))
        self.lblSunset.setText(QCoreApplication.translate("MainWindow", u"17:45", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"sunrise", None))
        self.label_16.setText("")
        self.lblSunrise.setText(QCoreApplication.translate("MainWindow", u"4:45", None))
        self.lblTodayName.setText(QCoreApplication.translate("MainWindow", u"Today / Wednesday", None))
        self.lblTodayDate.setText(QCoreApplication.translate("MainWindow", u"20 February 2020 / 20 Ramadhan 1445", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Fajr", None))
        self.label_11.setText("")
        self.txFajr.setText(QCoreApplication.translate("MainWindow", u"txtFajr", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Dhuhr", None))
        self.label_14.setText("")
        self.txDhuhr.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Asr", None))
        self.label_17.setText("")
        self.txAshr.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Maghrib", None))
        self.label_20.setText("")
        self.txMaghrib.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Isya", None))
        self.label_23.setText("")
        self.txIsya.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnTimeTable.setText(QCoreApplication.translate("MainWindow", u"Prayer", None))
        self.btnSetting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.btnHide.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mathab", None))
        self.btnPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.cbMathhab.setItemText(0, QCoreApplication.translate("MainWindow", u"Shafi'i", None))
        self.cbMathhab.setItemText(1, QCoreApplication.translate("MainWindow", u"Hanafi", None))

        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"UTC", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.cbMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Egyptian General Authority of Survey", None))
        self.cbMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"University of Islamic Sciences, Karachi (Shaf'i)", None))
        self.cbMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"University of Islamic Sciences, Karachi (Hanafi)", None))
        self.cbMethod.setItemText(3, QCoreApplication.translate("MainWindow", u"Islamic Society of North America", None))
        self.cbMethod.setItemText(4, QCoreApplication.translate("MainWindow", u"Muslim World League (MWL)", None))
        self.cbMethod.setItemText(5, QCoreApplication.translate("MainWindow", u"Umm Al-Qurra University", None))
        self.cbMethod.setItemText(6, QCoreApplication.translate("MainWindow", u"Fixed Isha Angle Interval (always 90)", None))
        self.cbMethod.setItemText(7, QCoreApplication.translate("MainWindow", u"Egyptian General Authority of Survey (Egypt)", None))

        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.ckStartTray.setText(QCoreApplication.translate("MainWindow", u"Start in Tray", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Method", None))
    # retranslateUi

