#setting = Setting object.

import sys
from time import sleep
from functools import partial
from settings import Setting
from main_window import main_guiWindow
from welcome_gui import welcome_screen
import app_functions as app_functions
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
# gui_win.make_buttons()
# gui_win.show()
main_Widget.addWidget(welcome_gui)
main_Widget.addWidget(gui_win)
main_Widget.setGeometry(50, 50, 800, 600)
def flip_screen():
    main_Widget.setCurrentIndex(1)
    app_functions.add_device("Square 1", gui_win)
    app_functions.add_device("Edison", gui_win)
    app_functions.add_device("IBN Boys Hostel", gui_win)
    app_functions.add_complaints(gui_win)
    app_functions.add_complaints(gui_win)
    timer.stop()

main_Widget.show()
timer = QTimer()
timer.start(2000)
timer.timeout.connect(flip_screen)
sys.exit(pycalcApp.exec())