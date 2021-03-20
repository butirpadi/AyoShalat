#! /usr/bin/python

from PySide6.QtWidgets import QApplication
from ayoshalat import AyoShalat
import os
import pathlib
from pprint import pprint
from tinydb import TinyDB,Query as TinyQuery

def init_setting(app,window):
    # set window in center of screen
    # window.setGeometry(app.primaryScreen().geometry().getRect().)
    screen = app.primaryScreen().geometry().getRect()
    win = window.geometry().getRect()
    window.setGeometry((screen[2]/2)-(win[2]/2),(screen[3]/2)-(win[3]/2),0,0)
    # window.setWindowFlags(Qt.FramelessWindowHint) # disable window decoration
    start_in_tray = 'False'

    # open app setting
    db = TinyDB('ayodb.json')
    TinyData = TinyQuery()
    if len(db.all()) == 0:
        # init database
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
                'enable_notification_before' : "False",
                'before_pray_time': 0,
                'enable_jumah_notification': "False",
                'before_jumah_time': 0,
            }
        db.insert(item)
    setting_lines  = db.search(TinyData.code == 'setting')[0]
    start_in_tray = setting_lines['open_in_tray']

    if start_in_tray == 'False':
        window.show()

    window.runningme()
    app.exec_()
    os._exit(0)

    


