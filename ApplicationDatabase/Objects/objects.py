from dataclasses import InitVar
import sys
from datetime import date
from webbrowser import get
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QFont,QShortcut,QKeySequence
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt, QEvent
from PyQt6 import QtCore

sys.path.insert(0, 'D:\Companies list\ApplicationDatabase')
from Objects.company import Company
from Objects.role import Role


class ObjImports():
    def __init__(self):
        pass

    
    def initVars(self):
        # TAB Organisers    
        # Widgets
        
        self.data_by_company_widget = QWidget()
        self.data_by_role_widget = QWidget()
        self.data_by_state_widget = QWidget()
        self.data_by_status_widget = QWidget()
        self.data_by_industry_widget = QWidget()
        
        self.update_company = QFrame()
        self.update_status = QWidget()
        self.update_all = QWidget()
        
        self.new_entry_tab = QWidget()

        # GroupBox
        self.company_info_box =  QGroupBox("Company Details")
        self.role_info_box = QGroupBox("Role Details")
        self.add_info_box = QGroupBox("Additional Details")
        self.three_button_box = QFrame()
        self.update_comp_info_box = QFrame()
        self.update_button_box = QFrame()
        self.update_stat_box = QGroupBox("Application Status")
        
        self.company_search_box = QGroupBox("Search Company")
        self.role_search_box = QGroupBox("Search Role")
        
        # Layouts
        self.company_grid_layout = QGridLayout()
        self.role_grid_layout = QGridLayout()
        self.add_info_layout = QVBoxLayout()
        self.three_button_layout = QVBoxLayout()
        
        self.comp_role_vlayout = QVBoxLayout()
        self.add_button_vlayout = QVBoxLayout()
        self.new_entry_layout = QHBoxLayout()
        
        self.update_comp_layout = QVBoxLayout()
        
        self.update_comp_info_layout = QVBoxLayout()
        self.update_button_layout = QGridLayout()
        self.update_stat_layout = QGridLayout()
        self.search_comp_layout = QHBoxLayout()
        self.search_role_layout = QGridLayout()
        
        self.update_status_layout = QVBoxLayout()

        
        self.update_comp_role_vlayout = QVBoxLayout()
        self.update_add_button_vlayout = QVBoxLayout()
        self.update_all_box_layout = QGridLayout()

        
        
        self.initLabels()
        self.initEntry()
        self.initButtons()
        
    def initLabels(self):
        # Labels
        self.comp_name_label = QLabel("Company Name")
        self.industry_label = QLabel("Industry")
        self.hq_city_label = QLabel("HQ City")
        self.hq_state_label = QLabel("HQ State")
        self.company_size_label = QLabel("Number of Employees")
        self.revenue_label = QLabel("Company Revenue")
        self.website_label = QLabel("Website")

        self.role_title_label = QLabel("Job Title")
        self.job_city_label = QLabel("Job City")
        self.job_state_label = QLabel("Job State")
        self.job_level_label = QLabel("Job Level")
        self.job_module_label = QLabel("Job Module")
        self.department_label = QLabel("Department")
        self.poc_label = QLabel("Person of Contact")
        self.poc_position_label = QLabel("PoC - Position")
        self.poc_origin_label = QLabel("PoC - Origin")
        self.app_date_label = QLabel("Application Date")
        self.app_status_label = QLabel("Application Status")
        self.app_result_label = QLabel("Application Result")        

        self.remarks_text_label = QLabel("Remarks")
        self.company_info_label = QLabel("Company Info")
        self.role_info_label = QLabel("Role Info")
        
        self.search_comp_label = QLabel("Company: ")
        self.search_role_label = QLabel("Role: ")

    def initEntry(self):
        # LineEdit
        self.comp_name_entry = QLineEdit()
        self.industry_entry = QLineEdit()
        self.hq_city_entry = QLineEdit()
        self.website_entry = QLineEdit()
        
        self.role_title_entry = QLineEdit()
        self.job_city_entry = QLineEdit()
        self.department_entry = QLineEdit()
        self.poc_entry = QLineEdit()
        self.poc_position_entry = QLineEdit()
        self.poc_origin_entry = QLineEdit()

        self.search_comp_entry = QLineEdit()
        self.search_role_entry = QLineEdit()

        # DatePicker
        self.app_date_picker = QDateEdit()
        self.app_date_picker.setDate(date.today())


        # ComboBox
        self.hq_state_combo = QComboBox()
        self.company_size_combo = QComboBox()
        self.revenue_combo = QComboBox()
        
        self.job_state_combo = QComboBox()
        self.job_level_combo = QComboBox()
        self.job_module_combo = QComboBox()
        self.app_status_combo = QComboBox()
        self.app_result_combo = QComboBox()
        
        self.comp_name_entry.setPlaceholderText("Company Name")
        self.industry_entry.setPlaceholderText("Industry")
        self.hq_city_entry.setPlaceholderText("City")
        self.website_entry.setPlaceholderText("Website")
        self.hq_state_combo.setPlaceholderText("State")
        self.company_size_combo.setPlaceholderText("Employees")
        self.revenue_combo.setPlaceholderText("Revenue")
        
        self.role_title_entry.setPlaceholderText("Job Title")
        self.job_city_entry.setPlaceholderText("Work Location - City")
        self.department_entry.setPlaceholderText("Department")
        self.poc_entry.setPlaceholderText("Point of contact")
        self.poc_position_entry.setPlaceholderText("PoC Position")
        self.poc_origin_entry.setPlaceholderText("PoC Origin")

        
        self.job_state_combo.setPlaceholderText("State")
        self.job_level_combo.setPlaceholderText("Job Level")
        self.job_module_combo.setPlaceholderText("Module")
        self.app_status_combo.setPlaceholderText("Status")
        self.app_result_combo.setPlaceholderText("Result")
        
        self.search_comp_entry.setPlaceholderText("Enter Company Name")
        self.search_role_entry.setPlaceholderText("Enter Job Title")

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

        self.hq_state_combo.addItems(self.state)
        self.company_size_combo.addItems(self.comp_size)
        self.revenue_combo.addItems(self.comp_revenue)
        self.job_state_combo.addItems(self.state)
        self.job_level_combo.addItems(self.job_level)
        self.job_module_combo.addItems(['Primary','Support'])
        self.app_status_combo.addItems(self.app_status)
        self.app_result_combo.addItems(self.app_result)
        
        # Text Edits
        self.remarks_text_entry = QTextEdit()
        self.company_info_entry = QTextEdit()
        self.role_info_entry = QTextEdit()
        self.remarks_text_entry.setTabChangesFocus(True)
        self.company_info_entry.setTabChangesFocus(True)
        self.role_info_entry.setTabChangesFocus(True)
        self.remarks_text_entry.setPlaceholderText("Interview Questions")
        self.company_info_entry.setPlaceholderText("Company information")
        self.role_info_entry.setPlaceholderText("Role information")
        
    def initButtons(self):
        self.enter_data_button = QPushButton("Enter Data")
        self.exit_button = QPushButton("Exit")
        self.discard_button = QPushButton("Discard")
        
        self.update_button = QPushButton("Update")
        self.update_discard_button = QPushButton("Discard")
        
        self.search_comp_button = QPushButton("Search Company")
        self.search_role_button = QPushButton("Search Role")
        
        self.enter_data_button.setStyleSheet(
            """
            QPushButton {
                background-color: #A6F5A2; /* Normal state color */
                color: black;
            }
            QPushButton:pressed {
                background-color: #7AF274; /* Clicked state color */
            }
            """)
        
        self.update_button.setStyleSheet(
            """
            QPushButton {
                background-color: #A6F5A2; /* Normal state color */
                color: black;
            }
            QPushButton:pressed {
                background-color: #7AF274; /* Clicked state color */
            }
            """)

        self.exit_button.setStyleSheet(
            """
            QPushButton {
                background-color: #fa7f7f; /* Normal state color */
                color: black;
            }
            QPushButton:pressed {
                background-color: #fa5555; /* Clicked state color */
            }
            """
        )
    
        self.discard_button.setStyleSheet(
            """
            QPushButton {
                background-color: #fcc488; /* Normal state color */
                color: black;
            }
            QPushButton:pressed {
                background-color: #f7aa57; /* Clicked state color */
            }
            """
        )
    
        self.update_discard_button.setStyleSheet(
            """
            QPushButton {
                background-color: #fcc488; /* Normal state color */
                color: black;
            }
            QPushButton:pressed {
                background-color: #f7aa57; /* Clicked state color */
            }
            """
        )
    
    def create_new_entry_box(self):
        self.initVars()

        self.new_entry_tab.setLayout(self.new_entry_layout)

        [line_edit.setMinimumSize(150, 20) for line_edit in self.new_entry_tab.findChildren(QLineEdit)]
        [text_edit.setMinimumWidth(200) for text_edit in self.new_entry_tab.findChildren(QTextEdit)]
        [group_box.setStyleSheet("background-color: white;") for group_box in self.new_entry_tab.findChildren(QGroupBox)]
        
        self.new_entry_layout.addLayout(self.comp_role_vlayout)
        self.new_entry_layout.addLayout(self.add_button_vlayout)
        # self.new_entry_layout.addLayout(self.comp_role_vlayout)
        
        self.comp_role_vlayout.addWidget(self.company_info_box)
        self.comp_role_vlayout.addWidget(self.role_info_box)
        
        self.add_button_vlayout.addWidget(self.add_info_box)
        self.add_button_vlayout.addWidget(self.three_button_box)
        
        self.disp_comp_group()
        self.disp_role_group()
        self.disp_add_info_group()
        self.disp_button_group()

        
        return self.new_entry_tab

    def create_update_comp_box(self):
        self.initVars()
        
        self.update_company.setLayout(self.update_comp_layout)

        # self.update_comp_layout.addWidget(self.company_info_box)
        # self.update_comp_layout.addWidget(self.role_info_box)
        # self.update_comp_layout.addWidget(self.add_info_box)
        # self.update_comp_layout.addWidget(self.three_button_box)
        
        # self.dispCompGroup()
        # self.dispRoleGroup()
        # self.dispAddInfoGroup()
        # self.dispButtonGroup()
        
        self.update_comp_layout.addWidget(self.company_search_box)
        self.update_comp_layout.addWidget(self.company_info_box)
        self.update_comp_layout.addWidget(self.update_comp_info_box)
        self.update_comp_layout.addWidget(self.update_button_box)
        
        self.disp_comp_search_box()
        self.disp_comp_group()
        self.disp_update_comp_info_box()
        self.disp_update_button_box()
        
        return self.update_company

    def create_update_status_box(self):
        self.initVars()
        
        self.update_status.setLayout(self.update_status_layout)
        
        self.update_status_layout.addWidget(self.role_search_box)
        self.update_status_layout.addWidget(self.update_stat_box)
        self.update_status_layout.addWidget(self.update_button_box)
        
        self.disp_role_search_box()
        self.disp_update_stat_box()
        self.disp_update_button_box()
        
        return self.update_status

    def create_update_all_box(self):
        self.initVars()
        self.update_all.setLayout(self.update_all_box_layout)
        
    
        
        self.enter_data_button.setText("Update")
        
        
        self.update_all_box_layout.addWidget(self.role_search_box,0,0,1,2)
        self.update_all_box_layout.addLayout(self.update_comp_role_vlayout,1,0)
        self.update_all_box_layout.addLayout(self.update_add_button_vlayout,1,1)
        
        self.update_comp_role_vlayout.addWidget(self.company_info_box)
        self.update_comp_role_vlayout.addWidget(self.role_info_box)
        self.update_add_button_vlayout.addWidget(self.add_info_box)
        self.update_add_button_vlayout.addWidget(self.update_button_box)
        
        self.disp_role_search_box()
        self.disp_comp_group()
        self.disp_role_group()
        self.disp_add_info_group()
        self.disp_update_button_box()
        
        return self.update_all

    def disp_update_comp_info_box(self):
        self.update_comp_info_box.setLayout(self.update_comp_info_layout)
        
        self.update_comp_info_layout.addWidget(self.company_info_label)
        self.update_comp_info_layout.addWidget(self.company_info_entry)
            
    def disp_comp_search_box(self):
        self.company_search_box.setLayout(self.search_comp_layout)
        
        self.search_comp_layout.addWidget(self.comp_name_label)
        self.search_comp_layout.addWidget(self.search_comp_entry)
        self.search_comp_layout.addWidget(self.search_comp_button)
                
    def disp_role_search_box(self):
        self.role_search_box.setLayout(self.search_role_layout)
        
        self.search_role_button.setMinimumSize(150,50)
        
        self.search_role_layout.addWidget(self.search_comp_label,0,0)
        self.search_role_layout.addWidget(self.search_comp_entry,0,1)
        self.search_role_layout.addWidget(self.search_role_label,1,0)
        self.search_role_layout.addWidget(self.search_role_entry,1,1)
        self.search_role_layout.addWidget(self.search_role_button,0,2,2,2)
                
    def disp_update_button_box(self):

        self.update_button_box.setLayout(self.update_button_layout)
        
        self.update_button_layout.addWidget(self.update_button,0,0)
        self.update_button_layout.addWidget(self.update_discard_button,0,1)
        
        return self.update_button_box
    
    def disp_update_stat_box(self):
        self.update_stat_box.setLayout(self.update_stat_layout)
        
        self.update_stat_layout.addWidget(self.role_title_label,0,0)
        self.update_stat_layout.addWidget(self.role_title_entry,1,0)
        
        self.update_stat_layout.addWidget(self.comp_name_label,0,1)
        self.update_stat_layout.addWidget(self.comp_name_entry,1,1)
    
        self.update_stat_layout.addWidget(self.app_result_label,2,1)
        self.update_stat_layout.addWidget(self.app_result_combo,3,1)
        
        self.update_stat_layout.addWidget(self.app_status_label,2,0)
        self.update_stat_layout.addWidget(self.app_status_combo,3,0)
        
        self.update_stat_layout.addWidget(self.remarks_text_label,4,0,1,2)
        self.update_stat_layout.addWidget(self.remarks_text_entry,5,0,1,2)
        
    
    def disp_comp_group(self):
        self.company_info_box.setLayout(self.company_grid_layout)
        # COMPANY GROUP
        self.company_grid_layout.addWidget(self.comp_name_label,0,0,1,3)
        self.company_grid_layout.addWidget(self.comp_name_entry,1,0,1,3)
        
        self.company_grid_layout.addWidget(self.industry_label,2,0)
        self.company_grid_layout.addWidget(self.industry_entry,3,0)
        
        self.company_grid_layout.addWidget(self.hq_city_label,2,1)
        self.company_grid_layout.addWidget(self.hq_city_entry,3,1)
        
        self.company_grid_layout.addWidget(self.hq_state_label,2,2)
        self.company_grid_layout.addWidget(self.hq_state_combo,3,2)
        
        self.company_grid_layout.addWidget(self.website_label,4,0)
        self.company_grid_layout.addWidget(self.website_entry,5,0)
        
        self.company_grid_layout.addWidget(self.company_size_label,4,1)
        self.company_grid_layout.addWidget(self.company_size_combo,5,1)
        
        self.company_grid_layout.addWidget(self.revenue_label,4,2)
        self.company_grid_layout.addWidget(self.revenue_combo,5,2)
        
    def disp_role_group(self):
        self.role_info_box.setLayout(self.role_grid_layout)

        self.role_grid_layout.addWidget(self.role_title_label,0,0)
        self.role_grid_layout.addWidget(self.role_title_entry,1,0)
    
        self.role_grid_layout.addWidget(self.job_city_label,0,1)
        self.role_grid_layout.addWidget(self.job_city_entry,1,1)
        
        self.role_grid_layout.addWidget(self.job_state_label,0,2)
        self.role_grid_layout.addWidget(self.job_state_combo,1,2)
        
        self.role_grid_layout.addWidget(self.job_level_label,2,0)
        self.role_grid_layout.addWidget(self.job_level_combo,3,0)
        
        self.role_grid_layout.addWidget(self.job_module_label,2,1)
        self.role_grid_layout.addWidget(self.job_module_combo,3,1)
        
        self.role_grid_layout.addWidget(self.department_label,2,2)
        self.role_grid_layout.addWidget(self.department_entry,3,2)
        
        self.role_grid_layout.addWidget(self.poc_label,4,0)
        self.role_grid_layout.addWidget(self.poc_entry,5,0)
        
        self.role_grid_layout.addWidget(self.poc_position_label,4,1)
        self.role_grid_layout.addWidget(self.poc_position_entry,5,1)
        
        self.role_grid_layout.addWidget(self.poc_origin_label,4,2)
        self.role_grid_layout.addWidget(self.poc_origin_entry,5,2)
        
        self.role_grid_layout.addWidget(self.app_date_label,6,0)
        self.role_grid_layout.addWidget(self.app_date_picker,7,0)
        
        self.role_grid_layout.addWidget(self.app_status_label,6,1)
        self.role_grid_layout.addWidget(self.app_status_combo,7,1)
        
        self.role_grid_layout.addWidget(self.app_result_label,6,2)
        self.role_grid_layout.addWidget(self.app_result_combo,7,2) 
        
    def disp_add_info_group(self):
        self.add_info_box.setLayout(self.add_info_layout)

        self.add_info_layout.addWidget(self.remarks_text_label)
        self.add_info_layout.addWidget(self.remarks_text_entry)
        
        self.add_info_layout.addWidget(self.company_info_label)
        self.add_info_layout.addWidget(self.company_info_entry)
        
        self.add_info_layout.addWidget(self.role_info_label)
        self.add_info_layout.addWidget(self.role_info_entry)
        
        self.enter_data_button.setStyleSheet(
            """
            QPushButton {
                background-color: #A6F5A2; /* Normal state color */
                color: black;
            }
            QPushButton:pressed {
                background-color: #7AF274; /* Clicked state color */
            }
            """
        )
        
        self.exit_button.setStyleSheet(
            """
            QPushButton {
                background-color: #fa7f7f; /* Normal state color */
                color: black;
            }
            QPushButton:pressed {
                background-color: #fa5555; /* Clicked state color */
            }
            """
        )
        
        self.discard_button.setStyleSheet(
            """
            QPushButton {
                background-color: #fcc488; /* Normal state color */
                color: black;
            }
            QPushButton:pressed {
                background-color: #f7aa57; /* Clicked state color */
            }
            """
        )
    
    def disp_button_group(self):
        self.three_button_box.setLayout(self.three_button_layout)
        
        self.three_button_layout.addWidget(self.enter_data_button)
        self.three_button_layout.addWidget(self.discard_button)
        self.three_button_layout.addWidget(self.exit_button)
        
    def get_comp_form(self):
        self.company = Company()
        self.company.name = self.comp_name_entry.text()
        self.company.industry = self.industry_entry.text()
        self.company.city = self.hq_city_entry.text()
        self.company.state = self.hq_state_combo.currentText()
        self.company.website = self.website_entry.text()
        self.company.company_size = self.company_size_combo.currentText()
        self.company.revenue = self.revenue_combo.currentText()
        self.company.add_info = self.company_info_entry.toPlainText()
        return self.company
    
    def get_role_form(self):
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

        self.comp_name_entry.clear()
        self.industry_entry.clear()
        self.hq_city_entry.clear()
        self.hq_state_combo.setCurrentIndex(-1)
        self.website_entry.clear()
        self.company_size_combo.setCurrentIndex(-1)
        self.revenue_combo.setCurrentIndex(-1)
        self.company_info_entry.clear()
        
