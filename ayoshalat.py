# This Python file uses the following encoding: utf-8
from azan_dialog_ui_window import AzanDialogUiWindow
from PySide6.QtGui import QIcon, Qt
from azanplay import AzanPlay
from PySide6.QtWidgets import QErrorMessage, QMainWindow, QMenu, QSystemTrayIcon, QWidget
from main_ui import Ui_MainWindow
import pathlib
import os
import io
import subprocess
from pprint import pprint
import time
import datetime
import threading
import pwd
import random
from PIL import Image


class AyoShalat(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set clicked
        self.ui.btnPlay.clicked.connect(self.playAzan)
        self.ui.btnStop.clicked.connect(self.stopAzan)
        # self.ui.btnHide.clicked.connect(self.openSetting)
        self.ui.btnHide.clicked.connect(self.hide)
        self.ui.btnExit.clicked.connect(self.exit)
        self.ui.btnSave.clicked.connect(self.do_save)

        # get username of this login user
        self.myusername = pwd.getpwuid(os.getuid()).pw_name

        # get time
        self.init_times()

        # init thread
        self.docalc = threading.Thread(
            target=self.do_calculate, name="Azan Calculating")

        # init icon
        self.current_directory = str(pathlib.Path(__file__).parent.absolute())
        self.setting_file = self.current_directory + '/setting.txt'
        self.icopath = self.current_directory + '/icon/masjid.xpm'
        self.setWindowIcon(QIcon(self.icopath))
        self.default_azan = self.current_directory + '/audio/azan.mp3'

        # open setting
        self.openSetting()

        # show times
        self.showTimes()

        # show tray on start
        self.show_tray()

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

    def init_times(self):
        opt = subprocess.Popen(['ipraytime', '--brief'],
                               stdout=subprocess.PIPE)
        timetable = io.TextIOWrapper(opt.stdout, encoding="utf-8")
        self.times = list(timetable)[2].split()

        # testing
        # self.times[6] = "10:17"

    def do_save(self):
        # checking input
        if not self.ui.txLat.text().isdigit():
            msg = QErrorMessage()
            msg.showMessage('Latitude in false type.')

        setting_lines = []
        setting_lines.append('City: city_name' + '\n')
        setting_lines.append(
            'Latitude: ' + self.ui.txLat.text().strip() + '\n')
        setting_lines.append(
            'Longitude: ' + self.ui.txLong.text().strip() + '\n')
        setting_lines.append('UTC: ' + self.ui.txUtc.text().strip() + '\n')
        setting_lines.append(
            'AngleMethod: ' + str(self.ui.cbMethod.currentIndex() + 1) + '\n')
        setting_lines.append(
            'Mathhab: ' + str(self.ui.cbMathhab.currentIndex() + 1) + '\n')
        setting_lines.append(
            'OffsetList: ' + '0 0 0 0 0 0' + '\n')

        fileob = open(r'/home/' + self.myusername + '/.iprayrc', 'w')

        for line in setting_lines:
            fileob.writelines(line)

        fileob.close()

        # save app setting
        setting_lines = []
        if self.ui.ckStartTray.isChecked():
            print('tray is true')
            setting_lines.append('open_in_tray : True' + '\n')
        else:
            print('tray is false')
            setting_lines.append('open_in_tray : False' + '\n')

        settingfile = open(self.setting_file, 'w')
        for line in setting_lines:
            print(line)
            settingfile.writelines(line)
        settingfile.close()
        print('Save setting file app success')
        print('-------------------------')

        # reload setting
        self.init_times()
        self.showTimes()

    def do_calculate(self):
        while True:
            time.sleep(1)
            # get current time
            current_time = datetime.datetime.now()
            # now = current_time.strftime("%-H:%M:%S")
            now = current_time.strftime("%-H:%M")
            now_prec = current_time.strftime("%-H:%M:%S")

            subh = self.times[1].strip()  # + ':00'
            duhr = self.times[3].strip()  # + ':00'
            ashr = self.times[4].strip()  # + ':00'
            maghrib = self.times[5].strip()  # + ':00'
            isya = self.times[6].strip()  # + ':00'            

            # print('subh "' + subh + '"')
            # print('dhuhr "' + duhr + '"')
            # print('ashr "' + ashr + '"')
            # print('maghrib "' + maghrib + '"')
            # print('isya "' + isya + '"')
            # print('NOW "' + now + '"')
            # print('NOW PREC"' + now_prec + '"')
            # print('------------------------------')
            # maghrib = "17:33"

            if now == subh or now == duhr or now == ashr or now == maghrib or now == isya:
                azanThread = threading.Thread(
                    target=self.playAzan, name="Azan Play")
                azanThread.start()
                time.sleep(60)

    def runningme(self):
        # do some stuff
        self.docalc.start()

    def exit(self):
        # self.docalc._stop().set()
        print('--------------exiting---------------')
        os._exit(0)

    def stopAzan(self):
        self.azanpy.stop()

    def playAzan(self):
        image_dir = self.current_directory + '/images'
        filename = random.choice(os.listdir(image_dir))

        image_path = image_dir + '/' + filename
        im = Image.open(image_path)
        im_width, im_height = im.size
        # show dialog info shalat
        azanui = AzanDialogUiWindow()
        azanui.setStyleSheet(
            "background-image:url('" + image_path + "');background-position: center;background-repeat: no-repeat;")
        # # # azanui.setParent(self)
        azanui.setFixedWidth(im_width)
        azanui.setFixedHeight(im_height)
        azanui.setWindowModality(Qt.ApplicationModal)
        azanui.setModal(True)
        azanui.show()

        self.azanpy = AzanPlay()
        self.azanpy.play(self.default_azan)

    def showTimes(self):
        self.ui.txFajr.setText(self.times[1] + ':00')
        self.ui.txDhuhr.setText(self.times[3] + ':00')
        self.ui.txAshr.setText(self.times[4] + ':00')
        self.ui.txMaghrib.setText(self.times[5] + ':00')
        self.ui.txIsya.setText(self.times[6] + ':00')

    def openSetting(self):
        # opening app setting
        try:
            fileob = open(self.setting_file, 'r')
            setting_lines = fileob.readlines()

            open_in_tray = setting_lines[0].split(':')[1].strip()

            if open_in_tray == 'True':
                # self.hide()
                self.ui.ckStartTray.setChecked(True)
            fileob.close()

        except FileNotFoundError:
            print('error load setting')

        try:
            fileob = open(r'/home/' + self.myusername + '/.iprayrc', 'r')
            lines = fileob.readlines()

            city = lines[0].split(':')[1].strip()
            lat = lines[1].split(':')[1].strip()
            long = lines[2].split(':')[1].strip()
            utc = lines[3].split(':')[1].strip()
            method = lines[4].split(':')[1].strip()
            mathhab = lines[5].split(':')[1].strip()
            # offset = lines[4].split(':')[1]

            self.ui.txLat.setText(lat)
            self.ui.txLong.setText(long)
            self.ui.txUtc.setText(utc)
            self.ui.cbMethod.setCurrentIndex(int(method)-1)
            self.ui.cbMathhab.setCurrentIndex(int(mathhab)-1)

            fileob.close()
        except FileNotFoundError:
            # init file setting
            setting_lines = []
            setting_lines.append('City: city_name' + '\n')
            setting_lines.append(
                'Latitude: -7.502814765426055\n')
            setting_lines.append(
                'Longitude: 112.71057820736571\n')
            setting_lines.append('UTC: 7\n')
            setting_lines.append(
                'AngleMethod: 5\n')
            setting_lines.append(
                'Mathhab: 1\n')
            setting_lines.append(
                'OffsetList: ' + '0 0 0 0 0 0' + '\n')

            fileob = open(r'/home/' + self.myusername + '/.iprayrc', 'w')

            for line in setting_lines:
                fileob.writelines(line)

            fileob.close()

            # open setting
            self.openSetting()
