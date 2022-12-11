from PyQt5 import QtCore
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

def make_buttons(Layout1, setting, centralWidget):
    
    butt_add_sys = QPushButton("1")
    butt_remove_sys = QPushButton("2")
    butt_sys_list = QPushButton("3")
    # butt_add_sys.resize(100, 100)
    # butt_remove_sys.resize(100, 100)
    # butt_sys_list.resize(100, 100)
    Layout1.addWidget(butt_add_sys)
    Layout1.addWidget(butt_remove_sys)
    Layout1.addWidget(butt_sys_list)

