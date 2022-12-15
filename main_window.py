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
        self.init_elements()
        self.set_geometry()
        self.set_style_sheet()
        self.connect_buttons()

    def init_elements(self):
        self.device_list = QListWidget(self.centralWidget)
        self.complaints_list = QListWidget(self.centralWidget)
        self.device_data_list = QListWidget(self.centralWidget)
        self.complaints_data_list = QListWidget(self.centralWidget)
        self.emptyone_list = QListWidget(self.centralWidget)
        self.emptytwo_list = QListWidget(self.centralWidget)
        #****************************
        self.device_label = QLabel("Devices", self.centralWidget)
        self.complaint_label = QLabel("Complaints",  self.centralWidget)
        self.last_review_label = QLabel("Last Reviewed", self.centralWidget)
        self.last_review_data_label = QLabel("12, Aug", self.centralWidget)
        self.reading_data_label = QLabel("TDS: 80", self.centralWidget)
        self.reading_label = QLabel("Reading", self.centralWidget)
        self.location_label = QLabel("Location", self.centralWidget)
        self.time_issued_label = QLabel("Time Issued", self.centralWidget)
        self.status_label = QLabel("Status:", self.centralWidget)
        #*******************
        self.more_button = QPushButton("More...", self.centralWidget)
        self.view_history_button = QPushButton("View History", self.centralWidget)
        self.resolved_button = QPushButton("Resolved", self.centralWidget)
        self.ignore_button = QPushButton("Ignore", self.centralWidget)  

    def set_geometry(self):
        self.device_label.setGeometry(120,60,67,17)
        self.complaint_label.setGeometry(120,300,101,31)
        self.last_review_label.setGeometry(400,90,131,20)
        self.reading_label.setGeometry(400,150,131,20)
        self.last_review_data_label.setGeometry(410, 120, 191, 21)
        self.reading_data_label.setGeometry(410, 180, 191, 21)
        self.location_label.setGeometry(400,340,131,20)
        self.time_issued_label.setGeometry(400,370,251,20)
        self.status_label.setGeometry(400,400,131,20)
        self.more_button.setGeometry(520,220,81,20)
        self.view_history_button.setGeometry(120,420,121,25)
        self.ignore_button.setGeometry(520,440,111,25)
        self.device_list.setGeometry(121,80,231,161)
        self.complaints_list.setGeometry(120,331,231,81)
        self.device_data_list.setGeometry(390,80,261,131)
        self.complaints_data_list.setGeometry(390,330,261,101)
        self.resolved_button.setGeometry(400,440,111,25)
        self.emptyone_list.setGeometry(350,80,41,21)
        self.emptytwo_list.setGeometry(350,330,41,21)

    def set_style_sheet(self):
        self.device_label.setStyleSheet("background-color: rgba(0,0,0,0);\nfont: 14pt, italics ;")
        self.complaint_label.setStyleSheet("background-color: rgba(0,0,0,0);\nfont: 14pt, italics ;")
        # self.last_review_label.setStyleSheet()
        # self.reading_label.setStyleSheet()
        self.last_review_data_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reading_data_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.location_label.setStyleSheet()
        # self.time_issued_label.setStyleSheet()
        # self.status_label.setStyleSheet()
        self.more_button.setStyleSheet("background-color:rgb(153, 193, 241);\nborder-radius : 10;\n")
        self.view_history_button.setStyleSheet("background-color:rgb(153, 193, 241);\nborder-radius : 10;\n")
        self.ignore_button.setStyleSheet("background-color:rgb(153, 193, 241);\nborder-radius : 10;\n")
        self.resolved_button.setStyleSheet("background-color:rgb(153, 193, 241);\nborder-radius : 10;\n")
        self.device_list.setStyleSheet("font: 11pt;\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(127, 179, 249, 255), stop:1 rgba(255, 255, 255, 255))")
        self.complaints_list.setStyleSheet("font: 11pt;\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(127, 179, 249, 255), stop:1 rgba(255, 255, 255, 255))")
        self.device_data_list.setStyleSheet("font: 11pt;\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(127, 179, 249, 255), stop:1 rgba(255, 255, 255, 255))")
        self.complaints_data_list.setStyleSheet("font: 11pt;\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(127, 179, 249, 255), stop:1 rgba(255, 255, 255, 255))")
        self.emptyone_list.setStyleSheet("font: 11pt ;\nbackground-color: rgb(207, 247, 255)")
        self.emptytwo_list.setStyleSheet("font: 25 11pt;\nbackground-color:rgb(207, 247, 255)")

    def connect_buttons(self):
        self.resolved_button.clicked.connect(self.remove_item)

    def remove_item(self):
        self.complaints_list.takeItem(self.complaints_list.currentRow())
