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


class DataVis(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(DataVis, self).__init__(*args, **kwargs)
        self.setWindowTitle("Applications")
        # self.resize(400,400)
        self.connectDatabase()
        self.createModels()
        
        self.createTables()
        # self.companyTab()
        self.finalLayout()
        self.args = args
        self.setCentralWidget(self.finWindow)
        # self.styling()
        
    def ifMain(self):
        self.createActions()
        self.createStatusBar()
        self.createMenuBar()
        
    def styling(self):
        style = """ 
        QMainWindow {background-color: LightGray}
        QTab {background-color: LightGray}
        """
        self.setStyleSheet(style)
        
    def finalLayout(self):
        self.createTabs()
        self.initTabs()
        self.update_button_layout()
        
        self.finWindow = QFrame()
        self.finLayout = QVBoxLayout()
        
        self.finLayout.addWidget(self.tabOrg)
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
        
        self.update_comp_button.pressed.connect(self.on_update_comp_button)
        self.update_status_button.pressed.connect(lambda: print("Update Status Placeholder"))
        self.update_all_button.pressed.connect(lambda: print("Update All Placeholder"))

        
        self.buttonLayout.addWidget(self.update_comp_button)
        self.buttonLayout.addWidget(self.update_status_button)
        self.buttonLayout.addWidget(self.update_all_button)
        
        
    def createTabs(self):
        
        self.byCompanyWidget = QWidget()
        self.byRoleWidget = QWidget()
        self.byStateWidget = QWidget()
        self.byStatusWidget = QWidget()
        self.byIndustryWidget = QWidget()
        
        
        self.tabOrg = QTabWidget(self)
        # self.tabOrg.setTabPosition(QTabWidget.TabPosition.West)
        self.tabOrg.addTab(self.byCompanyWidget,"Company")
        self.tabOrg.addTab(self.byRoleWidget,"Role")
        self.tabOrg.addTab(self.byStateWidget,"State")
        self.tabOrg.addTab(self.byStatusWidget,"Status")
        self.tabOrg.addTab(self.byIndustryWidget,"Industry")
        
    def initTabs(self):
        self.companyTab()
        self.roleTab()
        self.stateTab()
        self.statusTab()
        self.industryTab()
        
        self.tabOrg.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabOrg.currentChanged.connect(self.onChange)
        self.tabOrg.setAutoFillBackground(True)
        palette = self.tabOrg.palette()
        palette.setColor(self.tabOrg.backgroundRole(), Qt.GlobalColor.lightGray)
        self.tabOrg.setPalette(palette)

    def onChange(self,i):
        match i:
            case 0:
                self.companyEntry.setFocus()
            case 1:
                self.roleEntry.setFocus()
            case 2:
                self.stateEntry.setFocus()
            case 3:
                self.statusEntry.setFocus()
            case 4:
                self.industryEntry.setFocus()
            case _:
                pass
                # self.statusbar.showMessage("Should not be possible check tab change code.",300)
    
    def companyTab(self):
        
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        
        vLayoutWidget = QWidget()
        hLayoutWidget = QWidget()
        
        vLayoutWidget.setLayout(vLayout)
        hLayoutWidget.setLayout(hLayout)
        # vLayout.setContentsMargins(20,20,20,20)
        # hLayout.setContentsMargins(20,10,10,20)
        
        self.getByCompanyButton = QPushButton("Get Applications")
        self.getByCompanyButton.setMinimumWidth(200)
        self.getByCompanyButton.clicked.connect(lambda: self.onByCompanyClick())
        self.getByCompanyButton.setDefault(True)

        # headLabel = QLabel("Company: ")
        # headLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # headLabel.setFont(QFont('Times',14))
        
        self.companyLabel = QLabel("Company Name")
        self.companyLabel.setMinimumWidth(100)
        self.companyEntry = QLineEdit()
        self.companyEntry.returnPressed.connect(self.onByCompanyClick)
        self.companyEntry.setPlaceholderText("Enter Company Name")
        self.companyEntry.setMinimumWidth(200)
        
        hLayout.addWidget(self.companyLabel)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.companyEntry)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.getByCompanyButton)
        
        # vLayout.addWidget(headLabel)
        vLayout.addWidget(self.byCompanyTable)
        vLayout.addWidget(hLayoutWidget)
        
        
        self.byCompanyWidget.setLayout(vLayout)
        self.companyEntry.setFocus()
        # self.byCompanyWidget.setFocus()
    
    def roleTab(self):    
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        
        vLayoutWidget = QWidget()
        hLayoutWidget = QWidget()
        
        vLayoutWidget.setLayout(vLayout)
        hLayoutWidget.setLayout(hLayout)
        # vLayout.setContentsMargins(20,20,20,20)
        # hLayout.setContentsMargins(20,10,10,20)
        
        self.getByRoleButton = QPushButton("Get Applications")
        self.getByRoleButton.setMinimumWidth(200)
        self.getByRoleButton.clicked.connect(lambda: self.onByRoleClick())
        self.getByRoleButton.setDefault(True)

        # headLabel = QLabel("Company: ")
        # headLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # headLabel.setFont(QFont('Times',14))
        
        self.roleLabel = QLabel("Role")       
        self.roleLabel.setMinimumWidth(100)
        self.roleEntry = QLineEdit()
        self.roleEntry.returnPressed.connect(self.onByRoleClick)
        self.roleEntry.setPlaceholderText("Enter Role")
        self.roleEntry.setMinimumWidth(200)
        
        hLayout.addWidget(self.roleLabel)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.roleEntry)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.getByRoleButton)
        
        # vLayout.addWidget(headLabel)
        vLayout.addWidget(self.byRoleTable)
        vLayout.addWidget(hLayoutWidget)
        
        self.byRoleWidget.setLayout(vLayout)
        # self.roleEntry.setFocus()
        # self.byCompanyWidget.setFocus()
    
    def stateTab(self):
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        
        vLayoutWidget = QWidget()
        hLayoutWidget = QWidget()
        
        vLayoutWidget.setLayout(vLayout)
        hLayoutWidget.setLayout(hLayout)
        # vLayout.setContentsMargins(20,20,20,20)
        # hLayout.setContentsMargins(20,10,10,20)
        
        self.getByStateButton = QPushButton("Get Applications")
        self.getByStateButton.setMinimumWidth(200)
        self.getByStateButton.clicked.connect(lambda: self.onByStateClick())
        self.getByStateButton.setDefault(True)

        # headLabel = QLabel("Company: ")
        # headLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # headLabel.setFont(QFont('Times',14))
        
        self.stateLabel = QLabel("State")
        self.stateLabel.setMinimumWidth(100)
        self.stateEntry = QLineEdit()
        self.stateEntry.returnPressed.connect(self.onByStateClick)
        self.stateEntry.setPlaceholderText("Enter State")
        self.stateEntry.setMinimumWidth(200)
        
        hLayout.addWidget(self.stateLabel)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.stateEntry)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.getByStateButton)
        
        # vLayout.addWidget(headLabel)
        vLayout.addWidget(self.byStateTable)
        vLayout.addWidget(hLayoutWidget)
        
        self.byStateWidget.setLayout(vLayout)
        # self.stateEntry.setFocus()
        # self.byCompanyWidget.setFocus()
    
    def statusTab(self):
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        
        vLayoutWidget = QWidget()
        hLayoutWidget = QWidget()
        
        vLayoutWidget.setLayout(vLayout)
        hLayoutWidget.setLayout(hLayout)
        # vLayout.setContentsMargins(20,20,20,20)
        # hLayout.setContentsMargins(20,10,10,20)
        
        self.getByStatusButton = QPushButton("Get Applications")
        self.getByStatusButton.setMinimumWidth(200)
        self.getByStatusButton.clicked.connect(lambda: self.onByStatusClick())
        self.getByStatusButton.setDefault(True)

        # headLabel = QLabel("Company: ")
        # headLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # headLabel.setFont(QFont('Times',14))
        
        self.statusLabel = QLabel("Status")
        self.statusLabel.setMinimumWidth(100)
        self.statusEntry = QLineEdit()
        self.statusEntry.returnPressed.connect(self.onByStatusClick)
        self.statusEntry.setPlaceholderText("Enter Status")
        self.statusEntry.setMinimumWidth(200)
        
        hLayout.addWidget(self.statusLabel)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.statusEntry)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.getByStatusButton)
        
        # vLayout.addWidget(headLabel)
        vLayout.addWidget(self.byStatusTable)
        vLayout.addWidget(hLayoutWidget)
        
        self.byStatusWidget.setLayout(vLayout)
        # self.statusEntry.setFocus()
        # self.byCompanyWidget.setFocus()
    
    def industryTab(self):
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        
        vLayoutWidget = QWidget()
        hLayoutWidget = QWidget()
        
        vLayoutWidget.setLayout(vLayout)
        hLayoutWidget.setLayout(hLayout)
        # vLayout.setContentsMargins(20,20,20,20)
        # hLayout.setContentsMargins(20,10,10,20)
        
        self.getByIndustryButton = QPushButton("Get Applications")
        self.getByIndustryButton.setMinimumWidth(200)
        self.getByIndustryButton.clicked.connect(lambda: self.onByIndustryClick())
        self.getByIndustryButton.setDefault(True)

        # headLabel = QLabel("Company: ")
        # headLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # headLabel.setFont(QFont('Times',14))
        
        self.industryLabel = QLabel("Industry")
        self.industryLabel.setMinimumWidth(100)
        self.industryEntry = QLineEdit()
        self.industryEntry.returnPressed.connect(self.onByIndustryClick)
        self.industryEntry.setPlaceholderText("Enter Industry")
        self.industryEntry.setMinimumWidth(200)
        
        hLayout.addWidget(self.industryLabel)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.industryEntry)
        hLayout.addSpacerItem(QSpacerItem(50,20))
        hLayout.addWidget(self.getByIndustryButton)
        
        # vLayout.addWidget(headLabel)
        vLayout.addWidget(self.byIndustryTable)
        vLayout.addWidget(hLayoutWidget)
        
        self.byIndustryWidget.setLayout(vLayout)
        # self.industryEntry.setFocus()
        # self.byCompanyWidget.setFocus()
    
    def onByCompanyClick(self):
        # self.statusbar.showMessage("Getting Applications",300)
        
        companyName = self.companyEntry.text()
        
        query = QSqlQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid AND Name LIKE '%{}%'".format(companyName))
        query.exec()
        if len(companyName)==0:
            self.companyTable.setQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
        else: 
            self.companyTable.setQuery(query)
        self.companyTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
        self.byCompanyTable.resizeColumnsToContents()
        self.companyEntry.clear()    
    
    def onByRoleClick(self):
        # self.statusbar.showMessage("Getting Applications",300)
        
        # companyName = self.companyEntry.text()
        # self.headLabel = QLabel("Company: {}".format(companyName))
        roleName = self.roleEntry.text()

        query = QSqlQuery("""SELECT Name,Title, Industry,Poc, Application_status, Application_result FROM Roles, 
                          Companies WHERE Roles.company_ID = Companies.rowid AND Title LIKE '%{}%'""".format(roleName))
        query.exec()
        if len(roleName)==0:
            self.roleTable.setQuery("SELECT Name, Title, Industry,Poc,  Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
        else: 
            self.roleTable.setQuery(query)
        self.roleTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
        self.byRoleTable.resizeColumnsToContents()
        self.roleEntry.clear()    
    
    def onByStateClick(self):
        # self.statusbar.showMessage("Getting Applications",300)
        
        stateName = self.stateEntry.text()

        query = QSqlQuery("""SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, 
                          Companies WHERE Roles.company_ID = Companies.rowid AND Job_state LIKE '%{}%'""".format(stateName))
        query.exec()
        if len(stateName)==0:
            self.stateTable.setQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
        else: 
            self.stateTable.setQuery(query)
        self.stateTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
        self.byStateTable.resizeColumnsToContents()
        self.stateEntry.clear()    
    
    def onByStatusClick(self):
        # self.statusbar.showMessage("Getting Applications",300)
        
        statusName = self.statusEntry.text()
        self.headLabel = QLabel("Company: {}".format(statusName))

        query = QSqlQuery("""SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles,
                          Companies WHERE Roles.company_ID = Companies.rowid AND Application_status LIKE '%{}%'""".format(statusName))
        query.exec()
        if len(statusName)==0:
            self.statusTable.setQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
        else: 
            self.statusTable.setQuery(query)
        self.statusTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
        self.byStatusTable.resizeColumnsToContents()
        self.statusEntry.clear()    
    
    def onByIndustryClick(self):
        # self.statusbar.showMessage("Getting Applications",300)
        
        industryName = self.industryEntry.text()
        self.headLabel = QLabel("Company: {}".format(industryName))

        query = QSqlQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid AND Industry LIKE '%{}%'".format(industryName))
        query.exec()
        if len(industryName)==0:
            self.industryTable.setQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
        else: 
            self.industryTable.setQuery(query)
        self.industryTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
        self.byIndustryTable.resizeColumnsToContents()
        self.industryEntry.clear()    
    
    def on_update_comp_button(self):
        selection = self.byCompanyTable.selectionModel()
        index = self.byCompanyTable.currentIndex()
        row = index.row()
        Company = self.byCompanyTable.model().data(self.byCompanyTable.model().index(row,0))
        print(Company)
        self.final_instance.on_update_comp_button(Company)
        # selRow = selection.selectedRows()
        # if selection.hasSelection():
        #     self.args.on_company_click()
        # updateC = UpdateComp()
        
        # finalApp = FinalApp()
        # finalApp.on_update_comp_button()
        
        

    def createTables(self):
        self.byCompanyTable = QTableView(self)
        self.byStateTable = QTableView(self)
        self.byRoleTable = QTableView(self)
        self.byStatusTable = QTableView(self)
        self.byIndustryTable = QTableView(self)
        
        
        self.byCompanyTable.setModel(self.companyTable)
        self.byCompanyTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.byCompanyTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.byCompanyTable.resizeColumnsToContents()
        self.byCompanyTable.setAlternatingRowColors(True)
        
        self.byRoleTable.setModel(self.roleTable)
        self.byRoleTable.resizeColumnsToContents()
        self.byRoleTable.setAlternatingRowColors(True)
        
        self.byStateTable.setModel(self.stateTable)
        self.byStateTable.resizeColumnsToContents()
        self.byStateTable.setAlternatingRowColors(True)
        
        self.byStatusTable.setModel(self.statusTable)
        self.byStatusTable.resizeColumnsToContents()
        self.byStatusTable.setAlternatingRowColors(True)
        
        self.byIndustryTable.setModel(self.industryTable)
        self.byIndustryTable.resizeColumnsToContents()
        self.byIndustryTable.setAlternatingRowColors(True)
        
    def createModels(self):

        self.companyTable = QSqlTableModel()
        self.companyTable.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.companyTable.select()
        
        self.roleTable = QSqlTableModel()
        self.roleTable.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.roleTable.select()
    
        self.stateTable = QSqlTableModel()
        self.stateTable.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.stateTable.select()
            
        self.statusTable = QSqlTableModel()
        self.statusTable.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.statusTable.select()
        
        self.industryTable = QSqlTableModel()
        self.industryTable.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.industryTable.select()
    
    def createMenuBar(self):
        
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newEntryAction)
        fileMenu.addSeparator
        fileMenu.addAction(self.discardAction)
        fileMenu.addAction(self.exitAction)
        
        dataMenu = menuBar.addMenu("&Data")
        dataMenu.addActions([self.byCompanyAction,self.byRoleAction,
                             self.byStateAction,self.byStatusAction])
        
    def createActions(self):
        self.newEntryAction = QAction("&New Entry")
        self.discardAction = QAction("D&iscard")
        self.exitAction = QAction("&Exit")
        
        self.byCompanyAction = QAction("By &Company")        
        self.byRoleAction = QAction("By &Role")
        self.byStateAction = QAction("By &State")
        self.byStatusAction = QAction("By S&tatus")
        
        # self.discardAction.triggered.connect(lambda: self.clear_form())
        self.discardAction.triggered.connect(lambda: self.statusbar.showMessage("Discarding entry",300))

        self.exitAction.triggered.connect(lambda: self.close())
        
    def createStatusBar(self):
        
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

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
    Window = DataVis()
    Window.ifMain()
    Window.show()
    Window.conn.close
    app.exec()