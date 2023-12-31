from ast import Tuple
from dataclasses import InitVar
from operator import index
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QFont
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt
# from DataEntry.updateCompany import UpdateComp

# sys.path.insert(0, 'D:\Companies list\ApplicationDatabase')

class DataView():
    def __init__(self):
        pass
    
    def initVars(self,entry_type="normal"):
        
        self.entry_type = entry_type

        
        self.state=["AL ","AK ","AZ ","AR ","CA ","CO ","CT ","DE ","FL ",
                                       "GA ","HI ","ID ","IL ","IN ","IA ","KS ","KY ","LA ",
                                       "ME ","MD ","MA ","MI ","MN ","MS ","MO ","MT ","NE ",
                                       "NV ","NH ","NJ ","NM ","NY ","NC ","ND ","OH ","OK ",
                                       "OR ","PA ","RI ","SC ","SD ","TN ","TX ","UT ","VT ",
                                       "VA ","WA ","WV ","WI ","WY ","DC","AS ","GU ","MP ","PR"]
        self.comp_size = ['1 to 20','20 to 99','100-999','1,000-9,999','10,000-99,999','100,000+']
        self.comp_revenue = ['<$5M','$5M-$99M','$100M-$999M','$1B+']
        self.job_level = ["Internship", "New Grad", 'Engineer I','Engineer II','Engineer III','Start-up']
        self.app_status = ['Applied','In-Review','Interview-1','Interview-2','Interview-3']
        self.app_result = ['In-Process','Accepted','Rejected']

        # LAYOUT
        self.finLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()
        
        self.vLayout = QVBoxLayout()
        self.hLayout = QHBoxLayout()
        
        # CONTAINERS
        self.finWindow = QFrame()
        
        # BUTTONS
        self.buttonGroup = QGroupBox("Update Information")

        self.update_comp_button = QPushButton("Company")
        self.update_status_button = QPushButton("Status")
        self.update_all_button = QPushButton("All Details")
        
        
        # WIDGETS
        self.byCompanyWidget = QWidget()
        
        self.vLayoutWidget = QWidget()
        self.hLayoutWidget = QWidget()
        
        # TABLES
        self.tableView = QTableView()
        self.dataTable = QSqlTableModel()
        

        
        # ENTRY
        
        if self.entry_type == "normal":
            self.searchDataEntry = QLineEdit()
        elif self.entry_type == "status":
            self.searchDataEntry = QComboBox()
            self.searchDataEntry.setPlaceholderText("Select Job Status")
            self.searchDataEntry.addItems(self.app_status)
        
    
    def create_table_view(self,entry_type="normal"):
        self.initVars(entry_type)
        
        self.finLayout.addWidget(self.byCompanyWidget)
        self.finLayout.addWidget(self.buttonGroup)
        
        self.finWindow.setLayout(self.finLayout)
        
        self.buttonGroup.setLayout(self.buttonLayout)
        self.buttonGroup.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.buttonLayout.addWidget(self.update_comp_button)
        self.buttonLayout.addWidget(self.update_status_button)
        self.buttonLayout.addWidget(self.update_all_button)
        
        self.vLayoutWidget.setLayout(self.vLayout)
        self.hLayoutWidget.setLayout(self.hLayout)
        
        self.getDataButton = QPushButton("Get Applications")
        self.getDataButton.setMinimumWidth(200)
        self.getDataButton.setDefault(True)

        self.searchDataLabel = QLabel("Placeholder name")
        self.searchDataLabel.setMinimumWidth(200)
        self.searchDataEntry.setMinimumWidth(200)

        self.hLayout.addWidget(self.searchDataLabel)
        self.hLayout.addSpacerItem(QSpacerItem(50,20))
        self.hLayout.addWidget(self.searchDataEntry)
        self.hLayout.addSpacerItem(QSpacerItem(50,20))
        self.hLayout.addWidget(self.getDataButton)
        
        self.vLayout.addWidget(self.tableView)
        self.vLayout.addWidget(self.hLayoutWidget)
        
        self.byCompanyWidget.setLayout(self.vLayout)
        self.searchDataEntry.setFocus()
        
        self.tableView.setModel(self.dataTable)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.resizeColumnsToContents()
        self.tableView.setAlternatingRowColors(True)
        
        self.dataTable.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.dataTable.select()
        
        return self.finWindow


    def connectDatabase(self):
        self.conn = QSqlDatabase.addDatabase('QSQLITE')
        # self.conn.setDatabaseName('.\ApplicationDatabase\Database\database.db')
        self.conn.setDatabaseName('database.db')
        if not self.conn.open():
            QMessageBox.critical(
                None,
                "App Name - Error",
                "Database Error: %s" % self.conn.lastError().databaseText(),
            )
    
    def closeDatabase(self):
        self.conn.close()
    