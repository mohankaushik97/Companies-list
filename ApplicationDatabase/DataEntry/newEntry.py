import sqlite3
import sys
sys.path.insert(0, 'D:\Companies list\ApplicationDatabase')
from datetime import date
from typing import Any
from PyQt6.QtCore import  Qt

# from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame,
#                              QComboBox, QGridLayout, QLabel, QGroupBox, QMainWindow,QMenuBar,QMenu,QStatusBar)
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon,QAction
from Objects.company import Company
from Objects.role import Role
from Database.database import Database

class NewEntry(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(NewEntry, self).__init__(*args, **kwargs)
        self.setWindowTitle('Application Info')
        # self.setContentsMargins(10,10,10,10)
        self.db = Database()

        # self.createActions()
        # self.createStatusBar()
        # self.createMenuBar()

        self.companyInfoLayout()
        self.roleInfoLayout()
        self.buttonGroupLayout()
        self.AdditionalInfoLayout()
        self.createFinalLayout()
        self.company_name_entry.setFocus()
        self.styling()
        
    def styling(self):
        style = """ 
        QMainWindow {background-color: LightGray}
        QGroupBox {background-color: White}
        """
        self.setStyleSheet(style)

    def ifMain(self):
        self.createActions()
        self.createStatusBar()
        self.createMenuBar()
        
    def createFinalLayout(self):
        self.cw = QWidget()
        self.setCentralWidget(self.cw)

        self.main_layout = QHBoxLayout()
        self.cw.setLayout(self.main_layout)

        self.form_layout = QVBoxLayout()
        self.info_layout = QVBoxLayout()

        self.form_layout.addWidget(self.company_group)
        self.form_layout.addWidget(self.role_group)
        self.info_layout.addWidget(self.additional_info_group)
        self.info_layout.addWidget(self.button_frame)
        
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.info_layout)

    def companyInfoLayout(self):
        self.company_group = QGroupBox("Company Information")

        self.company_layout = QVBoxLayout()
        self.company_layout.setContentsMargins(20,20,20,20)

        self.name_layout = QVBoxLayout()
        self.name_layout.setContentsMargins(20,20,20,0)
        
        self.company_grid = QGridLayout()
        self.company_grid.setContentsMargins(20,20,20,20)
        self.company_group.setLayout(self.company_layout)

        self.company_layout.addLayout(self.name_layout)
        self.company_layout.addLayout(self.company_grid)

        self.company_name_label = QLabel("Company Name")
        self.company_name_entry = QLineEdit()
        self.name_layout.addWidget(self.company_name_label)
        self.name_layout.addWidget(self.company_name_entry)
        
        # TODO: Dropdown
        self.industry_label = QLabel("Industry")
        self.industry_entry = QLineEdit()
        self.company_grid.addWidget(self.industry_label,0,0)
        self.company_grid.addWidget(self.industry_entry,1,0)
        
        self.hq_city_label = QLabel("HQ City")
        self.hq_city_entry = QLineEdit()
        self.company_grid.addWidget(self.hq_city_label,0,1)
        self.company_grid.addWidget(self.hq_city_entry,1,1)

        self.hq_state_combo = QComboBox()
        self.hq_state_combo.setPlaceholderText("State")
        self.hq_state_combo.addItems(["AL ","AK ","AZ ","AR ","CA ","CO ","CT ","DE ","FL ",
                                       "GA ","HI ","ID ","IL ","IN ","IA ","KS ","KY ","LA ",
                                       "ME ","MD ","MA ","MI ","MN ","MS ","MO ","MT ","NE ",
                                       "NV ","NH ","NJ ","NM ","NY ","NC ","ND ","OH ","OK ",
                                       "OR ","PA ","RI ","SC ","SD ","TN ","TX ","UT ","VT ",
                                       "VA ","WA ","WV ","WI ","WY ","DC","AS ","GU ","MP ","PR"])
        self.hq_state_label = QLabel("HQ State")
        self.company_grid.addWidget(self.hq_state_label,0,2)
        self.company_grid.addWidget(self.hq_state_combo,1,2)

        self.website_label = QLabel("Website")
        self.website_entry = QLineEdit()
        self.company_grid.addWidget(self.website_label,2,0)
        self.company_grid.addWidget(self.website_entry,3,0)

        self.company_size_label = QLabel("Number of Employees")
        self.company_size_combo = QComboBox()
        self.company_size_combo.setPlaceholderText("Employees")
        self.company_size_combo.addItems(['1 to 20','20 to 99','100-999','1,000-9,999','10,000-99,999','100,000+'])
        self.company_grid.addWidget(self.company_size_label,2,1)
        self.company_grid.addWidget(self.company_size_combo,3,1)

        self.revenue_label = QLabel("Company Revenue")
        self.revenue_combo = QComboBox()
        self.revenue_combo.setPlaceholderText("Revenue")
        self.revenue_combo.addItems(['<$5M','$5M-$99M','$100M-$999M','$1B+'])
        self.company_grid.addWidget(self.revenue_label,2,2)
        self.company_grid.addWidget(self.revenue_combo,3,2)

    def roleInfoLayout(self):
        self.role_group = QGroupBox("Role Information") 

        self.role_grid = QGridLayout()
        self.role_grid.setContentsMargins(20,20,20,20)

        self.app_grid = QGridLayout()
        self.app_grid.setContentsMargins(20,0,20,20)
        
        self.role_layout = QVBoxLayout()
        self.role_layout.addLayout(self.role_grid,0)
        self.role_layout.addLayout(self.app_grid,1)

        self.role_group.setLayout(self.role_layout)


        self.role_title_label = QLabel("Job Title")
        self.role_title_entry = QLineEdit()
        self.role_grid.addWidget(self.role_title_label,0,0)
        self.role_grid.addWidget(self.role_title_entry,1,0)
        
        self.job_city_label = QLabel("Job City")
        self.job_city_entry = QLineEdit()
        self.role_grid.addWidget(self.job_city_label,0,1)
        self.role_grid.addWidget(self.job_city_entry,1,1)

        self.job_state_combo = QComboBox()
        self.job_state_combo.setPlaceholderText("State")
        self.job_state_combo.addItems(["AL ","AK ","AZ ","AR ","CA ","CO ","CT ","DE ","FL ",
                                       "GA ","HI ","ID ","IL ","IN ","IA ","KS ","KY ","LA ",
                                       "ME ","MD ","MA ","MI ","MN ","MS ","MO ","MT ","NE ",
                                       "NV ","NH ","NJ ","NM ","NY ","NC ","ND ","OH ","OK ",
                                       "OR ","PA ","RI ","SC ","SD ","TN ","TX ","UT ","VT ",
                                       "VA ","WA ","WV ","WI ","WY ","DC","AS ","GU ","MP ","PR"])
        self.job_state_label = QLabel("Job State")
        self.role_grid.addWidget(self.job_state_label,0,2)
        self.role_grid.addWidget(self.job_state_combo,1,2)
        
        self.job_level_combo = QComboBox()
        self.job_level_combo.setPlaceholderText("Job Level")
        self.job_level_combo.addItems(["Internship", "New Grad", 'Engineer I','Engineer II','Engineer III','Start-up'])
        self.job_level_label = QLabel("Job Level")
        self.role_grid.addWidget(self.job_level_label,2,0)
        self.role_grid.addWidget(self.job_level_combo,3,0)
        
        self.job_module_combo = QComboBox()
        self.job_module_combo.setPlaceholderText("Module")
        self.job_module_combo.addItems(['Primary','Support'])
        self.job_module_label = QLabel("Job Module")
        self.role_grid.addWidget(self.job_module_label,2,1)
        self.role_grid.addWidget(self.job_module_combo,3,1)

        self.department_label = QLabel("Department")
        self.department_entry = QLineEdit()
        self.role_grid.addWidget(self.department_label,2,2)
        self.role_grid.addWidget(self.department_entry,3,2)

        self.poc_label = QLabel("Person of Contact")
        self.poc_entry = QLineEdit()
        self.role_grid.addWidget(self.poc_label,4,0)
        self.role_grid.addWidget(self.poc_entry,5,0)

        self.poc_position_label = QLabel("PoC - Position")
        self.poc_position_entry = QLineEdit()
        self.role_grid.addWidget(self.poc_position_label,4,1)
        self.role_grid.addWidget(self.poc_position_entry,5,1)

        self.poc_origin_label = QLabel("PoC - Origin")
        self.poc_origin_entry = QLineEdit()
        self.role_grid.addWidget(self.poc_origin_label,4,2)
        self.role_grid.addWidget(self.poc_origin_entry,5,2)
        
        
        self.app_date_picker = QDateEdit()
        self.app_date_picker.setDate(date.today())
        self.app_date_label = QLabel("Application Date")
        self.app_grid.addWidget(self.app_date_label,0,0)
        self.app_grid.addWidget(self.app_date_picker,1,0)
        
        self.app_status_combo = QComboBox()
        self.app_status_combo.setPlaceholderText("Status")
        self.app_status_combo.addItems(['Applied','In-Reivew','Interview-1','Interview-2','Interview-3'])
        self.app_status_label = QLabel("Application Status")
        self.app_grid.addWidget(self.app_status_label,0,1)
        self.app_grid.addWidget(self.app_status_combo,1,1)

        self.app_result_combo = QComboBox()
        self.app_result_combo.setPlaceholderText("Result")
        self.app_result_combo.addItems(['In-Process','Accepted','Rejected'])
        self.app_result_label = QLabel("Application Result")        
        self.app_grid.addWidget(self.app_result_label,0,2)
        self.app_grid.addWidget(self.app_result_combo,1,2)

    def AdditionalInfoLayout(self):
        self.additional_info_group = QGroupBox("Additional Info")
        
        self.add_info_layout = QVBoxLayout()
        self.additional_info_group.setLayout(self.add_info_layout)

        
        # LABELS
        self.remarks_text_label = QLabel("Remarks")
        self.company_info_label = QLabel("Company Info")
        self.role_info_label = QLabel("Role Info")
        
        # ENTRY BOXES
        self.remarks_text_entry = QTextEdit()
        self.company_info_entry = QTextEdit()
        self.role_info_entry = QTextEdit()
        self.remarks_text_entry.setTabChangesFocus(True)
        self.company_info_entry.setTabChangesFocus(True)
        self.role_info_entry.setTabChangesFocus(True)
        
        
        # ADDING WIDGETS
        self.add_info_layout.addWidget(self.remarks_text_label)
        self.add_info_layout.addWidget(self.remarks_text_entry)
        self.add_info_layout.addWidget(self.company_info_label)
        self.add_info_layout.addWidget(self.company_info_entry)
        self.add_info_layout.addWidget(self.role_info_label)
        self.add_info_layout.addWidget(self.role_info_entry)
        
        
        pass
        
    def buttonGroupLayout(self):
        self.button_layout = QVBoxLayout()
        self.button_frame = QFrame()
        self.button_frame.setLayout(self.button_layout)


        self.data_enter_button = QPushButton("Enter Data")
        self.button_layout.addWidget(self.data_enter_button)
        self.data_enter_button.clicked.connect(self.onButtonClick)

        self.exit_button = QPushButton("Close")
        self.button_layout.addWidget(self.exit_button)
        self.exit_button.clicked.connect(self.close)
        
    def getCompanyData(self):
        self.company = Company()
        self.company.name = self.company_name_entry.text()
        self.company.industry = self.industry_entry.text()
        self.company.city = self.hq_city_entry.text()
        self.company.state = self.hq_state_combo.currentText()
        self.company.website = self.website_entry.text()
        self.company.company_size = self.company_size_combo.currentText()
        self.company.revenue = self.revenue_combo.currentText()
        self.company.add_info = self.company_info_entry.toPlainText()
        return self.company
    
    def getRoleData(self):
        self.role = Role()
        self.role.title = self.role_title_entry.text()
        self.role.city = self.job_city_entry.text()
        self.role.state = self.job_state_combo.currentText()
        self.role.department = self.department_entry.text()
        self.role.job_level = self.job_level_combo.currentText()
        self.role.job_module = self.job_module_combo.currentText()
        self.role.poc = self.poc_entry.text()
        self.role.poc_position = self.poc_position_entry.text()
        self.role.poc_origin = self.poc_origin_entry.text()
        self.role.app_date = self.app_date_picker.text()
        self.role.app_status = self.app_status_combo.currentText()
        self.role.app_result = self.app_result_combo.currentText() 
        self.role.add_info = self.role_info_entry.toPlainText()
        self.role.remarks = self.remarks_text_entry.toPlainText()
        return self.role
    
    def clearForm(self):
        self.role_title_entry.clear()
        self.job_city_entry.clear()
        self.job_state_combo.setCurrentIndex(-1)
        self.department_entry.clear()
        self.job_level_combo.setCurrentIndex(-1)
        self.job_module_combo.setCurrentIndex(-1)
        self.poc_entry.clear()
        self.poc_origin_entry.clear()
        self.poc_position_entry.clear()
        self.app_date_picker.setDate(date.today())
        self.app_status_combo.setCurrentIndex(-1)
        self.app_result_combo.setCurrentIndex(-1)
        self.role_info_entry.clear()
        self.remarks_text_entry.clear()

        self.company_name_entry.clear()
        self.industry_entry.clear()
        self.hq_city_entry.clear()
        self.hq_state_combo.setCurrentIndex(-1)
        self.website_entry.clear()
        self.company_size_combo.setCurrentIndex(-1)
        self.revenue_combo.setCurrentIndex(-1)
        self.company_info_entry.clear()

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
        
        self.discardAction.triggered.connect(lambda: self.clearForm())
        self.discardAction.triggered.connect(lambda: self.statusbar.showMessage("Discarding entry",300))

        self.exitAction.triggered.connect(lambda: self.close())
        
    def createStatusBar(self):
        
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

    def onButtonClick(self):
        company = self.getCompanyData()
        role = self.getRoleData()
        self.db.insert_company(company)
        self.db.insert_role(role,company)
        self.clearForm()
        self.statusbar.showMessage("Inserted into Database",300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= NewEntry()
    window.ifMain()
    window.show()
    app.exec()