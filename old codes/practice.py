import sqlite3
import sys
from datetime import date
from typing import Any
from PyQt6.QtCore import  Qt

# from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame,
#                              QComboBox, QGridLayout, QLabel, QGroupBox, QMainWindow,QMenuBar,QMenu,QStatusBar)
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon,QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        label = QLabel("Hello!")
        # label.setAlignment(Qt.)
        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
    
    def onMyToolBarButtonClick(self, s):
        print("click", s)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= MainWindow()
    window.show()
    app.exec()