
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
import app_functions as app_functions
from settings import Setting

class main_guiWindow(QMainWindow):
    def __init__(self, setting):
        super().__init__()
        self.setting = setting
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle(self.setting.win_title)
        # self.setGeometry(self.setting.win_x, self.setting.win_y, self.setting.win_height, self.setting.win_breadth)
        # self.VLayout1 = QVBoxLayout()
        self.HLayout1 = QHBoxLayout()
        centralWidget = QWidget(self)
        app_functions.make_buttons(self.HLayout1, self.setting, centralWidget)
        centralWidget.setLayout(self.HLayout1)
