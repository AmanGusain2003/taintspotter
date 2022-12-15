from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QLabel
)

import app_functions as app_functions
from settings import Setting

class main_guiWindow(QMainWindow):
    def __init__(self, setting):
        super().__init__()
        self.setting = setting
        self.setGeometry(100, 100, 800, 650)
        self.setWindowTitle(self.setting.win_title)
        # self.setGeometry(self.setting.win_x, self.setting.win_y, self.setting.win_height, self.setting.win_breadth)
        # self.VLayout1 = QVBoxLayout()
        self.HLayout1 = QHBoxLayout()
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setStyleSheet("QWidget#centralWidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 142, 175, 255), stop:0.845771 rgba(255, 255, 255, 255))}")
        self.setCentralWidget(self.centralWidget)
        self.make_buttons()
        self.make_list()
        self.make_complaint_list()
    def make_buttons(self):
        butt_add_sys = QPushButton("Add new System", self.centralWidget)
        butt_remove_sys = QPushButton("Remove a System",self.centralWidget)
        butt_sys_list = QPushButton("System List", self.centralWidget)
        butt_setting = QPushButton("Setting", self.centralWidget)
        butt_add_sys.setGeometry(100, 30, 150, 25)
        butt_remove_sys.setGeometry(100, 60, 150, 25)
        butt_sys_list.setGeometry(100, 90, 150, 25)
        butt_setting.setGeometry(10, 30, 46, 20)
        # Layout1.addWidget(butt_add_sys)
        # Layout1.addWidget(butt_remove_sys)
        # Layout1.addWidget(butt_sys_list)
    
    def make_list(self):
        label = QLabel("Deives", self.centralWidget)
        label.setGeometry(100, 180, 70, 50)
        listWidget = QListWidget(self.centralWidget)
        listWidget.setGeometry(100, 200, 100, 100)
        QListWidgetItem("System A", listWidget)
        QListWidgetItem("Square 1", listWidget)
        QListWidgetItem("IBN", listWidget)
    
    def make_complaint_list(self):
        label = QLabel("Deives", self.centralWidget)
        label.setGeometry(220, 280, 70, 50)
        listWidget = QListWidget(self.centralWidget)
        listWidget.setGeometry(220, 280, 200, 200)
        QListWidgetItem("System A", listWidget)
        QListWidgetItem("Square 1", listWidget)
        QListWidgetItem("IBN", listWidget)