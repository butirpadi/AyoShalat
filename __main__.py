import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from ayoshalat import AyoShalat
import os
import pathlib

if __name__ == "__main__":
    app = QApplication([])
    window = AyoShalat()

    # set icon
    current_directory = str(pathlib.Path(__file__).parent.absolute())
    icopath = current_directory + '/icon/masjid.xpm'
    window.setWindowIcon(QIcon(icopath))

    window.show()
    window.runningme()
    app.exec_()
    os._exit(0)
    # sys.exit()
