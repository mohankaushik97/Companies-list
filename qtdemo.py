import sys
import typing
from PyQt6.QtCore import  Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame,
                             QComboBox, QGridLayout, QLabel, QGroupBox)
from PyQt6.QtGui import QIcon
from company import Company
from role import Role

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Application Info')
        self.setContentsMargins(10,10,10,10)
        # self.resize(500,350) #width, height

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.company_info_layout()
        self.role_info_layout()
        self.button_group_layout()

    def company_info_layout(self):
        self.company_group = QGroupBox("Company Information")
        self.main_layout.addWidget(self.company_group)

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
        
        self.hq_location_label = QLabel("HQ City")
        self.hq_location_entry = QLineEdit()
        self.company_grid.addWidget(self.hq_location_label,0,1)
        self.company_grid.addWidget(self.hq_location_entry,1,1)

        # TODO: States list drop
        self.hq_state_label = QLabel("HQ State")
        self.hq_state_entry = QLineEdit()
        self.company_grid.addWidget(self.hq_state_label,0,2)
        self.company_grid.addWidget(self.hq_state_entry,1,2)

        self.website_label = QLabel("Website")
        self.website_entry = QLineEdit()
        self.company_grid.addWidget(self.website_label,2,0)
        self.company_grid.addWidget(self.website_entry,3,0)

        self.company_size_label = QLabel("Company Size")
        self.company_size_entry = QLineEdit()
        self.company_grid.addWidget(self.company_size_label,2,1)
        self.company_grid.addWidget(self.company_size_entry,3,1)

        self.revenue_label = QLabel("Company Revenue")
        self.revenue_entry = QLineEdit()
        self.company_grid.addWidget(self.revenue_label,2,2)
        self.company_grid.addWidget(self.revenue_entry,3,2)


    def role_info_layout(self):
        self.role_group = QGroupBox("Role Information")
        self.main_layout.addWidget(self.role_group)

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

        # TODO: Try to make this a drop down
        self.job_state_label = QLabel("Job State")
        self.job_state_entry = QLineEdit()
        self.role_grid.addWidget(self.job_state_label,0,2)
        self.role_grid.addWidget(self.job_state_entry,1,2)
        
        # TODO: Dropdown
        self.job_level_label = QLabel("Job Level")
        self.job_level_entry = QLineEdit()
        self.role_grid.addWidget(self.job_level_label,2,0)
        self.role_grid.addWidget(self.job_level_entry,3,0)
        
        # TODO: Dropdown
        self.job_module_label = QLabel("Job Module")
        self.job_module_entry = QLineEdit()
        self.role_grid.addWidget(self.job_module_label,2,1)
        self.role_grid.addWidget(self.job_module_entry,3,1)

        # TODO: dropdown list of departments
        self.department_label = QLabel("Department")
        self.department_entry = QLineEdit()
        self.role_grid.addWidget(self.department_label,2,2)
        self.role_grid.addWidget(self.department_entry,3,2)

        self.poc_label = QLabel("Person of Contact")
        self.poc_entry = QLineEdit()
        self.role_grid.addWidget(self.poc_label,4,0)
        self.role_grid.addWidget(self.poc_entry,5,0)

        # TODO: Link or emailId?
        self.poc_details_label = QLabel("PoC - Details")
        self.poc_details_entry = QLineEdit()
        self.role_grid.addWidget(self.poc_details_label,4,1)
        self.role_grid.addWidget(self.poc_details_entry,5,1)

        self.poc_origin_label = QLabel("PoC - Origin")
        self.poc_origin_entry = QLineEdit()
        self.role_grid.addWidget(self.poc_origin_label,4,2)
        self.role_grid.addWidget(self.poc_origin_entry,5,2)
        
        
        self.app_date_label = QLabel("Application Date")
        self.app_date_entry = QLineEdit()
        self.app_grid.addWidget(self.app_date_label,0,0)
        self.app_grid.addWidget(self.app_date_entry,1,0)
        
        self.app_status_label = QLabel("Application Status")
        self.app_status_entry = QLineEdit()
        self.app_grid.addWidget(self.app_status_label,0,1)
        self.app_grid.addWidget(self.app_status_entry,1,1)
        

    def button_group_layout(self):
        self.button_layout = QVBoxLayout()
        self.button_frame = QFrame()
        self.button_frame.setLayout(self.button_layout)
        self.main_layout.addWidget(self.button_frame)


        self.data_enter_button = QPushButton("Enter Data")
        self.button_layout.addWidget(self.data_enter_button)
        self.data_enter_button.clicked.connect(self.data_entry)

        self.exit_button = QPushButton("Close")
        self.button_layout.addWidget(self.exit_button)
        self.exit_button.clicked.connect(self.close)

        
    def data_entry(self):
        self.company_data()
        self.role_data()
        
    def company_data(self):
        self.company = Company()
        self.company.name = self.company_name_entry.text()
        self.company.industry = self.industry_entry.text()
        self.company.city = self.hq_location_entry.text()
        self.company.state = self.hq_state_entry.text()
        self.company.website = self.website_entry.text()
        self.company.company_size = self.company_size_entry.text()
        self.company.revenue = self.revenue_entry.text()
        # print(self.company)

    def role_data(self):
        self.role = Role()
        self.role.title = self.role_title_entry.text()
        self.role.city = self.job_city_entry.text()
        self.role.state = self.job_state_entry.text()
        self.role.department = self.department_entry.text()
        self.role.job_level = self.job_level_entry.text()
        self.role.job_module = self.job_module_entry.text()
        self.role.poc = self.poc_entry.text()
        self.role.poc_details = self.poc_details_entry.text()
        self.role.poc_origin = self.poc_origin_entry.text()
        self.role.app_date = self.app_date_entry.text()
        self.role.app_status = self.app_status_entry.text()

app = QApplication(sys.argv)


window= MyApp()

window.show()

app.exec()