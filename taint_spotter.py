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
import devices as devices
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
import pyrebase

setting = Setting()
devicess = devices.Devices()

#setting up the database
firebase = pyrebase.initialize_app(setting.config)  
db = firebase.database()

pycalcApp = QApplication(sys.argv)
main_Widget = QStackedWidget()

gui_win = main_guiWindow(setting)
welcome_gui = welcome_screen()
# gui_win.make_buttons()
# gui_win.show()
main_Widget.addWidget(welcome_gui)
main_Widget.addWidget(gui_win)
main_Widget.setGeometry(50, 50, 800, 600)

timer_init = QTimer()
timer_database = QTimer()

def begin_timer_init():
    timer_init.start(2000)
    timer_init.timeout.connect(flip_screen)

def flip_screen():
    main_Widget.setCurrentIndex(1)
    devicess.add_device("IBN Boys", "phval", "tds")
    devicess.add_device("Square One", "plav2", "tds2")

    for item in devicess.devices_list:
        app_functions.add_to_device_list(item, gui_win)

    app_functions.add_complaints(gui_win)
    app_functions.add_complaints(gui_win)
    timer_init.stop()

def update_values():
    for device in devicess.devices_list:
        device.phval = db.child(device.phval_address).get().val()
    currentRow = gui_win.device_list.currentIndex()
    currentDevice =  devicess.devices_list[currentRow - 1]
    textt = "TDS: " + str(currentDevice.tds)
    gui_win.reading_data_label.setText(textt)

def begin_database_timer():
    timer_database.start(1500)
    timer_database.timeout.connect(update_values)

begin_timer_init()
begin_database_timer()
main_Widget.show()

sys.exit(pycalcApp.exec())