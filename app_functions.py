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
    
    butt_add_sys = QPushButton("Add new System", centralWidget)
    butt_remove_sys = QPushButton("Remove a System",centralWidget)
    butt_sys_list = QPushButton("System List", centralWidget)
    butt_setting = QPushButton("Setting", centralWidget)
    butt_add_sys.setGeometry(100, 30, 150, 25)
    butt_remove_sys.setGeometry(100, 60, 150, 25)
    butt_sys_list.setGeometry(100, 90, 150, 25)
    butt_setting.setGeometry(10, 30, 46, 20)
    # Layout1.addWidget(butt_add_sys)
    # Layout1.addWidget(butt_remove_sys)
    # Layout1.addWidget(butt_sys_list)