#setting = Setting object.

import sys
from time import sleep
from functools import partial
from settings import Setting
from main_window import main_guiWindow
from welcome_gui import welcome_screen
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QStackedWidget
)

setting = Setting()
pycalcApp = QApplication(sys.argv)
main_Widget = QStackedWidget()

gui_win = main_guiWindow(setting)
welcome_gui = welcome_screen()
gui_win.make_buttons()
# gui_win.show()
main_Widget.addWidget(welcome_gui)
main_Widget.addWidget(gui_win)
main_Widget.setGeometry(50, 50, 800, 600)
def flip_screen():
    main_Widget.setCurrentIndex(1)
main_Widget.show()
timer = QTimer()
timer.start(2000)
timer.timeout.connect(flip_screen)
sys.exit(pycalcApp.exec())