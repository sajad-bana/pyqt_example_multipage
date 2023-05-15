from PyQt6.QtWidgets import QMainWindow, QDialog
from ui_py.main import Ui_MainWindow
from run_ui_py.run_dialog import MyRunDialog


def open_dialog():
    dialog = QDialog()
    ui = MyRunDialog()
    ui.setupUi(dialog)
    dialog.exec()


class LibraryApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(open_dialog)
