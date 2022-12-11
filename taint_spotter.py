#setting = Setting object.

import sys
from functools import partial
from settings import Setting
from main_window import main_guiWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout
)

setting = Setting()
pycalcApp = QApplication(sys.argv)
gui_win = main_guiWindow(setting)

gui_win.show()
sys.exit(pycalcApp.exec())
