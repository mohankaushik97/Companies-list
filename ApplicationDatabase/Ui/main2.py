#!/usr/bin/env Python3

import sys
from datetime import date
from telnetlib import STATUS
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QFont,QShortcut,QKeySequence
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt, QEvent, QDate
from PyQt6 import QtCore

sys.path.insert(0, '/home/mohan/Desktop/Companies-list/ApplicationDatabase')
# from DataVisualization.data import ShowData
from Objects.objects import ObjImports
from Objects.dataView import DataView
from Database.database import Database



class ApplicationVer2(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(ApplicationVer2, self).__init__(*args, **kwargs)
        self.setWindowTitle("Ver2")
        # self.resize(400,400)
        
        self.styling()
        self.createStatusBar()
        self.createActions()
        self.createMenuBar()
        # self.connectDatabase()
        self.initializations()
        self.setCentralWidget(self.main_tabs)
        self.newEntry()
        self.showData()
        self.updateData()
        self.horTabs()
        self.verTabs()
        # self.setStyleSheet("background-color: #bdd6fc;")
        
        # self.set_groupboxes_background_color("#C0C0C0", self)
        
    def initializations(self):
        self.db = Database()

        # TAB Organisers
        self.main_tabs = QTabWidget()        
        self.data_tabs = QTabWidget()
        self.update_tabs = QTabWidget()

        # OBJECTS
        self.entry_obj = ObjImports()
        self.update_comp_obj = ObjImports()
        self.update_stat_obj = ObjImports()
        self.update_all_obj = ObjImports()
        self.disp_data_obj = ObjImports()
        
        self.search_comp_obj = DataView()
        self.search_role_obj = DataView()
        self.search_status_obj = DataView()
        self.search_industry_obj = DataView()
        
    def verTabs(self):
        # self.show_data_tab = self.data_tab
        
        self.main_tabs.setTabShape(QTabWidget.TabShape.Triangular)
        self.main_tabs.setTabPosition(QTabWidget.TabPosition.West)
        
        self.main_tabs.addTab(self.new_entry_tab,"N &Entry")
        self.main_tabs.addTab(self.data_tabs,"&Data")
        self.main_tabs.addTab(self.update_tabs,"&Update")

        self.main_tabs.currentChanged.connect(self.on_ver_change)
        
        shortcut = QShortcut(QKeySequence('Ctrl+Q'), self)
        shortcut2 = QShortcut(QKeySequence('Ctrl+Shift+Q'), self)
        shortcut.activated.connect(self.on_tab)
        shortcut2.activated.connect(self.on_shift_tab)

        self.main_tabs.setAutoFillBackground(True)
        palette = self.main_tabs.palette()
        palette.setColor(self.main_tabs.backgroundRole(), Qt.GlobalColor.lightGray)
        self.main_tabs.setPalette(palette)
        
        self.data_tabs.installEventFilter(self)
        self.update_tabs.installEventFilter(self)
        
        self.entry_obj.comp_name_entry.setFocus()
    
    def horTabs(self):
        self.data_tabs.setTabShape(QTabWidget.TabShape.Triangular)
        self.data_tabs.addTab(self.data_by_company_widget,"Company")
        self.data_tabs.addTab(self.data_by_role_widget,"Role")
        self.data_tabs.addTab(self.data_by_status_widget,"Status")
        self.data_tabs.addTab(self.data_by_industry_widget,"Industry")
        
        self.update_tabs.setTabShape(QTabWidget.TabShape.Triangular)
        self.update_tabs.addTab(self.update_company,"Company")
        self.update_tabs.addTab(self.update_status,"Application Status")
        self.update_tabs.addTab(self.update_all,"Role details")

        self.data_tabs.currentChanged.connect(self.on_data_change)
        # self.update_tabs.currentChanged.connect(self.on_hor_cahnge)
        
    def newEntry(self):
        self.new_entry_tab = self.entry_obj.create_new_entry_box()
        
        self.entry_obj.enter_data_button.clicked.connect(self.on_enter_data_click)
        self.entry_obj.discard_button.clicked.connect(self.on_discard_data_click)
        self.entry_obj.exit_button.clicked.connect(self.on_exit_click)
        
    def showData(self):
        self.dispCompData()
        self.dispRoleData()
        self.dispStatusData()
        self.dispIndustryData()
        # Company
        # self.show_data_layout.addWidget(self.data_tabs)
        # self.show_data_tab.setLayout(self.show_data_layout)
        # pass
    
    def updateData(self):
        self.dispUpdateComp()
        self.dispUpdateStatus()
        self.dispUpdateAll()
        pass
    
    def dispCompData(self):
        self.data_by_company_widget = self.search_comp_obj.create_table_view()
        self.search_comp_obj.searchDataLabel.setText("Company Name")
        self.search_comp_obj.searchDataEntry.setPlaceholderText("Enter Company Name")

        self.search_comp_obj.getDataButton.clicked.connect(self.on_company_search_click)
        self.search_comp_obj.searchDataEntry.returnPressed.connect(self.on_company_search_click)

        self.search_comp_obj.update_comp_button.clicked.connect(self.on_update_comp_button)
        self.search_comp_obj.update_status_button.clicked.connect(self.on_update_status_button)
        self.search_comp_obj.update_all_button.clicked.connect(self.on_update_all_button)
        
    def dispRoleData(self):
        self.data_by_role_widget = self.search_role_obj.create_table_view()
        self.search_role_obj.searchDataLabel.setText("Role Title")
        self.search_role_obj.searchDataEntry.setPlaceholderText("Enter Job title")

        self.search_role_obj.getDataButton.clicked.connect(self.on_role_search_click)
        self.search_role_obj.searchDataEntry.returnPressed.connect(self.on_role_search_click)


        self.search_role_obj.update_comp_button.clicked.connect(lambda: self.on_update_comp_button())
        self.search_role_obj.update_status_button.clicked.connect(lambda: self.on_update_status_button())
        self.search_role_obj.update_all_button.clicked.connect(lambda: self.on_update_all_button())

    def dispStatusData(self):  
        self.data_by_status_widget = self.search_status_obj.create_table_view("status")
        self.search_status_obj.searchDataLabel.setText("Application Status")
        # self.data_by_status_widget = self.search_status_obj.create_data_table()
        self.search_status_obj.getDataButton.clicked.connect(self.on_status_search_click)
        
        self.search_status_obj.searchDataEntry.currentTextChanged.connect(self.on_status_search_click)

        self.search_status_obj.update_comp_button.clicked.connect(lambda: self.on_update_comp_button())
        self.search_status_obj.update_status_button.clicked.connect(lambda: self.on_update_status_button())
        self.search_status_obj.update_all_button.clicked.connect(lambda: self.on_update_all_button())
            
    def dispIndustryData(self):
        self.data_by_industry_widget = self.search_industry_obj.create_table_view()
        self.search_industry_obj.searchDataLabel.setText("Industry")
        self.search_industry_obj.searchDataEntry.setPlaceholderText("Enter Company Industry")
        
        self.search_industry_obj.getDataButton.clicked.connect(self.on_industry_search_click)
        self.search_industry_obj.searchDataEntry.returnPressed.connect(self.on_industry_search_click)
        
        self.search_industry_obj.update_comp_button.clicked.connect(lambda: self.on_update_comp_button())
        self.search_industry_obj.update_status_button.clicked.connect(lambda: self.on_update_status_button())
        self.search_industry_obj.update_all_button.clicked.connect(lambda: self.on_update_all_button())
        
        pass
    
    def dispUpdateComp(self):
        self.update_company = self.update_comp_obj.create_update_comp_box()
        
        
        # self.update_comp_layout.addWidget(self.company_info_label)
        # self.update_comp_layout.addWidget(self.company_info_entry)
        self.update_comp_obj.search_comp_button.clicked.connect(lambda: self.search_comp_data(self.update_comp_obj.search_comp_entry.text()))
        # self.update_comp_obj.search_comp_button.clicked.connect(lambda: print(self.update_comp_obj.search_comp_entry.text()))
        
    def dispUpdateStatus(self):
        self.update_status = self.update_stat_obj.create_update_status_box()
        
        
        compName = self.update_stat_obj.search_comp_entry.text()
        roleTitle = self.update_stat_obj.search_role_entry.text()
        
        self.update_stat_obj.search_role_button.clicked.connect(lambda: self.search_app_status_data(compName,roleTitle))
        
    def dispUpdateAll(self):
        self.update_all = self.update_all_obj.create_update_all_box()
        
        compName = self.update_all_obj.search_comp_entry.text()
        roleTitle = self.update_all_obj.search_role_entry.text()
        
        self.update_all_obj.search_role_button.clicked.connect(lambda: self.search_role_data(compName,roleTitle))
        pass
    
    def search_comp_data(self,compName):
        self.status_bar.showMessage("Getting Company Details",300)

        compName = compName
        # print(compName)
        comp = self.db.get_comp_details_by_name(compName)
        self.update_comp_obj.comp_name_entry.setText(comp.name)
        self.update_comp_obj.industry_entry.setText(comp.industry)
        self.update_comp_obj.hq_state_combo.setCurrentText(comp.state)
        self.update_comp_obj.hq_city_entry.setText(comp.city)
        self.update_comp_obj.website_entry.setText(comp.website)
        self.update_comp_obj.company_size_combo.setCurrentText(comp.company_size)
        self.update_comp_obj.revenue_combo.setCurrentText(comp.revenue)
        self.update_comp_obj.company_info_entry.setText(comp.add_info)
        
    def search_app_status_data(self,compName,roleTitle):
        self.status_bar.showMessage("Getting Application Status Details",300)

        compName = compName
        roleTitle = roleTitle
        comp = self.db.get_comp_details_by_name(compName)
        role = self.db.get_role_details(compName,roleTitle)
        self.update_stat_obj.role_title_entry.setText(role.title)
        self.update_stat_obj.comp_name_entry.setText(comp.name)
        self.update_stat_obj.app_status_combo.setCurrentText(role.app_status)
        self.update_stat_obj.app_result_combo.setCurrentText(role.app_result)
        self.update_stat_obj.remarks_text_entry.setText(role.remarks)
        
        pass
    
    def search_role_data(self,compName,roleTitle):
        self.status_bar.showMessage("Getting Role Details.",1000)
        

        compName = compName
        roleTitle = roleTitle
        self.company = self.db.get_comp_details_by_name(compName)
        self.role = self.db.get_role_details(compName,roleTitle)
        
        self.update_all_obj.comp_name_entry.setText(self.company.name)
        self.update_all_obj.industry_entry.setText(self.company.industry) 
        self.update_all_obj.hq_city_entry.setText(self.company.city) 
        self.update_all_obj.hq_state_combo.setCurrentText(self.company.state) 
        self.update_all_obj.website_entry.setText(self.company.website)
        self.update_all_obj.company_size_combo.setCurrentText(self.company.company_size)
        self.update_all_obj.revenue_combo.setCurrentText(self.company.revenue)
        self.update_all_obj.company_info_entry.setText(self.company.add_info)
        
        self.update_all_obj.role_title_entry.setText(self.role.title)
        self.update_all_obj.job_city_entry.setText(self.role.city)
        self.update_all_obj.job_state_combo.setCurrentText(self.role.state)
        self.update_all_obj.department_entry.setText(self.role.department)
        self.update_all_obj.job_level_combo.setCurrentText(self.role.job_level)
        self.update_all_obj.job_module_combo.setCurrentText(self.role.job_module)
        self.update_all_obj.poc_entry.setText(self.role.poc)
        self.update_all_obj.poc_position_entry.setText(self.role.poc_position)
        self.update_all_obj.poc_origin_entry.setText(self.role.poc_origin)
        self.update_all_obj.app_date_picker.setDate(QDate.fromString(self.role.app_date))
        self.update_all_obj.app_status_combo.setCurrentText(self.role.app_status)
        self.update_all_obj.app_result_combo.setCurrentText(self.role.app_result) 
        self.update_all_obj.role_info_entry.setText(self.role.add_info)
        self.update_all_obj.remarks_text_entry.setText(self.role.remarks)
    
    def on_enter_data_click(self):
        company = self.entry_obj.get_comp_form()
        role = self.entry_obj.get_role_form()
        self.db.insert_company(company)
        self.db.insert_role(role,company)
        self.entry_obj.clearForm()
        self.status_bar.showMessage("Inserted into Database",300)
    
    def on_discard_data_click(self):
        self.status_bar.showMessage("Discarding entry",300)
        print("Discard Placeholder")
        pass
    
    def on_exit_click(self):
        sys.exit()
    
    def on_company_search_click(self):
        # self.statusbar.showMessage("Getting Applications",300)
        self.search_comp_obj.connectDatabase()
        compName = self.search_comp_obj.searchDataEntry.text()
        self.headLabel = QLabel("Company: {}".format(compName))
        print(compName)
        query = QSqlQuery("""SELECT Name,Title, Industry,Poc, Application_status, Application_result FROM Roles, 
                          Companies WHERE Roles.company_ID = Companies.rowid AND Name LIKE '%{}%'""".format(compName))
        query.exec()
        if len(compName)==0:
            self.search_comp_obj.dataTable.setQuery("""SELECT Name, Title, Industry, Poc, Application_status,
                                                    Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid""")
        else: 
            self.search_comp_obj.dataTable.setQuery(query)
        self.search_comp_obj.dataTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
        self.search_comp_obj.tableView.resizeColumnsToContents()
        self.search_comp_obj.searchDataEntry.clear() 
        self.search_comp_obj.closeDatabase()

    def on_role_search_click(self):
        self.search_role_obj.connectDatabase()
        roleTitle = self.search_role_obj.searchDataEntry.text()
        self.headLabel = QLabel("Company: {}".format(roleTitle))
        print(roleTitle)
        query = QSqlQuery("""SELECT Name,Title, Industry,Poc, Application_status, Application_result FROM Roles, 
                          Companies WHERE Roles.company_ID = Companies.rowid AND Title LIKE '%{}%'""".format(roleTitle))
        query.exec()
        if len(roleTitle)==0:
            self.search_role_obj.dataTable.setQuery("""SELECT Name, Title, Industry, Poc, Application_status,
                                                    Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid""")
        else: 
            self.search_role_obj.dataTable.setQuery(query)
        self.search_role_obj.dataTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
        self.search_role_obj.tableView.resizeColumnsToContents()
        self.search_role_obj.searchDataEntry.clear()  
        self.search_role_obj.closeDatabase()
    
    def on_status_search_click(self):
        self.search_status_obj.connectDatabase()
        appStatus = self.search_status_obj.searchDataEntry.currentText()
        self.headLabel = QLabel("Company: {}".format(appStatus))
        print(appStatus)
        query = QSqlQuery("""SELECT Name,Title, Industry,Poc, Application_status, Application_result FROM Roles, 
                          Companies WHERE Roles.company_ID = Companies.rowid AND Roles.Application_status = '{}'""".format(appStatus))
        query.exec()
        if len(appStatus)==0:
            self.search_status_obj.dataTable.setQuery("""SELECT Name, Title, Industry, Poc, Application_status,
                                                    Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid""")
        else: 
            self.search_status_obj.dataTable.setQuery(query)
        self.search_status_obj.dataTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
        self.search_status_obj.tableView.resizeColumnsToContents()
        self.search_status_obj.closeDatabase()
        
    def on_industry_search_click(self):
        self.search_industry_obj.connectDatabase()
        Industry = self.search_industry_obj.searchDataEntry.text()
        self.headLabel = QLabel("Company: {}".format(Industry))
        print(Industry)
        query = QSqlQuery("""SELECT Name,Title, Industry,Poc, Application_status, Application_result FROM Roles, 
                          Companies WHERE Roles.company_ID = Companies.rowid AND Industry LIKE '%{}%'""".format(Industry))
        query.exec()
        if len(Industry)==0:
            self.search_industry_obj.dataTable.setQuery("""SELECT Name, Title, Industry, Poc, Application_status,
                                                    Application_result FROM Roles, Companies WHERE Roles.company_ID = Companies.rowid""")
        else: 
            self.search_industry_obj.dataTable.setQuery(query)
        self.search_industry_obj.dataTable.setHeaderData(0,Qt.Orientation.Horizontal,"Company")
        self.search_industry_obj.tableView.resizeColumnsToContents()
        self.search_industry_obj.searchDataEntry.clear()  
        self.search_industry_obj.closeDatabase()
    
    def on_update_comp_button(self):
        self.main_tabs.setCurrentIndex(2)
        self.update_tabs.setCurrentIndex(0)
        match self.data_tabs.currentIndex():
            case 0:
                selection = self.search_comp_obj.tableView.selectionModel()
                index = self.search_comp_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_comp_obj.tableView.model().data(self.search_comp_obj.tableView.model().index(row,0))
                self.search_comp_data(Company)    
            case 1:
                selection = self.search_role_obj.tableView.selectionModel()
                index = self.search_role_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_role_obj.tableView.model().data(self.search_role_obj.tableView.model().index(row,0))                
                self.search_comp_data(Company)    
            case 2:
                selection = self.search_status_obj.tableView.selectionModel()
                index = self.search_status_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_status_obj.tableView.model().data(self.search_status_obj.tableView.model().index(row,0))
                self.search_comp_data(Company)    
            case 3:
                selection = self.search_industry_obj.tableView.selectionModel()
                index = self.search_industry_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_industry_obj.tableView.model().data(self.search_industry_obj.tableView.model().index(row,0))
                self.search_comp_data(Company)    

    def on_update_status_button(self):
        self.main_tabs.setCurrentIndex(2)
        self.update_tabs.setCurrentIndex(1)
        match self.data_tabs.currentIndex():
            case 0:
                selection = self.search_comp_obj.tableView.selectionModel()
                index = self.search_comp_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_comp_obj.tableView.model().data(self.search_comp_obj.tableView.model().index(row,0))
                Role = self.search_comp_obj.tableView.model().data(self.search_comp_obj.tableView.model().index(row,1))
                self.search_app_status_data(Company,Role)
            case 1:
                selection = self.search_role_obj.tableView.selectionModel()
                index =  self.search_role_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_role_obj.tableView.model().data(self.search_role_obj.tableView.model().index(row,0))
                Role = self.search_role_obj.tableView.model().data(self.search_role_obj.tableView.model().index(row,1))
                self.search_app_status_data(Company,Role)
            case 2:
                selection = self.search_status_obj.tableView.selectionModel()
                index = self.search_status_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_status_obj.tableView.model().data(self.search_status_obj.tableView.model().index(row,0))
                Role = self.search_status_obj.tableView.model().data(self.search_status_obj.tableView.model().index(row,1))
                self.search_app_status_data(Company,Role)
            case 3:
                selection = self.search_industry_obj.tableView.selectionModel()
                index = self.search_industry_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_industry_obj.tableView.model().data(self.search_industry_obj.tableView.model().index(row,0))
                Role = self.search_industry_obj.tableView.model().data(self.search_industry_obj.tableView.model().index(row,1))
                self.search_app_status_data(Company,Role)
    
    def  on_update_all_button(self):
        self.main_tabs.setCurrentIndex(2)
        self.update_tabs.setCurrentIndex(2)
        match self.data_tabs.currentIndex():
            case 0:
                selection = self.search_comp_obj.tableView.selectionModel()
                index = self.search_comp_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_comp_obj.tableView.model().data(self.search_comp_obj.tableView.model().index(row,0))
                Role = self.search_comp_obj.tableView.model().data(self.search_comp_obj.tableView.model().index(row,1))
                self.search_role_data(Company,Role)
    
            case 1:
                selection = self.search_role_obj.tableView.selectionModel()
                index = self.search_role_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_role_obj.tableView.model().data(self.search_role_obj.tableView.model().index(row,0))
                Role = self.search_role_obj.tableView.model().data(self.search_role_obj.tableView.model().index(row,1))
                self.search_role_data(Company,Role)
    
            case 2:
                selection = self.search_status_obj.tableView.selectionModel()
                index = self.search_status_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_status_obj.tableView.model().data(self.search_status_obj.tableView.model().index(row,0))
                Role = self.search_status_obj.tableView.model().data(self.search_status_obj.tableView.model().index(row,1))
                self.search_role_data(Company,Role)
    
            case 3:
                selection = self.search_industry_obj.tableView.selectionModel()
                index = self.search_industry_obj.tableView.currentIndex()
                row = index.row()
                Company = self.search_industry_obj.tableView.model().data(self.search_industry_obj.tableView.model().index(row,0))
                Role = self.search_industry_obj.tableView.model().data(self.search_industry_obj.tableView.model().index(row,1))
                self.search_role_data(Company,Role)

    @QtCore.pyqtSlot()
    def on_tab(self):
        if self.main_tabs.currentIndex() == 1:
            current_tab = self.data_tabs.currentIndex()
            self.data_tabs.setCurrentIndex((current_tab + 1) % self.data_tabs.count())
        elif self.main_tabs.currentIndex() == 2:
            current_tab = self.update_tabs.currentIndex()
            self.update_tabs.setCurrentIndex((current_tab + 1) % self.update_tabs.count())

    @QtCore.pyqtSlot()
    def on_shift_tab(self):
        if self.main_tabs.currentIndex() == 1:
            current_tab = self.data_tabs.currentIndex()
            self.data_tabs.setCurrentIndex((current_tab - 1) % self.data_tabs.count())
        elif self.main_tabs.currentIndex() == 2:
            current_tab = self.update_tabs.currentIndex()
            self.update_tabs.setCurrentIndex((current_tab - 1) % self.update_tabs.count())
            
    def on_ver_change(self,i):
        match i:
            case 0:
                self.entry_obj.comp_name_entry.setFocus()
            case 1:
                pass
            case 2:
                pass
    
    def on_data_change(self,i):
        match i:
            case 0:
                self.search_comp_obj.searchDataEntry.setFocus()
            case 1:
                self.search_role_obj.searchDataEntry.setFocus()
            case 2: 
                self.search_status_obj.searchDataEntry.setFocus()
            case 3:
                self.search_industry_obj.searchDataEntry.setFocus()

    def on_update_change(self,i):
        match i:
            case 0:
                self.update_comp_obj.search_comp_entry.setFocus()
            case 1:
                self.update_stat_obj.search_comp_entry.setFocus()
            case 2:
                self.update_all_obj.search_comp_entry.setFocus()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress:
            # tab_widget = self.main_tabs.findChild(QTabWidget)
            if event.key() == Qt.Key.Key_Tab and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
                print(self.main_tabs.currentIndex())
                event.ignore()
              
                return True

        return super().eventFilter(obj, event)
    
    # def connectDatabase(self):
    #     self.conn = QSqlDatabase.addDatabase('QSQLITE')
    #     self.conn.setDatabaseName('.\ApplicationDatabase\Database\database.db')
    #     # self.conn.setDatabaseName('database.db')
    #     if not self.conn.open():
    #         QMessageBox.critical(
    #             None,
    #             "App Name - Error",
    #             "Database Error: %s" % self.conn.lastError().databaseText(),
    #         )
    
    def createMenuBar(self):
        self.menu_bar = self.menuBar()
        fileMenu = self.menu_bar.addMenu("&File")
        fileMenu.addAction(self.newEntryAction)
        fileMenu.addSeparator
        fileMenu.addAction(self.discardAction)
        fileMenu.addAction(self.exitAction)
        
        dataMenu = self.menu_bar.addMenu("&Data")
        dataMenu.addActions([self.byCompanyAction,self.byRoleAction,
                             self.byStatusAction,self.byIndustryAction])
    
    def createActions(self):
        self.newEntryAction = QAction("&New Entry")
        self.discardAction = QAction("D&iscard")
        self.exitAction = QAction("&Exit")
        
        self.byCompanyAction = QAction("By &Company")        
        self.byRoleAction = QAction("By &Role")
        self.byStatusAction = QAction("By &Status")
        self.byIndustryAction = QAction("By &Industry")
        
        self.discardAction.triggered.connect(self.on_discard_data_click)
        

        self.exitAction.triggered.connect(self.on_exit_click)
    
    def createStatusBar(self):
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def styling(self):
        style = """ 
        QMainWindow {background-color: LightGray}
        QGroupBox {background-color: White}
        """
        self.setStyleSheet(style)
    
    def set_groupboxes_background_color(self,color, widget):
        if isinstance(widget, (QGroupBox,QLineEdit,QLabel,QComboBox)):
            widget.setStyleSheet(f"QGroupBox {{ background-color: {color}; }}")
        # for child_widget in widget.findChildren(QGroupBox):
        for child_widget in widget.findChildren((QGroupBox,QLineEdit,QLabel,QComboBox)):
            self.set_groupboxes_background_color(color, child_widget)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ApplicationVer2()
    win.show()
    # win.closeDatabase()
    sys.exit(app.exec())