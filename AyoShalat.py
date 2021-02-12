#! /usr/bin/python

import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from ayoshalat import AyoShalat
import os
import pathlib
from pprint import pprint

if __name__ == "__main__":
    app = QApplication([])
    window = AyoShalat()

    # set window in center of screen
    # window.setGeometry(app.primaryScreen().geometry().getRect().)
    screen = app.primaryScreen().geometry().getRect()
    win = window.geometry().getRect()
    window.setGeometry((screen[2]/2)-(win[2]/2),(screen[3]/2)-(win[3]/2),0,0)
    start_in_tray = 'False'

    # open app setting
    try:
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        setting_file = current_directory + '/setting.txt'
        fileob = open(setting_file, 'r')
        setting_lines = fileob.readlines()

        start_in_tray = setting_lines[0].split(':')[1].strip()       

        # if open_in_tray == 'False':
        #     # self.hide()
        #     print('showing window')
        #     window.show()        
        fileob.close()
    except FileNotFoundError:
        print('error load setting')    
    
    if start_in_tray == 'False':
        window.show()
    else:
        window.show()
        window.hide()

    window.runningme()
    app.exec_()
    os._exit(0)
    # sys.exit()
