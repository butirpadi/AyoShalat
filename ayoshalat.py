# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import QIcon
from azanplay import AzanPlay
from PySide6.QtWidgets import QDialog, QFrame, QMainWindow, QMenu, QPushButton, QSystemTrayIcon
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
from tinydb import TinyDB, Query as TinyQuery
from distutils.util import strtobool


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

        if os.name == 'nt':
            self.current_directory = str(pathlib.Path(
                __file__).parent.absolute()).replace('\\', '/')
        else:
            self.current_directory = str(
                pathlib.Path(__file__).parent.absolute())

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
        self.ui.ckNotification.toggled.connect(self.toggle_check_notification)

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
        self.default_notif = self.current_directory + '/audio/hayyalashala.mp3'

        # OPEN SETTING ON START
        self.open_setting()

        # init thread
        self.docalc = threading.Thread(
            target=self.do_calculate, name="Azan Calculating")
        self.threadAzan = threading.Thread(
            target=self._playAzan, name="Play Azan")
        self.threadNotif = threading.Thread(
            target=self._playNotif, name="Play Notif")

        self.init_times_new()

        # show times
        self.showTimes()

        # show tray on start
        self.show_tray()

        # ---------------------------------------------------------------------------------------------------------------------

    def toggle_check_notification(self):
        # toggle enable of txNotification
        if self.ui.ckNotification.isChecked():
            self.ui.txBeforeTime.show()
            self.ui.label_7.show()
        else:
            self.ui.txBeforeTime.hide()
            self.ui.label_7.hide()

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
        # save setting to tinydb
        if self.ui.ckStartTray.isChecked():
            is_open_in_tray = 'True'
        else:
            is_open_in_tray = 'False'
        vals = {
            'open_in_tray': is_open_in_tray,
            'latitude': self.ui.txLat.text().strip(),
            'longitude': self.ui.txLong.text().strip(),
            'utc_offset': self.ui.txUtc.text().strip(),
            'calculation_method_index': str(self.ui.cbMethod.currentIndex()),
            'time_format': '24h',
            'mathhab_index': str(self.ui.cbMathhab.currentIndex()),
            'before_pray_time': self.ui.txBeforeTime.text().strip(),
            'enable_notification_before': str(self.ui.ckNotification.isChecked()),
        }
        pprint(vals)
        # setting_lines  = self.db.search(self.TinyData.code == 'setting')
        # for setting in setting_lines:

        #     setting['latitude'] = self.ui.txLat.text().strip()
        #     setting['longitude'] = self.ui.txLong.text().strip()
        #     setting['utc_offset'] = self.ui.txUtc.text().strip()
        #     setting['calculation_method_index'] = str(self.ui.cbMethod.currentIndex())
        #     setting['time_format'] = '24h'
        #     setting['mathhab_index'] = str(self.ui.cbMathhab.currentIndex())

        self.db.update(vals, self.TinyData.code == 'setting')

        # reload setting
        self.open_setting()
        self.init_times_new()
        self.showTimes()

    def do_calculate(self):
        while True:
            time.sleep(1)

            # update time every time
            self.init_times_new()

            # get current time
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M")

            subh = self.time_array['fajr'].strip()
            duhr = self.time_array['dhuhr'].strip()
            ashr = self.time_array['asr'].strip()
            maghrib = self.time_array['maghrib'].strip()
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

            # -----------------------------------------------------------------------

            # checking notification before pray time
            if self.enable_notification_before:
                current_time = datetime.datetime.now()

                # subh
                subh_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + subh + ':00'
                subh_date = datetime.datetime.strptime(
                    subh_date_str, '%Y/%m/%d %H:%M:%S')

                # duhr
                duhr_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + duhr + ':00'
                duhr_date = datetime.datetime.strptime(
                    duhr_date_str, '%Y/%m/%d %H:%M:%S')

                # asr
                asr_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + ashr + ':00'
                asr_date = datetime.datetime.strptime(
                    asr_date_str, '%Y/%m/%d %H:%M:%S')

                # asr
                maghrib_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + maghrib + ':00'
                maghrib_date = datetime.datetime.strptime(
                    maghrib_date_str, '%Y/%m/%d %H:%M:%S')

                # isya
                isya_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + isya + ':00'
                isya_date = datetime.datetime.strptime(
                    isya_date_str, '%Y/%m/%d %H:%M:%S')

                if self.get_remaining_time(current_time, subh_date) == int(self.before_pray_time):
                    self.playNotif()
                    time.sleep(75)

                if self.get_remaining_time(current_time, duhr_date) == int(self.before_pray_time):
                    self.playNotif()
                    time.sleep(75)

                if self.get_remaining_time(current_time, asr_date) == int(self.before_pray_time):
                    self.playNotif()
                    time.sleep(75)

                if self.get_remaining_time(current_time, maghrib_date) == int(self.before_pray_time):
                    self.playNotif()
                    time.sleep(75)

                if self.get_remaining_time(current_time, isya_date) == int(self.before_pray_time):
                    self.playNotif()
                    time.sleep(75)

    def get_remaining_time(self, time_1, time_2):
        time_delta = (time_2 - time_1)
        total_seconds = time_delta.total_seconds()
        minutes = round(total_seconds/60)
        return minutes

    def runningme(self):
        # do some stuff
        self.docalc.start()

    def exit(self):
        # self.docalc._stop().set()
        print('--------------exiting---------------')
        os._exit(0)

    def showImageAzan(self):
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
        azanui.resize(im_width, im_height)
        azanui.setWindowFlags(Qt.FramelessWindowHint)

        azanuiFrame = QFrame(azanui)
        azanuiFrame.setGeometry(0, 0, im_width, im_height)

        btnDialog = QPushButton("", azanuiFrame)
        btnDialog.setGeometry(0, 0, im_width, im_height)
        btnDialog.setStyleSheet("{border:none;border-style:outline;}")
        btnDialog.setFlat(True)
        btnDialog.clicked.connect(azanui.hide)

        azanui.exec_()

    def stopAzan(self):
        # self.azanThread.terminate()
        self.azanpy.stop()
        # del self.azanpy

    def stopNotif(self):
        # self.azanThread.terminate()
        self.notifplay.stop()
        # del self.azanpy

    def playAzan(self):
        # if threading.current_thread().isAlive():
        if self.threadAzan.isAlive():
            self.threadAzan = threading.Thread(
                target=self._playAzan, name="Play Azan")

        self.threadAzan.start()
        self.showImageAzan()

    def playNotif(self):
        if threading.current_thread().isAlive():
            self.threadAzan = threading.Thread(
                target=self._playNotif, name="Play Notif")

        self.threadNotif.start()
        # self.showImageAzan()

    def _playAzan(self):
        if os.name == 'nt':
            self.azanpy = AzanPlay(self.default_azan)
            self.azanpy.play()
        else:
            # play azan
            try:
                self.azanpy.play()
            except AttributeError:
                self.azanpy = AzanPlay(self.default_azan)
                self.azanpy.play()

    def _playNotif(self):
        if os.name == 'nt':
            self.notifplay = AzanPlay(self.default_notif)
            self.notifplay.play()
        else:
            # play azan
            try:
                self.notifplay.play()
            except AttributeError:
                self.notifplay = AzanPlay(self.default_notif)
                self.notifplay.play()

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

    def open_setting(self):
        # init database
        self.db = TinyDB('ayodb.json')
        self.TinyData = TinyQuery()

        # opening app setting
        try:
            setting_lines = self.db.search(self.TinyData.code == 'setting')[0]
        except IndexError:
            self.init_db()
            setting_lines = self.db.search(self.TinyData.code == 'setting')[0]

        # fileob = open(self.setting_file, 'r')
        # setting_lines = fileob.readlines()
        try:

            # open in tray
            self.open_in_tray = setting_lines['open_in_tray'] or 'False'
            # self.open_in_tray = setting_lines[0].split(
            #     ':')[1].strip() or 'False'

            # latitude
            # self.latitude = setting_lines[1].split(
            #     ':')[1].strip() or -7.502814765426055
            self.latitude = setting_lines['latitude'] or -7.502814765426055

            # longitude
            # self.longitude = setting_lines[2].split(
            #     ':')[1].strip() or 112.71057820736571
            self.longitude = setting_lines['longitude'] or 112.71057820736571

            # utc
            self.utc_offset = setting_lines['utc_offset'] or 7
            # self.utc_offset = setting_lines[3].split(':')[1].strip() or 7

            # calculation method
            self.calculation_method_index = int(
                setting_lines['calculation_method_index']) or 0
            # self.calculation_method_index = int(setting_lines[4].split(':')[
            #     1].strip()) or 0
            self.calculation_method = self.calculation_method_array[int(
                self.calculation_method_index)]
            # self.calculation_method = self.calculation_method_array[int(
            #     self.calculation_method_index)]

            # time format
            # self.time_format = setting_lines[5].split(':')[1].strip() or '24h'
            self.time_format = setting_lines['time_format'] or '24h'

            # mathhab
            self.mathhab_index = int(setting_lines['mathhab_index']) or 0
            # self.mathhab_index = int(setting_lines[6].split(':')[1].strip()) or 0

            self.mathhab = self.mathhab_array[int(self.mathhab_index)]

            self.before_pray_time = setting_lines['before_pray_time']
            print(setting_lines['enable_notification_before'])
            print(bool(setting_lines['enable_notification_before']))
            self.enable_notification_before = strtobool(
                setting_lines['enable_notification_before'])

            if self.open_in_tray == 'True':
                # self.hide()
                self.ui.ckStartTray.setChecked(True)
            # fileob.close()

            self.ui.txLat.setText(str(self.latitude))
            self.ui.txLong.setText(str(self.longitude))
            self.ui.txUtc.setText(str(self.utc_offset))
            self.ui.txBeforeTime.setText(str(self.before_pray_time))
            self.ui.cbMethod.setCurrentIndex(self.calculation_method_index)
            self.ui.cbMathhab.setCurrentIndex(self.mathhab_index)
            self.ui.ckNotification.setChecked(self.enable_notification_before)

        except KeyError:
            self.init_db()
            self.open_setting()

    def init_db(self):
        # delete first data
        self.db.remove(self.TinyData.code == 'setting')
        item = {
            'code': 'setting',
                    'open_in_tray': 'False',
                    'latitude': -7.502814765426055,
                    'longitude': 112.71057820736571,
                    'utc_offset': 7,
                    'calculation_method_index': 0,
                    'calculation_method': '',
                    'time_format': '24h',
                    'mathhab_index': 0,
                    'mathhab': '',
                    'enable_notification_before': "False",
                    'before_pray_time': 0,
        }
        self.db.insert(item)

    def show_current_prayer_time(self):
        current_time = datetime.datetime.now()

    def reformat_ui(self):
        self.ui.txBeforeTime.hide()
        self.ui.label_7.hide()

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
