# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QIcon
from azanplay import AzanPlay
from PySide6.QtWidgets import QDialog, QMainWindow, QMenu, QSystemTrayIcon, QWidget
from main_ui import Ui_MainWindow
import pathlib
import os
from pprint import pprint
import time
import datetime
import threading
# import pwd
import random
from PIL import Image
from prayertimes import PrayTimes
from multiprocessing import Process


class AyoShalat(QMainWindow):
    # +=========+===============================================+
    # | Method  | Description                                   |
    # +=========+===============================================+
    # | MWL     | Muslim World League                           |
    # +---------+-----------------------------------------------+
    # | ISNA    | Islamic Society of North America              |
    # +---------+-----------------------------------------------+
    # | Egypt   | Egyptian General Authority of Survey          |
    # +---------+-----------------------------------------------+
    # | Makkah  | Umm al-Qura University                        |
    # +---------+-----------------------------------------------+
    # | Karachi | University of Islamic Sciences, Karachi       |
    # +---------+-----------------------------------------------+
    # | Tehran  | Institute of Geophysics, University of Tehran |
    # +---------+-----------------------------------------------+
    # | Jafari  | Shia Ithna Ashari (Jafari)                    |
    # +---------+-----------------------------------------------+

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_directory = str(pathlib.Path(__file__).parent.absolute())
        self.reformat_ui()

        # set clicked
        self.ui.btnPlay.clicked.connect(self.playAzan)
        self.ui.btnStop.clicked.connect(self.stopAzan)
        # self.ui.btnHide.clicked.connect(self.openSetting)
        self.ui.btnHide.clicked.connect(self.hide)
        self.ui.btnExit.clicked.connect(self.exit)
        self.ui.btnSave.clicked.connect(self.do_save)
        self.ui.btnSetting.clicked.connect(self.show_frame_setting)
        self.ui.btnTimeTable.clicked.connect(self.show_time_table)

        self.calculation_method_array = ['MWL', 'ISNA',
                                         'Egypt', 'Makkah', 'Karachi', 'Tehran', 'Jafari']
        self.mathhab_array = ['Standard', 'Hanafi']

        # init form setting
        self.ui.frameSetting.setVisible(False)

        # get username of this login user
        # self.myusername = pwd.getpwuid(os.getuid()).pw_name

        # init icon
        self.setting_file = self.current_directory + '/setting.txt'
        self.icopath = self.current_directory + '/icon/masjid.xpm'
        self.setWindowIcon(QIcon(self.icopath))
        self.default_azan = self.current_directory + '/audio/azan.mp3'

        # OPEN SETTING ON START
        self.openSettingNew()

        # init thread
        self.docalc = threading.Thread(
            target=self.do_calculate, name="Azan Calculating")

        self.init_times_new()

        # show times
        self.showTimes()

        # show tray on start
        self.show_tray()

        # ---------------------------------------------------------------------------------------------------------------------

    def show_frame_setting(self):
        self.ui.frameSetting.setVisible(True)

    def show_time_table(self):
        self.ui.frameSetting.setVisible(False)

    def show_tray(self):
        if QSystemTrayIcon.isSystemTrayAvailable:
            # create tray menu
            traymenu = QMenu('AyoShalat', self)
            openwin_menu = traymenu.addAction('Show me!')
            openwin_menu.triggered.connect(self.show)

            playazan_menu = traymenu.addAction('Play Azan')
            playazan_menu.triggered.connect(self.playAzan)

            stop_azan_menu = traymenu.addAction('Stop Azan')
            stop_azan_menu.triggered.connect(self.stopAzan)

            traymenu.addSeparator()

            exit_menu = traymenu.addAction('Exit')
            exit_menu.triggered.connect(self.exit)

            # create tray icon
            qtray = QSystemTrayIcon(self)

            qtray.setIcon(QIcon(self.icopath))
            qtray.setVisible(True)
            qtray.setContextMenu(traymenu)
            qtray.show()

    def do_save(self):
        # using new module
        setting_lines = []

        if self.ui.ckStartTray.isChecked():
            print('tray is true')
            setting_lines.append('open_in_tray : True' + '\n')
        else:
            print('tray is false')
            setting_lines.append('open_in_tray : False' + '\n')

        setting_lines.append(
            'lat : ' + self.ui.txLat.text().strip() + '\n')
        setting_lines.append(
            'long : ' + self.ui.txLong.text().strip() + '\n')
        setting_lines.append('utc : ' + self.ui.txUtc.text().strip() + '\n')
        setting_lines.append(
            'method : ' + str(self.ui.cbMethod.currentIndex() ) + '\n')
        setting_lines.append(
            'time_format : 24h' +'\n')
        setting_lines.append(
            'mathhab : ' + str(self.ui.cbMathhab.currentIndex() ) + '\n')

        fileob = open(self.setting_file, 'w')

        for line in setting_lines:
            fileob.writelines(line)

        fileob.close()

        print('Save setting file app success')
        print('-------------------------')

        # reload setting
        self.openSettingNew()
        self.init_times_new()
        self.showTimes()

    def do_calculate(self):
        while True:
            time.sleep(1)

            # update time every time
            self.init_times_new()

            # get current time
            current_time = datetime.datetime.now()
            # now = current_time.strftime("%-H:%M:%S")
            # now = current_time.strftime("%-H:%M")
            # using padding with zero on hours
            now = current_time.strftime("%H:%M")
            # now_prec = current_time.strftime("%H:%M:%S")

            # self.times[1].strip()  # + ':00'
            subh = self.time_array['fajr'].strip()
            # self.times[3].strip()  # + ':00'
            duhr = self.time_array['dhuhr'].strip()
            # self.times[4].strip()  # + ':00'
            ashr = self.time_array['asr'].strip()
            # self.times[5].strip()  # + ':00'
            maghrib = self.time_array['maghrib'].strip()
            # self.times[6].strip()  # + ':00'
            isya = self.time_array['isha'].strip()

            if now == subh or now == duhr or now == ashr or now == maghrib or now == isya:
                self.playAzan()

                # show current prayer time info
                if now == subh:
                    self.ui.lblCurrentWaktu.setText('Subh')
                elif now == duhr:
                    self.ui.lblCurrentWaktu.setText('Duhr')
                elif now == ashr:
                    self.ui.lblCurrentWaktu.setText('Asr')
                elif now == maghrib:
                    self.ui.lblCurrentWaktu.setText('Maghrib')
                elif now == isya:
                    self.ui.lblCurrentWaktu.setText('Isya`')

                time.sleep(60)

    def runningme(self):
        # do some stuff
        self.docalc.start()

    def exit(self):
        # self.docalc._stop().set()
        print('--------------exiting---------------')
        os._exit(0)
    
    def showImageAzan(self):
        print('inside show image azan')
        image_dir = self.current_directory + '/images'
        filename = random.choice(os.listdir(image_dir))

        image_path = image_dir + '/' + filename
        im = Image.open(image_path)
        im_width, im_height = im.size
               # azanui = QDialog(f=Qt.FramelessWindowHint)
        azanui = QDialog()
        azanui.setWindowTitle("It's time to Shalat")
        azanui.setStyleSheet(
            "background-image:url('" + image_path + "');background-position: center;background-repeat: no-repeat;")
        azanui.resize(im_width,im_height)
        azanui.exec_()

    def stopAzan(self):
        self.azanThread.terminate()

    def playAzan(self):
        self.azanThread = Process(target=self._playAzan)
        self.azanThread.start()

        self.showImageAzan()
        
        # auto terminate after azan done
        time.sleep(180)
        self.azanThread.terminate()

    def _playAzan(self):        
        # play azan
        azanpy = AzanPlay(self.default_azan)
        azanpy.play()


    def showTimes(self):

        # show label current date name
        self.ui.lblTodayName.setText(
            'Today / ' + datetime.datetime.now().strftime('%A'))
        self.ui.lblTodayDate.setText(
            datetime.datetime.now().strftime('%d %B %Y') + ' / Hijri Date')
        self.ui.lblSunset.setText(self.time_array['sunset'])
        self.ui.lblSunrise.setText(self.time_array['sunrise'])

        # using new calculation module
        self.ui.txFajr.setText(self.time_array['fajr'].strip() + ':00')
        self.ui.txDhuhr.setText(self.time_array['dhuhr'].strip() + ':00')
        self.ui.txAshr.setText(self.time_array['asr'].strip() + ':00')
        self.ui.txMaghrib.setText(self.time_array['maghrib'].strip() + ':00')
        self.ui.txIsya.setText(self.time_array['isha'].strip() + ':00')

    def init_times_new(self):
        today = datetime.date.today()
        PT = PrayTimes('MWL')
        times = PT.get_times(today, (float(self.latitude), float(
            self.longitude)), float(self.utc_offset))
        self.time_array = times

    def openSettingNew(self):
        # opening app setting
        print('OPENING SETTING NEW')
        try:
            fileob = open(self.setting_file, 'r')
            setting_lines = fileob.readlines()

            # open in tray
            self.open_in_tray = setting_lines[0].split(
                ':')[1].strip() or 'False'
            # latitude
            self.latitude = setting_lines[1].split(
                ':')[1].strip() or -7.502814765426055
            # longitude
            self.longitude = setting_lines[2].split(
                ':')[1].strip() or 112.71057820736571
            # utc
            self.utc_offset = setting_lines[3].split(':')[1].strip() or 7
            # calculation method
            self.calculation_method_index = int(setting_lines[4].split(':')[
                1].strip()) or 0
            self.calculation_method = self.calculation_method_array[int(
                self.calculation_method_index)]
            # time format
            self.time_format = setting_lines[5].split(':')[1].strip() or '24h'
            # mathhab
            self.mathhab_index = int(setting_lines[6].split(':')[1].strip()) or 0
            self.mathhab = self.mathhab_array[int(self.mathhab_index)]

            if self.open_in_tray == 'True':
                # self.hide()
                self.ui.ckStartTray.setChecked(True)
            fileob.close()

            self.ui.txLat.setText(str(self.latitude))
            self.ui.txLong.setText(str(self.longitude))
            self.ui.txUtc.setText(str(self.utc_offset))
            self.ui.cbMethod.setCurrentIndex(self.calculation_method_index)
            self.ui.cbMathhab.setCurrentIndex(self.mathhab_index)

        except FileNotFoundError:
            print('error load setting')

    def show_current_prayer_time(self):
        current_time = datetime.datetime.now()

    def reformat_ui(self):
        icon = QIcon()
        icon.addFile(self.current_directory + u"/icon/masjid.xpm",
                     QSize(), QIcon.Normal, QIcon.Off)
        # MainWindow.setWindowIcon(icon)
        self.ui.centralwidget.setWindowIcon(icon)

        self.ui.frameSetting.setGeometry(QRect(-1, -1, 322, 461))
        self.ui.frameSetting.setStyleSheet(u"#frameSetting{\n"
                                           "	background-image:url('" + self.current_directory +
                                           "/icon/bg6-3.jpg');\n"
                                           "	background-position:center;\n"
                                           "}\n"
                                           ".QLabel{\n"
                                           "color:white;}\n")

        self.ui.frameDashboardUpper.setGeometry(QRect(-10, -1, 391, 271))
        self.ui.frameDashboardUpper.setStyleSheet(u"#frameDashboardUpper{\n"
                                                  "	background-image:url('" + self.current_directory +
                                                  "/icon/bg6-3.jpg');\n"
                                                  "	background-position:center;\n"

                                                  "}")

        self.ui.lblLocation.setStyleSheet(u"#lblLocation{\n"
                                          "	color:white;\n"
                                          "	background-image:url('" + self.current_directory +
                                          "/icon/location_on-24px.svg');\n"
                                          "background-position:center;\n"
                                          "}")

        self.ui.label_10.setStyleSheet(u".QLabel{\n"
                                       "	background-image:url('" + self.current_directory +
                                       "/icon/noun_Sea Sunset_395675.svg');\n"
                                       "	background-position:center;\n"
                                       "	background-repeat:no-repeat;\n"
                                       "}")

        self.ui.label_16.setStyleSheet(u".QLabel{\n"
                                       "	background-image:url('" + self.current_directory +
                                       "/icon/noun_Sunrise _395417.svg');\n"
                                       "	background-position:center;\n"
                                       "	background-repeat:no-repeat;\n"
                                       "}")

        self.ui.frame_4.setStyleSheet(u"#frame_4{\n"
                                      "	background-image:url('" + self.current_directory +
                                      "/icon/today-24px.svg');\n"
                                      "	background-repeat:no-repeat;\n"
                                      "	background-position:center;\n"
                                      "}")

        self.ui.label_11.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/notifications_none-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.label_14.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/notifications_none-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.label_17.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/notifications_none-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.label_20.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/notifications_none-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.label_23.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/notifications_none-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.lblIconSetting.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/settings-24px-white.svg');\n"
                                             "background-repeat:no-repeat;\n"
                                             "background-position:left center;")

        icon1 = QIcon()
        icon1.addFile(self.current_directory + u"/icon/date_range-24px.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.ui.btnTimeTable.setIcon(icon1)

        icon2 = QIcon()
        icon2.addFile(self.current_directory + u"/icon/settings-24px.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.ui.btnSetting.setIcon(icon2)

        icon3 = QIcon()
        icon3.addFile(self.current_directory +
                      u"/icon/hide_source-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.ui.btnHide.setIcon(icon3)

        icon4 = QIcon()
        icon4.addFile(self.current_directory +
                      u"/icon/exit_to_app-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.ui.btnExit.setIcon(icon4)
