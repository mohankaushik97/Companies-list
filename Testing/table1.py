import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase
from PyQt6.QtCore import Qt

class Table(QWidget):
    
    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)
        self.resize(400,300)
        self.setWindowTitle("Table")
        self.vLayout = QVBoxLayout()
        self.hLayout = QHBoxLayout()
        
        self.vLayoutWidget = QWidget()
        self.hLayoutWidget = QWidget()
        
        # self.test = QLabel("Testing")
        # layout = QVBoxLayout()
        # layout.addWidget(self.test)
        # self.setLayout(layout)
        
        self.vLayoutWidget.setLayout(self.vLayout)
        self.hLayoutWidget.setLayout(self.hLayout)
        self.vLayout.setContentsMargins(20,20,20,20)
        self.hLayout.setContentsMargins(20,10,10,20)
        
        self.table = QTableView()
        
        self.button = QPushButton("Get Applications")
        self.button.setMinimumWidth(200)
        self.companylabel = QLabel("Company Name")
        self.companyEntry = QLineEdit()
        self.companyEntry.setPlaceholderText("Enter Company Name")
        self.companyEntry.setMinimumWidth(200)
        
        self.hLayout.addWidget(self.companylabel)
        self.hLayout.addSpacerItem(QSpacerItem(50,20))
        self.hLayout.addWidget(self.companyEntry)
        self.hLayout.addSpacerItem(QSpacerItem(50,20))
        self.hLayout.addWidget(self.button)
        
        self.vLayout.addWidget(self.table)
        self.vLayout.addWidget(self.hLayoutWidget)
        
        self.setLayout(self.vLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Table()
    win.show()
    app.exec()