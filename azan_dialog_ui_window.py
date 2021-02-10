from PySide6.QtWidgets import QDial, QDialog, QMainWindow
from azan_dialog_ui import Ui_AzanDialog


class AzanDialogUiWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_AzanDialog
        # self.ui.setupUi(self)
