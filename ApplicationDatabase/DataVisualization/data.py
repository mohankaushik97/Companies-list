import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QFont,QShortcut,QKeySequence
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt
from PyQt6 import QtCore


class ShowData():
    
    def __init__(self, *args, **kwargs):
        super(ShowData, self).__init__(*args, **kwargs)
        self.connectDatabase()

    
    def onByCompanyClick(self,comp_name: str):
        # self.statusbar.showMessage("Getting Applications",300)
        
        companyName = comp_name
        
        query = QSqlQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid AND Name LIKE '%{}%'".format(companyName))
        query.exec()
        if len(companyName)==0:
            self.companyTable.setQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
        else: 
            self.companyTable.setQuery(query)
        return self.companyTable
        
    # def onByRoleClick(self):
    #     # self.statusbar.showMessage("Getting Applications",300)
        
    #     # companyName = self.companyEntry.text()
    #     # self.headLabel = QLabel("Company: {}".format(companyName))
    #     roleName = self.roleEntry.text()

    #     query = QSqlQuery("""SELECT Name,Title, Industry,Poc, Application_status, Application_result FROM Roles, 
    #                       Companies WHERE Roles.company_ID = Companies.rowid AND Title LIKE '%{}%'""".format(roleName))
    #     query.exec()
    #     if len(roleName)==0:
    #         self.roleTable.setQuery("SELECT Name, Title, Industry,Poc,  Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
    #     else: 
    #         self.roleTable.setQuery(query)
    #     self.roleTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
    #     self.byRoleTable.resizeColumnsToContents()
    #     self.roleEntry.clear()    
    
    # def onByStateClick(self):
    #     # self.statusbar.showMessage("Getting Applications",300)
        
    #     stateName = self.stateEntry.text()

    #     query = QSqlQuery("""SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, 
    #                       Companies WHERE Roles.company_ID = Companies.rowid AND Job_state LIKE '%{}%'""".format(stateName))
    #     query.exec()
    #     if len(stateName)==0:
    #         self.stateTable.setQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
    #     else: 
    #         self.stateTable.setQuery(query)
    #     self.stateTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
    #     self.byStateTable.resizeColumnsToContents()
    #     self.stateEntry.clear()    
    
    # def onByStatusClick(self):
    #     # self.statusbar.showMessage("Getting Applications",300)
        
    #     statusName = self.statusEntry.text()
    #     self.headLabel = QLabel("Company: {}".format(statusName))

    #     query = QSqlQuery("""SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles,
    #                       Companies WHERE Roles.company_ID = Companies.rowid AND Application_status LIKE '%{}%'""".format(statusName))
    #     query.exec()
    #     if len(statusName)==0:
    #         self.statusTable.setQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
    #     else: 
    #         self.statusTable.setQuery(query)
    #     self.statusTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
    #     self.byStatusTable.resizeColumnsToContents()
    #     self.statusEntry.clear()    
    
    # def onByIndustryClick(self):
    #     # self.statusbar.showMessage("Getting Applications",300)
        
    #     industryName = self.industryEntry.text()
    #     self.headLabel = QLabel("Company: {}".format(industryName))

    #     query = QSqlQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid AND Industry LIKE '%{}%'".format(industryName))
    #     query.exec()
    #     if len(industryName)==0:
    #         self.industryTable.setQuery("SELECT Name, Industry,Poc, Title, Application_status, Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid")
    #     else: 
    #         self.industryTable.setQuery(query)
    #     self.industryTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
    #     self.byIndustryTable.resizeColumnsToContents()
    #     self.industryEntry.clear()    
    
    def createCompanyModel(self):
        self.companyTable = QSqlTableModel()
        self.companyTable.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.companyTable.select()
        return self.companyTable
        
    def createModels(self):

        
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
    
    