from ui_py.dialog import Ui_Dialog
from PyQt6 import QtWidgets


class MyRunDialog(Ui_Dialog):
    def __init__(self):
        self.dialog = None

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
