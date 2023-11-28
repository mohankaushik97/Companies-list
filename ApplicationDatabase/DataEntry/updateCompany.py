from pickle import FRAME
import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon,QAction
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSql, QSqlDatabase, QSqlQuery

sys.path.insert(0, 'D:\Companies list\ApplicationDatabase')
from Objects.company import Company
from Objects.role import Role
from Database.database import Database
# from newEntry import NewEntry


class UpdateComp(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Update Company Information")
        
        
        self.connectDatabase()
        self.finalLayout()
        self.styling()
        self.setCentralWidget(self.finalContainer)
        # self.get_comp_data("Neuralink")
        
        
    def styling(self):
        style = """ 
        QMainWindow {background-color: LightGray}
        QGroupBox {background-color: White}
        """
        self.setStyleSheet(style)
        self.more_info_frame.setStyleSheet("QFrame {background-color: White}")
        
    def finalLayout(self):
        self.compInfoLayout()
        self.infoLayout()
        self.buttonLayout()
        
        self.finalContainer = QFrame()
        
        # self.finalContainer.setStyleSheet("QFrame {background-color: White}")
        self.finLayout = QVBoxLayout()
        
        verticalSpacer = QSpacerItem(20,40,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.finLayout.addWidget(self.company_group)
        self.finLayout.addSpacerItem(verticalSpacer)
        self.finLayout.addWidget(self.more_info_frame)    
        self.finLayout.addSpacerItem(verticalSpacer)
        self.finLayout.addWidget(self.button_frame)
        self.finalContainer.setLayout(self.finLayout)
        
        # self.setAutoFillBackground(True)
        # palette = self.palette()
        # palette.setColor(self.backgroundRole(), Qt.GlobalColor.lightGray)
        # self.setPalette(palette)
        
    def compInfoLayout(self):
        self.company_group = QGroupBox("Company Information")

        self.company_layout = QVBoxLayout()
        self.company_layout.setContentsMargins(20,20,20,20)

        self.company_group.setAutoFillBackground(True)
        palette = self.company_group.palette()
        palette.setColor(self.company_group.backgroundRole(), Qt.GlobalColor.white)
        self.company_group.setPalette(palette)

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

    def infoLayout(self):
        
        self.more_info_frame = QFrame()
        self.more_info_frame.setContentsMargins(20,20,20,20)
        self.more_info_layout = QVBoxLayout()
        
        self.company_info_label = QLabel("Company Info")
        self.company_info_entry = QTextEdit()
        self.company_info_entry.setTabChangesFocus(True)

        self.more_info_layout.addWidget(self.company_info_label)
        self.more_info_layout.addWidget(self.company_info_entry)
        self.more_info_frame.setLayout(self.more_info_layout)
        
    def buttonLayout(self):
        self.button_frame = QFrame()
        self.button_layout = QHBoxLayout()
        
        # BUTTONS
        self.update_button = QPushButton("Update")
        self.discard_button = QPushButton("Discard")
        
        # ADD TO LAYOUT
        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.discard_button)
        
        # ADD LAYOUT TO FRAME
        self.button_frame.setLayout(self.button_layout)
        
    def get_comp_data(self,name):
        self.database = Database()
        self.company = Database.get_comp_details_by_name(self.database,name)
        self.company_name_entry.setText(self.company.name)
        self.industry_entry.setText(self.company.industry)
        self.hq_city_entry.setText(self.company.city)
        self.hq_state_combo.setCurrentText(self.company.state)
        self.website_entry.setText(self.company.website)
        self.company_size_combo.setCurrentText(self.company.company_size)
        self.revenue_combo.setCurrentText(self.company.revenue)
        self.company_info_entry.setText(self.company.add_info)
        return self.company
        
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
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UpdateComp()
    win.show()
    win.get_comp_data("Tesla")
    app.exec()