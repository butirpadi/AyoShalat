#! /usr/bin/python

from PySide6.QtWidgets import QApplication
from ayoshalat import AyoShalat
import init

if __name__ == "__main__":
    app = QApplication([])
    window = AyoShalat()
    init.init_setting(app,window)