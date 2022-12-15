import sys
#import time
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel)

class Window2(QMainWindow):                          
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window 22222")

class Window3(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window 333333")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "First Window"
        self.top, self.left, self.width, self.height = 100, 100, 680, 500
        
        self.flag = ...

        self.pushButton = QPushButton("Start", self)
        self.pushButton.move(275, 200)
        self.pushButton.setToolTip("<h3>Start the Session</h3>")
        self.pushButton.clicked.connect(lambda: self.start_slide(True)) #(self.window2)      
        
        self.pushButton1 = QPushButton("Start", self)
        self.pushButton1.move(20, 20)
        self.pushButton1.setToolTip("<h3>Start the Session</h3>")
        self.pushButton1.clicked.connect(lambda: self.start_slide(False))   
        
# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.main_window()
        
        self.w2 = Window2()
        self.w3 = Window3()
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.viewWindows)

    def start_slide(self, flag):
        self.timer.stop()
        self.w3.hide()
        self.w2.hide()
        if flag: self.w2.show()
        else: self.w3.show()
        self.flag = not flag
        self.timer.start(5000)

    def viewWindows(self):
        if self.flag:
            self.w2.show()
            self.w3.hide()
        else:
            self.w3.show()
            self.w2.hide()
        self.flag = not self.flag
        
    def closeEvent(self, event):
        self.w2.close()
        self.w3.close()
        self.close()
        
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    def main_window(self):
        self.label = QLabel("Manager", self)
        self.label.move(285, 175)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())