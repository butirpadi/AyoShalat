# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import QCursor, QIcon
from azanplay import AzanPlay
from PySide6.QtWidgets import QDialog, QFrame, QMainWindow, QMenu, QMessageBox, QPushButton, QSystemTrayIcon
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
from plyer import notification


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
        self.ui.btnExit.clicked.connect(self.do_close)
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
        self.default_azan_wav = self.current_directory + '/audio/azan.wav'
        self.default_notif = self.current_directory + '/audio/hayyalashala.mp3'
        self.default_notif_wav = self.current_directory + '/audio/hayyalashala.wav'

        # image dialog
        azandialog = QDialog(self, Qt.FramelessWindowHint)
        azandialog.setWindowTitle("It's time to Shalat")
        self.azanDialog = azandialog
        btnDialog = QPushButton("", self.azanDialog)
        btnDialog.setFlat(True)
        btnDialog.clicked.connect(self.azanDialog.hide)

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

    def do_close(self):
        if QMessageBox().question(self, 'Close', 'Are you sure ?', QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes:
            self.qtray.hide()
            self.qtray.deleteLater()
            self.deleteLater()
            os._exit(0)

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
        self.ui.frameSetting.raise_()

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
            exit_menu.triggered.connect(self.do_close)

            # create tray icon
            self.qtray = QSystemTrayIcon(self)

            self.qtray.setIcon(QIcon(self.icopath))
            self.qtray.setVisible(True)
            self.qtray.setContextMenu(traymenu)
            self.qtray.show()

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
            'before_jumah_time': self.ui.txBeforeJumah.text().strip(),
            'enable_jumah_notification': str(self.ui.ckJumah.isChecked()),
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

    # active_time fajr = 1
    def set_color_prayer_time_frame(self, active_time):
        normal_style = "border-style:solid;border-radius:0px;border-bottom:1px solid whitesmoke;"
        active_style = normal_style + "background-color:rgb(252, 210, 93);"

        normal_style = ".QFrame{" + normal_style + "}"
        active_style = ".QFrame{" + active_style + "}"

        # clear
        self.ui.frameFajr.setStyleSheet(normal_style)
        self.ui.frameDhuhr.setStyleSheet(normal_style)
        self.ui.frameAsr.setStyleSheet(normal_style)
        self.ui.frameMaghrib.setStyleSheet(normal_style)
        self.ui.frameIsya.setStyleSheet(normal_style)

        if active_time == 1:
            self.ui.frameFajr.setStyleSheet(active_style)
        if active_time == 2:
            self.ui.frameDhuhr.setStyleSheet(active_style)
        if active_time == 3:
            self.ui.frameAsr.setStyleSheet(active_style)
        if active_time == 4:
            self.ui.frameMaghrib.setStyleSheet(active_style)
        if active_time == 5:
            self.ui.frameIsya.setStyleSheet(active_style)

    def show_prayer_time_info(self):
        # show current prayer time info
        # get current time
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")

        # if now == self.time_array['fajr'].strip():
        #     self.ui.lblCurrentWaktu.setText('Subh')
        #     self.set_color_prayer_time_frame(1)
        # elif now == self.time_array['dhuhr'].strip():
        #     self.ui.lblCurrentWaktu.setText('dhuhr')
        #     self.set_color_prayer_time_frame(2)
        # elif now == self.time_array['asr'].strip():
        #     self.ui.lblCurrentWaktu.setText('Asr')
        #     self.set_color_prayer_time_frame(3)
        # elif now == self.time_array['maghrib'].strip():
        #     self.ui.lblCurrentWaktu.setText('Maghrib')
        #     self.set_color_prayer_time_frame(4)
        # elif now == self.time_array['isha'].strip():
        #     self.ui.lblCurrentWaktu.setText('Isya`')
        #     self.set_color_prayer_time_frame(5)

        # subh
        subh = self.time_array['fajr'].strip()
        dhuhr = self.time_array['dhuhr'].strip()
        asr = self.time_array['asr'].strip()
        maghrib = self.time_array['maghrib'].strip()
        isya = self.time_array['isha'].strip()

        subh_date_str = str(current_time.year) + '/' + str(current_time.strftime(
            '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + subh + ':00'
        subh_date = datetime.datetime.strptime(
            subh_date_str, '%Y/%m/%d %H:%M:%S')

        # dhuhr
        dhuhr_date_str = str(current_time.year) + '/' + str(current_time.strftime(
            '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + dhuhr + ':00'
        dhuhr_date = datetime.datetime.strptime(
            dhuhr_date_str, '%Y/%m/%d %H:%M:%S')

        # asr
        asr_date_str = str(current_time.year) + '/' + str(current_time.strftime(
            '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + asr + ':00'
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

        # show upcoming
        if current_time >= subh_date and current_time <= dhuhr_date:
            self.ui.lblUpcomingWaktu.setText("Dhuhr")
            self.ui.lblUpcomingJam.setText(self.time_array['dhuhr'])
            self.ui.lblCurrentWaktu.setText('Subh')
            self.show_remaining_time()
            self.set_color_prayer_time_frame(1)

        if current_time >= dhuhr_date and current_time <= asr_date:
            self.ui.lblUpcomingWaktu.setText("Asr")
            self.ui.lblUpcomingJam.setText(self.time_array['asr'])
            self.ui.lblCurrentWaktu.setText('Duhr')
            self.show_remaining_time()
            self.set_color_prayer_time_frame(2)

        if current_time >= asr_date and current_time <= maghrib_date:
            self.ui.lblUpcomingWaktu.setText("Maghrib")
            self.ui.lblUpcomingJam.setText(self.time_array['maghrib'])
            self.ui.lblCurrentWaktu.setText('Asr')
            self.show_remaining_time()
            self.set_color_prayer_time_frame(3)

        if current_time >= maghrib_date and current_time <= isya_date:
            self.ui.lblUpcomingWaktu.setText("Isya")
            self.ui.lblUpcomingJam.setText(self.time_array['isha'])
            self.ui.lblCurrentWaktu.setText('Maghrib')
            self.show_remaining_time()
            self.set_color_prayer_time_frame(4)

        # if current_time >= isya_date and current_time <= subh_date:
        if current_time >= isya_date:
            self.ui.lblUpcomingWaktu.setText("Subh")
            self.ui.lblUpcomingJam.setText(self.time_array['fajr'])
            self.ui.lblCurrentWaktu.setText('Isya')
            self.show_remaining_time()
            self.set_color_prayer_time_frame(5)

    def show_remaining_time(self):
        current_time = datetime.datetime.now()
        subh = self.time_array['fajr'].strip()
        dhuhr = self.time_array['dhuhr'].strip()
        asr = self.time_array['asr'].strip()
        maghrib = self.time_array['maghrib'].strip()
        isya = self.time_array['isha'].strip()

        subh_date_str = str(current_time.year) + '/' + str(current_time.strftime(
            '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + subh + ':00'
        subh_date = datetime.datetime.strptime(
            subh_date_str, '%Y/%m/%d %H:%M:%S')

        # dhuhr
        dhuhr_date_str = str(current_time.year) + '/' + str(current_time.strftime(
            '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + dhuhr + ':00'
        dhuhr_date = datetime.datetime.strptime(
            dhuhr_date_str, '%Y/%m/%d %H:%M:%S')

        # asr
        asr_date_str = str(current_time.year) + '/' + str(current_time.strftime(
            '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + asr + ':00'
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
        # show upcoming
        if current_time >= subh_date and current_time <= dhuhr_date:
            remaining_hours = int(self.get_remaining_second(current_time, dhuhr_date)//3600)
            remaining_minutes = int((self.get_remaining_second(current_time, dhuhr_date)//60) % 60)

        if current_time >= dhuhr_date and current_time <= asr_date:
            remaining_hours = int(self.get_remaining_second(current_time, asr_date)//3600)
            remaining_minutes = int((self.get_remaining_second(current_time, asr_date)//60) % 60)

        if current_time >= asr_date and current_time <= maghrib_date:
            remaining_hours = int(self.get_remaining_second(current_time, maghrib_date)//3600)
            remaining_minutes = int((self.get_remaining_second(current_time, maghrib_date)//60) % 60)

        if current_time >= maghrib_date and current_time <= isya_date:
            remaining_hours = int(self.get_remaining_second(current_time, isya_date)//3600)
            remaining_minutes = int((self.get_remaining_second(current_time, isya_date)//60) % 60)

        # if current_time >= isya_date and current_time <= subh_date:
        if current_time >= isya_date or current_time <= subh_date:
            subh_date = subh_date + datetime.timedelta(days=1)
            remaining_hours = int(self.get_remaining_second(current_time, subh_date)//3600)
            remaining_minutes = int((self.get_remaining_second(current_time, subh_date)//60) % 60)

        remaining_str = f'{remaining_hours} hours and ' if (remaining_hours) else ''        
        remaining_str += f'{remaining_minutes} minutes to go'

        self.ui.lblRemaining.setText(remaining_str)

    def do_calculate(self):
        while True:
            time.sleep(1)

            # update time every time
            self.init_times_new()

            self.showTimes()

            self.show_remaining_time()

            # Check Azan Time
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M")
            if now == self.time_array['fajr'].strip() or now == self.time_array['dhuhr'].strip() or now == self.time_array['asr'].strip() or now == self.time_array['maghrib'].strip() or now == self.time_array['isha'].strip():
                self.playAzan()
                # self.show_current_prayer_time()
                self.show_prayer_time_info()
                time.sleep(60)
            # -----------------------------------------------------------------------

            # checking for jumah notification
            # friday is 4
            if current_time.weekday() == 4:
                if self.enable_jumah_notification:
                    # dhuhr
                    dhuhr_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                        '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + self.time_array['dhuhr'].strip() + ':00'
                    dhuhr_date = datetime.datetime.strptime(
                        dhuhr_date_str, '%Y/%m/%d %H:%M:%S')

                    if self.get_remaining_time(current_time, dhuhr_date) == int(self.before_jumah_time):
                        self.playNotif('Jum`ah')
                        time.sleep(75)

            # checking notification before pray time
            if self.enable_notification_before:

                # subh
                subh_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + self.time_array['fajr'].strip() + ':00'
                subh_date = datetime.datetime.strptime(
                    subh_date_str, '%Y/%m/%d %H:%M:%S')

                # dhuhr
                dhuhr_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + self.time_array['dhuhr'].strip() + ':00'
                dhuhr_date = datetime.datetime.strptime(
                    dhuhr_date_str, '%Y/%m/%d %H:%M:%S')

                # asr
                asr_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + self.time_array['asr'].strip() + ':00'
                asr_date = datetime.datetime.strptime(
                    asr_date_str, '%Y/%m/%d %H:%M:%S')

                # asr
                maghrib_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + self.time_array['maghrib'].strip() + ':00'
                maghrib_date = datetime.datetime.strptime(
                    maghrib_date_str, '%Y/%m/%d %H:%M:%S')

                # isya
                isya_date_str = str(current_time.year) + '/' + str(current_time.strftime(
                    '%m')) + '/' + str(current_time.strftime('%d')) + ' ' + self.time_array['isha'].strip() + ':00'
                isya_date = datetime.datetime.strptime(
                    isya_date_str, '%Y/%m/%d %H:%M:%S')

                if self.get_remaining_time(current_time, subh_date) == int(self.before_pray_time):
                    self.playNotif('Fajr')
                    time.sleep(75)

                if self.get_remaining_time(current_time, dhuhr_date) == int(self.before_pray_time):
                    self.playNotif('Dhuhr')
                    time.sleep(75)

                if self.get_remaining_time(current_time, asr_date) == int(self.before_pray_time):
                    self.playNotif('Asr')
                    time.sleep(75)

                if self.get_remaining_time(current_time, maghrib_date) == int(self.before_pray_time):
                    self.playNotif('Maghrib')
                    time.sleep(75)

                if self.get_remaining_time(current_time, isya_date) == int(self.before_pray_time):
                    self.playNotif('Isya')
                    time.sleep(75)

    def get_remaining_second(self, time_1, time_2):
        time_delta = (time_2 - time_1)
        return time_delta.total_seconds()  # in seconds

    def get_remaining_time(self, time_1, time_2):
        # in minutes
        return round(self.get_remaining_second(time_1, time_2)/60)

    def runningme(self):
        # do some stuff
        self.show_prayer_time_info()
        self.docalc.start()

    def showImageAzan(self):
        image_dir = self.current_directory + '/images'
        filename = random.choice(os.listdir(image_dir))

        image_path = image_dir + '/' + filename
        im = Image.open(image_path)
        im_width, im_height = im.size
        im_width -= 75
        im_height -= 75
        self.azanDialog.resize(im_width, im_height)

        im_width -= 10
        im_height -= 10

        print('showing azan dialog')
        btnDialog = self.azanDialog.children()[0]
        btnDialog.setGeometry(5, 5, im_width, im_height)
        styleBg = "border-image: url('" + image_path + \
            "') 0 0 0 0 stretch stretch;"
        btnDialog.setStyleSheet(styleBg)
        self.azanDialog.show()

    def stopAzan(self):
        try:
            self.azanplay.stop()
        except AttributeError as ae:
            print(ae)

    def stopNotif(self):
        self.notifplay.stop()

    def playAzan(self):
        self.threadAzan = threading.Thread(
            target=self._playAzan, name="Play Azan")

        self.threadAzan.start()
        self.showImageAzan()

    def playNotif(self, time_string):
        notification.notify(title="It's time to Shalat.", message=str(
            self.before_pray_time) + " minutes before " + time_string + ' prayer time.', timeout=10)
        self.threadNotif = threading.Thread(
            target=self._playNotif, name="Play Notif")

        self.threadNotif.start()

    def _playAzan(self):
        try:
            self.azanplay.stop()
            self.azanplay = AzanPlay(self.default_azan_wav)
            self.azanplay.play()
        except AttributeError:
            self.azanplay = AzanPlay(self.default_azan_wav)
            self.azanplay.play()

    def _playNotif(self):
        try:
            self.notifplay.stop()
            self.notifplay = AzanPlay(self.default_notif_wav)
            self.notifplay.play()
        except AttributeError:
            self.notifplay = AzanPlay(self.default_notif_wav)
            self.notifplay.play()

    def showTimes(self):
        # show label current date name
        self.ui.lblTodayName.setText(
            'Today / ' + datetime.datetime.now().strftime('%A'))
        self.ui.lblTodayDate.setText(
            datetime.datetime.now().strftime('%d %B %Y / %H:%M'))
        self.ui.lblSunset.setText(self.time_array['sunset'])
        self.ui.lblSunrise.setText(self.time_array['sunrise'])

        # using new calculation module
        self.ui.txFajr.setText(self.time_array['fajr'].strip())
        self.ui.txDhuhr.setText(self.time_array['dhuhr'].strip())
        self.ui.txAshr.setText(self.time_array['asr'].strip())
        self.ui.txMaghrib.setText(self.time_array['maghrib'].strip())
        self.ui.txIsya.setText(self.time_array['isha'].strip())

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

            # latitude
            self.latitude = setting_lines['latitude'] or -7.502814765426055

            # longitude
            self.longitude = setting_lines['longitude'] or 112.71057820736571

            # utc
            self.utc_offset = setting_lines['utc_offset'] or 7

            # calculation method
            self.calculation_method_index = int(
                setting_lines['calculation_method_index']) or 0

            self.calculation_method = self.calculation_method_array[int(
                self.calculation_method_index)]

            # time format
            self.time_format = setting_lines['time_format'] or '24h'

            # mathhab
            self.mathhab_index = int(setting_lines['mathhab_index']) or 0

            self.mathhab = self.mathhab_array[int(self.mathhab_index)]

            self.before_pray_time = setting_lines['before_pray_time']
            self.enable_notification_before = strtobool(
                setting_lines['enable_notification_before'])
            self.enable_jumah_notification = strtobool(
                setting_lines['enable_jumah_notification'])
            self.before_jumah_time = setting_lines['before_jumah_time']

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
            self.ui.txBeforeJumah.setText(str(self.before_jumah_time))
            self.ui.ckJumah.setChecked(self.enable_jumah_notification)

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
                    'enable_jumah_notification': "False",
                    'before_jumah_time': 0,
        }
        self.db.insert(item)

    # def show_current_prayer_time(self):
    #     current_time = datetime.datetime.now()

    def closeEvent(self, event):
        self.qtray.hide()
        self.qtray.deleteLater()
        self.deleteLater()

    def reformat_ui(self):
        self.ui.txBeforeTime.hide()
        self.ui.label_7.hide()
        self.ui.txBeforeJumah.hide()
        self.ui.label_8.hide()

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

        self.ui.label_11.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/alarm_on-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.label_14.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/alarm_on-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.label_17.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/alarm_on-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.label_20.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/alarm_on-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.label_23.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/alarm_on-24px.svg');\n"
                                       "background-repeat:no-repeat;\n"
                                       "background-position:right center;")

        self.ui.lblIconSetting.setStyleSheet(u"background-image:url('" + self.current_directory + "/icon/settings-24px-white.svg');\n"
                                             "background-repeat:no-repeat;\n"
                                             "background-position:left center;")

        icon1 = QIcon()
        icon1.addFile(self.current_directory + u"/icon/date_range-24px.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.ui.btnTimeTable.setIcon(icon1)
        self.ui.btnTimeTable.setCursor(QCursor(Qt.PointingHandCursor))

        icon2 = QIcon()
        icon2.addFile(self.current_directory + u"/icon/settings-24px.svg",
                      QSize(), QIcon.Normal, QIcon.On)
        self.ui.btnSetting.setIcon(icon2)
        self.ui.btnSetting.setCursor(QCursor(Qt.PointingHandCursor))

        icon3 = QIcon()
        icon3.addFile(self.current_directory +
                      u"/icon/hide_source-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.ui.btnHide.setIcon(icon3)
        self.ui.btnHide.setCursor(QCursor(Qt.PointingHandCursor))

        icon4 = QIcon()
        icon4.addFile(self.current_directory +
                      u"/icon/exit_to_app-24px.svg", QSize(), QIcon.Normal, QIcon.On)
        self.ui.btnExit.setIcon(icon4)
        self.ui.btnExit.setCursor(QCursor(Qt.PointingHandCursor))

        self.ui.containerSetting.setStyleSheet(u".QLineEdit{\n"
                                               "	border:none;\n"
                                               "	border-radius:0px;\n"
                                               "	background-color:whitesmoke;\n"
                                               "	border-bottom:1px solid gray;\n"
                                               "}\n"
                                               ".QLineEdit:focus{\n"
                                               "	background-color:rgb(255, 186, 97);\n"
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
                                               "	border-bottom:1px solid gray;\n"
                                               "	selection-color: black;\n"
                                               "      selection-background-color: rgb(255, 186, 97);\n"
                                               "}\n"
                                               ".QComboBox:focus{\n"
                                               "	background-color:rgb(255, 186, 97);\n"
                                               "}\n"
                                               "\n"
                                               ".QComboBox::drop-down:button{\n"
                                               "	background-color: rgb(234,234,234);\n"
                                               "	width:25px;\n"
                                               "background-image:url('" + self.current_directory +
                                               "/icon/expand_more-24px.svg')\n"
                                               "}")
