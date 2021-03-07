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
        self.frameDashboardUpper = QFrame(self.centralwidget)
        self.frameDashboardUpper.setObjectName(u"frameDashboardUpper")
        self.frameDashboardUpper.setGeometry(QRect(-10, 0, 391, 271))
        self.frameDashboardUpper.setStyleSheet(u"#frameDashboardUpper{\n"
"	background-image:url('icon/bg6-3.jpg');\n"
"        background-position:center;\n"
"}")
        self.frameDashboardUpper.setFrameShape(QFrame.StyledPanel)
        self.frameDashboardUpper.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frameDashboardUpper)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(30, 56, 171, 17))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.lblUpcomingWaktu = QLabel(self.frameDashboardUpper)
        self.lblUpcomingWaktu.setObjectName(u"lblUpcomingWaktu")
        self.lblUpcomingWaktu.setGeometry(QRect(30, 80, 71, 18))
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblUpcomingWaktu.setFont(font1)
        self.lblUpcomingWaktu.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"	font-weight:bold;\n"
"}")
        self.lblUpcomingJam = QLabel(self.frameDashboardUpper)
        self.lblUpcomingJam.setObjectName(u"lblUpcomingJam")
        self.lblUpcomingJam.setGeometry(QRect(101, 81, 61, 17))
        self.lblUpcomingJam.setFont(font)
        self.lblUpcomingJam.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.lblRemaining = QLabel(self.frameDashboardUpper)
        self.lblRemaining.setObjectName(u"lblRemaining")
        self.lblRemaining.setGeometry(QRect(30, 102, 141, 41))
        font2 = QFont()
        font2.setFamily(u"Ubuntu")
        font2.setPointSize(10)
        self.lblRemaining.setFont(font2)
        self.lblRemaining.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.lblRemaining.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblRemaining.setWordWrap(True)
        self.frame_6 = QFrame(self.frameDashboardUpper)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(200, 65, 20, 61))
        self.frame_6.setStyleSheet(u"#frame_6{\n"
"	border-style:outer;\n"
"	border-left:3px solid white;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.lblCurrentWaktu = QLabel(self.frameDashboardUpper)
        self.lblCurrentWaktu.setObjectName(u"lblCurrentWaktu")
        self.lblCurrentWaktu.setGeometry(QRect(210, 66, 171, 61))
        font3 = QFont()
        font3.setFamily(u"Ubuntu")
        font3.setPointSize(18)
        font3.setBold(True)
        self.lblCurrentWaktu.setFont(font3)
        self.lblCurrentWaktu.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.lblCurrentWaktu.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblLocation = QLabel(self.frameDashboardUpper)
        self.lblLocation.setObjectName(u"lblLocation")
        self.lblLocation.setGeometry(QRect(30, 19, 21, 21))
        self.lblLocation.setFont(font)
        self.lblLocation.setStyleSheet(u"#lblLocation{\n"
"	color:white;\n"
"	background-image:url('icon/location_on-24px.svg');\n"
"background-position:center;\n"
"}")
        self.lblCity = QLabel(self.frameDashboardUpper)
        self.lblCity.setObjectName(u"lblCity")
        self.lblCity.setGeometry(QRect(52, 16, 101, 21))
        self.lblCity.setFont(font2)
        self.lblCity.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.lblCity.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_10 = QLabel(self.frameDashboardUpper)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 136, 51, 32))
        self.label_10.setStyleSheet(u".QLabel{\n"
"	background-image:url('icon/noun_Sea Sunset_395675.svg');\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")
        self.label_36 = QLabel(self.frameDashboardUpper)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(60, 163, 51, 16))
        self.label_36.setFont(font2)
        self.label_36.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.label_36.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_36.setWordWrap(True)
        self.lblSunset = QLabel(self.frameDashboardUpper)
        self.lblSunset.setObjectName(u"lblSunset")
        self.lblSunset.setGeometry(QRect(60, 176, 51, 16))
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
        self.label_46 = QLabel(self.frameDashboardUpper)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(230, 163, 51, 16))
        self.label_46.setFont(font2)
        self.label_46.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.label_46.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_46.setWordWrap(True)
        self.label_16 = QLabel(self.frameDashboardUpper)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(230, 136, 51, 32))
        self.label_16.setStyleSheet(u".QLabel{\n"
"	background-image:url('icon/noun_Sunrise _395417.svg');\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")
        self.lblSunrise = QLabel(self.frameDashboardUpper)
        self.lblSunrise.setObjectName(u"lblSunrise")
        self.lblSunrise.setGeometry(QRect(230, 176, 51, 16))
        self.lblSunrise.setFont(font4)
        self.lblSunrise.setStyleSheet(u".QLabel{\n"
"	color:white;\n"
"}")
        self.lblSunrise.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lblSunrise.setWordWrap(True)
        self.frame_time_table = QFrame(self.centralwidget)
        self.frame_time_table.setObjectName(u"frame_time_table")
        self.frame_time_table.setGeometry(QRect(15, 204, 291, 241))
        self.frame_time_table.setStyleSheet(u"#frame_time_table{\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius:10;\n"
"	border-style:outer;\n"
"	border:1px solid #cbcbcb;\n"
"}\n"
"\n"
".QFrame{\n"
"	border-bottom:1px solid whitesmoke;\n"
"	border-radius:0;\n"
"}")
        self.frame_time_table.setFrameShape(QFrame.StyledPanel)
        self.frame_time_table.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_time_table)
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
        self.frameFajr = QFrame(self.frame_time_table)
        self.frameFajr.setObjectName(u"frameFajr")
        self.frameFajr.setGeometry(QRect(10, 54, 271, 31))
        self.frameFajr.setStyleSheet(u"")
        self.frameFajr.setFrameShape(QFrame.NoFrame)
        self.frameFajr.setFrameShadow(QFrame.Plain)
        self.label_9 = QLabel(self.frameFajr)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 3, 71, 25))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(0, 25))
        font7 = QFont()
        font7.setFamily(u"Ubuntu")
        font7.setPointSize(11)
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"color:black;")
        self.label_11 = QLabel(self.frameFajr)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 3, 21, 25))
        self.label_11.setMinimumSize(QSize(0, 25))
        self.label_11.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txFajr = QLabel(self.frameFajr)
        self.txFajr.setObjectName(u"txFajr")
        self.txFajr.setGeometry(QRect(120, 3, 111, 25))
        self.txFajr.setMinimumSize(QSize(0, 25))
        self.txFajr.setFont(font7)
        self.txFajr.setLayoutDirection(Qt.LeftToRight)
        self.txFajr.setStyleSheet(u"color:black;")
        self.txFajr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frameDhuhr = QFrame(self.frame_time_table)
        self.frameDhuhr.setObjectName(u"frameDhuhr")
        self.frameDhuhr.setGeometry(QRect(10, 88, 271, 31))
        self.frameDhuhr.setFont(font2)
        self.frameDhuhr.setStyleSheet(u"")
        self.frameDhuhr.setFrameShape(QFrame.NoFrame)
        self.frameDhuhr.setFrameShadow(QFrame.Plain)
        self.label_12 = QLabel(self.frameDhuhr)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 3, 71, 25))
        self.label_12.setMinimumSize(QSize(0, 25))
        font8 = QFont()
        font8.setFamily(u"Ubuntu")
        font8.setPointSize(11)
        font8.setBold(False)
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet(u"color:black;")
        self.label_14 = QLabel(self.frameDhuhr)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(240, 3, 21, 25))
        self.label_14.setMinimumSize(QSize(0, 25))
        self.label_14.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txDhuhr = QLabel(self.frameDhuhr)
        self.txDhuhr.setObjectName(u"txDhuhr")
        self.txDhuhr.setGeometry(QRect(120, 3, 111, 25))
        self.txDhuhr.setMinimumSize(QSize(0, 25))
        self.txDhuhr.setFont(font7)
        self.txDhuhr.setLayoutDirection(Qt.LeftToRight)
        self.txDhuhr.setStyleSheet(u"color:black;")
        self.txDhuhr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frameAsr = QFrame(self.frame_time_table)
        self.frameAsr.setObjectName(u"frameAsr")
        self.frameAsr.setGeometry(QRect(10, 122, 271, 31))
        self.frameAsr.setFont(font2)
        self.frameAsr.setStyleSheet(u"")
        self.frameAsr.setFrameShape(QFrame.NoFrame)
        self.frameAsr.setFrameShadow(QFrame.Plain)
        self.label_15 = QLabel(self.frameAsr)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 3, 71, 25))
        self.label_15.setMinimumSize(QSize(0, 25))
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"")
        self.label_17 = QLabel(self.frameAsr)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(240, 3, 21, 25))
        self.label_17.setMinimumSize(QSize(0, 25))
        self.label_17.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txAshr = QLabel(self.frameAsr)
        self.txAshr.setObjectName(u"txAshr")
        self.txAshr.setGeometry(QRect(120, 3, 111, 25))
        self.txAshr.setMinimumSize(QSize(0, 25))
        self.txAshr.setFont(font7)
        self.txAshr.setLayoutDirection(Qt.LeftToRight)
        self.txAshr.setStyleSheet(u"color:black;")
        self.txAshr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frameMaghrib = QFrame(self.frame_time_table)
        self.frameMaghrib.setObjectName(u"frameMaghrib")
        self.frameMaghrib.setGeometry(QRect(10, 156, 271, 31))
        self.frameMaghrib.setFont(font2)
        self.frameMaghrib.setStyleSheet(u"")
        self.frameMaghrib.setFrameShape(QFrame.NoFrame)
        self.frameMaghrib.setFrameShadow(QFrame.Plain)
        self.label_18 = QLabel(self.frameMaghrib)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 3, 71, 25))
        self.label_18.setMinimumSize(QSize(0, 25))
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"")
        self.label_20 = QLabel(self.frameMaghrib)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(240, 3, 21, 25))
        self.label_20.setMinimumSize(QSize(0, 25))
        self.label_20.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txMaghrib = QLabel(self.frameMaghrib)
        self.txMaghrib.setObjectName(u"txMaghrib")
        self.txMaghrib.setGeometry(QRect(120, 3, 110, 25))
        self.txMaghrib.setMinimumSize(QSize(0, 25))
        self.txMaghrib.setFont(font7)
        self.txMaghrib.setLayoutDirection(Qt.LeftToRight)
        self.txMaghrib.setStyleSheet(u"color:black;")
        self.txMaghrib.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frameIsya = QFrame(self.frame_time_table)
        self.frameIsya.setObjectName(u"frameIsya")
        self.frameIsya.setGeometry(QRect(10, 190, 271, 31))
        self.frameIsya.setFont(font2)
        self.frameIsya.setStyleSheet(u"")
        self.frameIsya.setFrameShape(QFrame.NoFrame)
        self.frameIsya.setFrameShadow(QFrame.Plain)
        self.label_21 = QLabel(self.frameIsya)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 3, 71, 25))
        self.label_21.setMinimumSize(QSize(0, 25))
        self.label_21.setFont(font8)
        self.label_21.setStyleSheet(u"")
        self.label_23 = QLabel(self.frameIsya)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(240, 3, 21, 25))
        self.label_23.setMinimumSize(QSize(0, 25))
        self.label_23.setStyleSheet(u"background-image:url('icon/chevron_left-24px.svg');\n"
"background-repeat:no-repeat;\n"
"background-position:right center;")
        self.txIsya = QLabel(self.frameIsya)
        self.txIsya.setObjectName(u"txIsya")
        self.txIsya.setGeometry(QRect(120, 3, 110, 25))
        self.txIsya.setMinimumSize(QSize(0, 25))
        self.txIsya.setFont(font7)
        self.txIsya.setLayoutDirection(Qt.LeftToRight)
        self.txIsya.setStyleSheet(u"color: black;")
        self.txIsya.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frameButtonBar = QFrame(self.centralwidget)
        self.frameButtonBar.setObjectName(u"frameButtonBar")
        self.frameButtonBar.setGeometry(QRect(0, 455, 321, 45))
        self.frameButtonBar.setStyleSheet(u"#frameButtonBar{\n"
"	border-style:outline;\n"
"	border-top: 1px solid #bdbdbd;\n"
"}\n"
".QPushButton{\n"
"	color:#626262;\n"
"	border:none;\n"
"}\n"
".QPushButton:hover{\n"
"	background: rgb(223, 223, 223);\n"
"}")
        self.frameButtonBar.setFrameShape(QFrame.NoFrame)
        self.frameButtonBar.setFrameShadow(QFrame.Plain)
        self.frameButtonBar.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frameButtonBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnTimeTable = QPushButton(self.frameButtonBar)
        self.btnTimeTable.setObjectName(u"btnTimeTable")
        self.btnTimeTable.setMinimumSize(QSize(0, 45))
        self.btnTimeTable.setFont(font2)
        self.btnTimeTable.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"icon/date_range-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btnTimeTable.setIcon(icon1)
        self.btnTimeTable.setIconSize(QSize(24, 24))
        self.btnTimeTable.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnTimeTable)

        self.btnSetting = QPushButton(self.frameButtonBar)
        self.btnSetting.setObjectName(u"btnSetting")
        self.btnSetting.setMinimumSize(QSize(0, 45))
        self.btnSetting.setFont(font2)
        self.btnSetting.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"icon/settings-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btnSetting.setIcon(icon2)
        self.btnSetting.setIconSize(QSize(24, 24))
        self.btnSetting.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnSetting)

        self.btnHide = QPushButton(self.frameButtonBar)
        self.btnHide.setObjectName(u"btnHide")
        self.btnHide.setMinimumSize(QSize(0, 45))
        self.btnHide.setFont(font2)
        self.btnHide.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"icon/hide_source-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btnHide.setIcon(icon3)
        self.btnHide.setIconSize(QSize(24, 24))
        self.btnHide.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnHide)

        self.btnExit = QPushButton(self.frameButtonBar)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(0, 45))
        self.btnExit.setFont(font2)
        self.btnExit.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"icon/exit_to_app-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btnExit.setIcon(icon4)
        self.btnExit.setIconSize(QSize(24, 24))
        self.btnExit.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnExit)

        self.frameSetting = QFrame(self.centralwidget)
        self.frameSetting.setObjectName(u"frameSetting")
        self.frameSetting.setEnabled(True)
        self.frameSetting.setGeometry(QRect(0, 0, 321, 450))
        self.frameSetting.setStyleSheet(u"#frameSetting{\n"
"	background-color:#f6f6f6;\n"
"	color:white;\n"
"}\n"
".QLabel{\n"
"	color:white;\n"
"}")
        self.frameSetting.setFrameShape(QFrame.StyledPanel)
        self.frameSetting.setFrameShadow(QFrame.Raised)
        self.containerSetting = QFrame(self.frameSetting)
        self.containerSetting.setObjectName(u"containerSetting")
        self.containerSetting.setGeometry(QRect(15, 54, 291, 391))
        self.containerSetting.setStyleSheet(u".QLineEdit{\n"
"	border:none;\n"
"	border-radius:0px;\n"
"	background-color:whitesmoke;\n"
"	border-bottom:1px solid gray;\n"
"}\n"
"#containerSetting{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10;\n"
"	border-style:outer;\n"
"	border:1px solid #cbcbcb;\n"
"}\n"
".QLabel{\n"
"	color:black;\n"
"}\n"
".QPushButton{\n"
"	border-radius:2px;\n"
"	background-color:rgb(0, 85, 127);\n"
"	color:#fff;\n"
"}\n"
".QPushButton:hover{\n"
"	background-color:rgb(0, 135, 201);\n"
"}\n"
".QCheckBox{\n"
"	color:black;\n"
"}\n"
"\n"
".QComboBox{\n"
"border:none;\n"
"	border:none;\n"
"	border-radius:0px;\n"
"	background-color:whitesmoke;\n"
"	selection-color: black;\n"
"      selection-background-color: rgb(255, 186, 97);\n"
"	border-bottom:1px solid gray;\n"
"}\n"
"\n"
".QComboBox::drop-down:button{\n"
"	background-color: rgb(234,234,234);\n"
"	width:25px;\n"
"background-image:url('icon/expand_more-24px.svg')\n"
"}")
        self.containerSetting.setFrameShape(QFrame.StyledPanel)
        self.containerSetting.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.containerSetting)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 110, 70, 25))
        self.label_3.setMinimumSize(QSize(70, 25))
        self.label_3.setMaximumSize(QSize(70, 25))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.containerSetting)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 340, 251, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnPlay = QPushButton(self.layoutWidget)
        self.btnPlay.setObjectName(u"btnPlay")
        self.btnPlay.setMinimumSize(QSize(0, 30))
        self.btnPlay.setMaximumSize(QSize(16777215, 30))
        self.btnPlay.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPlay.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnPlay)

        self.btnStop = QPushButton(self.layoutWidget)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setMinimumSize(QSize(0, 30))
        self.btnStop.setMaximumSize(QSize(16777215, 30))
        self.btnStop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnStop.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnStop)

        self.btnSave = QPushButton(self.layoutWidget)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(0, 30))
        self.btnSave.setMaximumSize(QSize(16777215, 30))
        self.btnSave.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSave.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btnSave)

        self.ckStartTray = QCheckBox(self.containerSetting)
        self.ckStartTray.setObjectName(u"ckStartTray")
        self.ckStartTray.setGeometry(QRect(20, 210, 101, 25))
        self.ckStartTray.setMinimumSize(QSize(20, 25))
        self.ckStartTray.setMaximumSize(QSize(210, 25))
        self.ckStartTray.setFont(font2)
        self.ckStartTray.setStyleSheet(u"")
        self.label = QLabel(self.containerSetting)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 70, 25))
        self.label.setMinimumSize(QSize(70, 25))
        self.label.setMaximumSize(QSize(70, 25))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")
        self.label_6 = QLabel(self.containerSetting)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 110, 70, 25))
        self.label_6.setMinimumSize(QSize(70, 25))
        self.label_6.setMaximumSize(QSize(70, 25))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"")
        self.cbMathhab = QComboBox(self.containerSetting)
        self.cbMathhab.addItem("")
        self.cbMathhab.addItem("")
        self.cbMathhab.setObjectName(u"cbMathhab")
        self.cbMathhab.setGeometry(QRect(100, 130, 171, 25))
        self.cbMathhab.setMinimumSize(QSize(20, 25))
        self.cbMathhab.setMaximumSize(QSize(320, 16777215))
        self.cbMathhab.setFont(font2)
        self.cbMathhab.setStyleSheet(u"")
        self.cbMathhab.setFrame(False)
        self.cbMethod = QComboBox(self.containerSetting)
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.addItem("")
        self.cbMethod.setObjectName(u"cbMethod")
        self.cbMethod.setGeometry(QRect(20, 180, 251, 25))
        self.cbMethod.setMinimumSize(QSize(20, 25))
        self.cbMethod.setMaximumSize(QSize(320, 16777215))
        self.cbMethod.setFont(font2)
        self.cbMethod.setStyleSheet(u"")
        self.cbMethod.setFrame(False)
        self.label_2 = QLabel(self.containerSetting)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 70, 25))
        self.label_2.setMinimumSize(QSize(70, 25))
        self.label_2.setMaximumSize(QSize(70, 25))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")
        self.label_4 = QLabel(self.containerSetting)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 160, 70, 25))
        self.label_4.setMinimumSize(QSize(70, 25))
        self.label_4.setMaximumSize(QSize(70, 25))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"")
        self.txLong = QLineEdit(self.containerSetting)
        self.txLong.setObjectName(u"txLong")
        self.txLong.setGeometry(QRect(20, 80, 251, 25))
        self.txLong.setMinimumSize(QSize(20, 25))
        self.txLong.setMaximumSize(QSize(320, 16777215))
        self.txLong.setFont(font2)
        self.txLong.setStyleSheet(u"")
        self.txLong.setFrame(False)
        self.txUtc = QLineEdit(self.containerSetting)
        self.txUtc.setObjectName(u"txUtc")
        self.txUtc.setGeometry(QRect(20, 130, 71, 25))
        self.txUtc.setMinimumSize(QSize(20, 25))
        self.txUtc.setMaximumSize(QSize(320, 16777215))
        self.txUtc.setFont(font2)
        self.txUtc.setStyleSheet(u"")
        self.txUtc.setFrame(False)
        self.txLat = QLineEdit(self.containerSetting)
        self.txLat.setObjectName(u"txLat")
        self.txLat.setGeometry(QRect(20, 30, 251, 28))
        self.txLat.setMinimumSize(QSize(20, 25))
        self.txLat.setMaximumSize(QSize(320, 16777215))
        self.txLat.setFont(font2)
        self.txLat.setStyleSheet(u"")
        self.txLat.setFrame(False)
        self.txBeforeTime = QLineEdit(self.containerSetting)
        self.txBeforeTime.setObjectName(u"txBeforeTime")
        self.txBeforeTime.setGeometry(QRect(20, 253, 61, 25))
        self.label_7 = QLabel(self.containerSetting)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 254, 54, 21))
        self.ckNotification = QCheckBox(self.containerSetting)
        self.ckNotification.setObjectName(u"ckNotification")
        self.ckNotification.setGeometry(QRect(20, 230, 191, 23))
        self.ckJumah = QCheckBox(self.containerSetting)
        self.ckJumah.setObjectName(u"ckJumah")
        self.ckJumah.setGeometry(QRect(20, 280, 191, 23))
        self.txBeforeJumah = QLineEdit(self.containerSetting)
        self.txBeforeJumah.setObjectName(u"txBeforeJumah")
        self.txBeforeJumah.setGeometry(QRect(20, 303, 61, 25))
        self.label_8 = QLabel(self.containerSetting)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 306, 54, 21))
        self.label_22 = QLabel(self.frameSetting)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(50, 10, 81, 40))
        self.label_22.setMinimumSize(QSize(20, 20))
        self.label_22.setMaximumSize(QSize(9999, 9999))
        font9 = QFont()
        font9.setFamily(u"Ubuntu")
        font9.setPointSize(14)
        self.label_22.setFont(font9)
        self.label_22.setStyleSheet(u"")
        self.lblIconSetting = QLabel(self.frameSetting)
        self.lblIconSetting.setObjectName(u"lblIconSetting")
        self.lblIconSetting.setGeometry(QRect(20, 10, 31, 40))
        self.lblIconSetting.setMinimumSize(QSize(30, 30))
        self.lblIconSetting.setMaximumSize(QSize(9999, 9999))
        self.lblIconSetting.setFont(font9)
        self.lblIconSetting.setStyleSheet(u"")
        self.frameSettingBottom = QFrame(self.frameSetting)
        self.frameSettingBottom.setObjectName(u"frameSettingBottom")
        self.frameSettingBottom.setGeometry(QRect(0, 271, 321, 191))
        self.frameSettingBottom.setStyleSheet(u"#frameSettingBottom{\n"
"	background-color:#f6f6f6;\n"
"}")
        self.frameSettingBottom.setFrameShape(QFrame.StyledPanel)
        self.frameSettingBottom.setFrameShadow(QFrame.Raised)
        self.frameSettingBottom.raise_()
        self.containerSetting.raise_()
        self.label_22.raise_()
        self.lblIconSetting.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.txLat, self.txLong)
        QWidget.setTabOrder(self.txLong, self.txUtc)
        QWidget.setTabOrder(self.txUtc, self.cbMathhab)
        QWidget.setTabOrder(self.cbMathhab, self.cbMethod)
        QWidget.setTabOrder(self.cbMethod, self.ckStartTray)
        QWidget.setTabOrder(self.ckStartTray, self.ckNotification)
        QWidget.setTabOrder(self.ckNotification, self.txBeforeTime)
        QWidget.setTabOrder(self.txBeforeTime, self.ckJumah)
        QWidget.setTabOrder(self.ckJumah, self.txBeforeJumah)
        QWidget.setTabOrder(self.txBeforeJumah, self.btnPlay)
        QWidget.setTabOrder(self.btnPlay, self.btnStop)
        QWidget.setTabOrder(self.btnStop, self.btnSave)
        QWidget.setTabOrder(self.btnSave, self.btnTimeTable)
        QWidget.setTabOrder(self.btnTimeTable, self.btnSetting)
        QWidget.setTabOrder(self.btnSetting, self.btnHide)
        QWidget.setTabOrder(self.btnHide, self.btnExit)

        self.retranslateUi(MainWindow)
        self.ckJumah.toggled.connect(self.label_8.setVisible)
        self.ckJumah.toggled.connect(self.txBeforeJumah.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AyoShalat", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"AyoShalat", None))
#endif // QT_CONFIG(tooltip)
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"UPCOMING PRAYER", None))
        self.lblUpcomingWaktu.setText(QCoreApplication.translate("MainWindow", u"Upcoming", None))
        self.lblUpcomingJam.setText(QCoreApplication.translate("MainWindow", u"12:00", None))
        self.lblRemaining.setText(QCoreApplication.translate("MainWindow", u"remaining in hours", None))
        self.lblCurrentWaktu.setText(QCoreApplication.translate("MainWindow", u"Current", None))
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
#if QT_CONFIG(tooltip)
        self.btnTimeTable.setToolTip(QCoreApplication.translate("MainWindow", u"Show time table", None))
#endif // QT_CONFIG(tooltip)
        self.btnTimeTable.setText(QCoreApplication.translate("MainWindow", u"Prayer", None))
#if QT_CONFIG(tooltip)
        self.btnSetting.setToolTip(QCoreApplication.translate("MainWindow", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.btnSetting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
#if QT_CONFIG(tooltip)
        self.btnHide.setToolTip(QCoreApplication.translate("MainWindow", u"Hide current window", None))
#endif // QT_CONFIG(tooltip)
        self.btnHide.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
#if QT_CONFIG(tooltip)
        self.btnExit.setToolTip(QCoreApplication.translate("MainWindow", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"UTC", None))
        self.btnPlay.setText(QCoreApplication.translate("MainWindow", u"Test Play", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.ckStartTray.setText(QCoreApplication.translate("MainWindow", u"Start in Tray", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mathab", None))
        self.cbMathhab.setItemText(0, QCoreApplication.translate("MainWindow", u"Shafi'i", None))
        self.cbMathhab.setItemText(1, QCoreApplication.translate("MainWindow", u"Hanafi", None))

        self.cbMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"Muslim World League", None))
        self.cbMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"Islamic Society of North America", None))
        self.cbMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"Egyptian General Authority of Survey", None))
        self.cbMethod.setItemText(3, QCoreApplication.translate("MainWindow", u"Umm al-Qura University", None))
        self.cbMethod.setItemText(4, QCoreApplication.translate("MainWindow", u"University of Islamic Sciences, Karachi", None))
        self.cbMethod.setItemText(5, QCoreApplication.translate("MainWindow", u"Institute of Geophysics, University of Tehran", None))
        self.cbMethod.setItemText(6, QCoreApplication.translate("MainWindow", u"Shia Ithna Ashari (Jafari)", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.ckNotification.setText(QCoreApplication.translate("MainWindow", u"Notification before pray time", None))
        self.ckJumah.setText(QCoreApplication.translate("MainWindow", u"Jum'ah Notification", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"minutes", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.lblIconSetting.setText("")
    # retranslateUi

