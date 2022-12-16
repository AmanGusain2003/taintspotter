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
import pyrebase

class Device():
    def __init__(self, name, phval_address, tds_address) -> None:
        self.name = name
        self.phval = 0.0
        self.tds = 0.0
        self.phval_address = phval_address
        self.tds_address = tds_address

class Devices():
    def __init__(self) -> None:
        self.devices_list = []

    def add_device(self, phval_address,tds_address, name):
        device = Device(name, phval_address, tds_address)
        self.devices_list.append(device)

