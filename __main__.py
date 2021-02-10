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

    # set icon
    # current_directory = str(pathlib.Path(__file__).parent.absolute())
    # icopath = current_directory + '/icon/masjid.xpm'
    # window.setWindowIcon(QIcon(icopath))

    # set window in center of screen
    # window.setGeometry(app.primaryScreen().geometry().getRect().)
    screen = app.primaryScreen().geometry().getRect()
    win = window.geometry().getRect()
    window.setGeometry((screen[2]/2)-(win[2]/2),(screen[3]/2)-(win[3]/2),0,0)
    
    
    window.show()
    window.runningme()
    app.exec_()
    os._exit(0)
    # sys.exit()
