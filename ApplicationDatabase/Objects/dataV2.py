from ast import Tuple
from operator import index
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QFont
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt
# from DataEntry.updateCompany import UpdateComp

sys.path.insert(0, 'D:\Companies list\ApplicationDatabase')
from Database.database import Database
# from FinalApp.finalApp import FinalApp


class DataV2(QMainWindow):
    
    def __init__(self,entry_type="normal"):
        super(DataV2, self).__init__()
        self.setWindowTitle("Applications")
        self.entry_type = entry_type
        self.initSearchEdit()
        self.createModels()
        self.createTables()
        self.finalLayout()
        self.dispDataTable()

        self.setCentralWidget(self.finWindow)
        
        
    def styling(self):
        pass
        # style = """ 
        # QMainWindow {background-color: LightGray}
        # QTab {background-color: LightGray}
        # """
        # self.setStyleSheet(style)
        
    def finalLayout(self):
        self.update_button_layout()
        
        self.finWindow = QFrame()
        self.finLayout = QVBoxLayout()
        self.byCompanyWidget = QWidget()
        
        self.finLayout.addWidget(self.byCompanyWidget)
        self.finLayout.addWidget(self.buttonGroup)
        
        self.finWindow.setLayout(self.finLayout)
        
    def update_button_layout(self):
        self.buttonGroup = QGroupBox("Update Information")
        self.buttonLayout = QHBoxLayout()
        
        self.buttonGroup.setLayout(self.buttonLayout)
        self.buttonGroup.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.update_comp_button = QPushButton("Company")
        self.update_status_button = QPushButton("Status")
        self.update_all_button = QPushButton("All Details")
        
        # self.update_comp_button.pressed.connect(self.on_update_comp_button)
        # self.update_status_button.pressed.connect(lambda: print("Update Status Placeholder"))
        # self.update_all_button.pressed.connect(lambda: print("Update All Placeholder"))
        
        self.buttonLayout.addWidget(self.update_comp_button)
        self.buttonLayout.addWidget(self.update_status_button)
        self.buttonLayout.addWidget(self.update_all_button)
        
    def create_data_table(self):
        self.byCompanyWidget = QWidget()
        
        self.createModels()
        self.createTables()
        self.dispDataTable()
        
        return self.finWindow
    
    
    def initSearchEdit(self):
        
        self.state=["AL ","AK ","AZ ","AR ","CA ","CO ","CT ","DE ","FL ",
                                       "GA ","HI ","ID ","IL ","IN ","IA ","KS ","KY ","LA ",
                                       "ME ","MD ","MA ","MI ","MN ","MS ","MO ","MT ","NE ",
                                       "NV ","NH ","NJ ","NM ","NY ","NC ","ND ","OH ","OK ",
                                       "OR ","PA ","RI ","SC ","SD ","TN ","TX ","UT ","VT ",
                                       "VA ","WA ","WV ","WI ","WY ","DC","AS ","GU ","MP ","PR"]
        self.comp_size = ['1 to 20','20 to 99','100-999','1,000-9,999','10,000-99,999','100,000+']
        self.comp_revenue = ['<$5M','$5M-$99M','$100M-$999M','$1B+']
        self.job_level = ["Internship", "New Grad", 'Engineer I','Engineer II','Engineer III','Start-up']
        self.app_status = ['Applied','In-Reivew','Interview-1','Interview-2','Interview-3']
        self.app_result = ['In-Process','Accepted','Rejected']

        
        if self.entry_type == "normal":
            self.searchDataEntry = QLineEdit()
        elif self.entry_type == "state":
            self.searchDataEntry = QComboBox()
            self.searchDataEntry.addItems(self.state)
        elif self.entry_type == "status":
            self.searchDataEntry = QComboBox()
            self.searchDataEntry.addItems(self.app_status)
    
    def dispDataTable(self):
        
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        
        vLayoutWidget = QWidget()
        hLayoutWidget = QWidget()
        
        vLayoutWidget.setLayout(vLayout)
        hLayoutWidget.setLayout(hLayout)
        
        self.getDataButton = QPushButton("Get Applications")
        self.getDataButton.setMinimumWidth(200)
        # self.getDataButton.clicked.connect(lambda: self.onByCompanyClick())
        # self.getDataButton.clicked.connect(lambda: print("Button Press"))
        self.getDataButton.setDefault(True)

        self.searchDataLabel = QLabel("Placeholder name")
        self.searchDataLabel.setMinimumWidth(200)
        
        # self.searchDataEntry.returnPressed.connect(lambda: print("Button Press"))
        # self.searchDataEntry.setPlaceholderText("Enter Placeholder Name")
        self.searchDataEntry.setMinimumWidth(200)
        
        hLayout.addWidget(self.searchDataLabel)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.searchDataEntry)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.getDataButton)
        
        # vLayout.addWidget(headLabel)
        vLayout.addWidget(self.tableView)
        vLayout.addWidget(hLayoutWidget)
        
        
        self.byCompanyWidget.setLayout(vLayout)
        self.searchDataEntry.setFocus()
    
    def createTables(self):
        self.tableView = QTableView(self)
        
        self.tableView.setModel(self.dataTable)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.resizeColumnsToContents()
        self.tableView.setAlternatingRowColors(True)
        
    def createModels(self):
        self.dataTable = QSqlTableModel()
        self.dataTable.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.dataTable.select()
        
    def connectDatabase(self):
        self.conn = QSqlDatabase.addDatabase('QSQLITE')
        self.conn.setDatabaseName('.\ApplicationDatabase\Database\database.db')
        # self.conn.setDatabaseName('database.db')
        if not self.conn.open():
            QMessageBox.critical(
                None,
                "App Name - Error",
                "Database Error: %s" % self.conn.lastError().databaseText(),
            )
    
    def closeDatabase(self):
        self.conn.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = DataV2()
    Window.show()
    # Window.conn.close
    app.exec()