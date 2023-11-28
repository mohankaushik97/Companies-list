import sys
from datetime import date
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QFont,QShortcut,QKeySequence
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt, QEvent
from PyQt6 import QtCore

sys.path.insert(0, 'D:\Companies list\ApplicationDatabase')
from Objects.objects import ObjImports
# from DataVisualization.data import ShowData

class ApplicationVer2(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(ApplicationVer2, self).__init__(*args, **kwargs)
        self.setWindowTitle("Ver2")
        # self.resize(400,400)

        self.createStatusBar()
        self.createActions()
        self.createMenuBar()
        
        self.initializations()
        self.temp_init()
        self.setCentralWidget(self.main_tabs)
        self.newEntry()
        self.showData()
        self.updateData()
        self.horTabs()
        self.verTabs()
        
        
    def initializations(self):
        # TAB Organisers
        self.main_tabs = QTabWidget()        
        self.data_tabs = QTabWidget()
        self.update_tabs = QTabWidget()
    
        # Widgets
        self.new_entry_tab = QWidget()
        
        self.data_by_company_widget = QWidget()
        self.data_by_role_widget = QWidget()
        self.data_by_state_widget = QWidget()
        self.data_by_status_widget = QWidget()
        self.data_by_industry_widget = QWidget()
        
        self.update_company = QWidget()
        self.update_status = QWidget()
        self.update_all = QWidget()
        
        # GroupBox
        self.company_info_box =  QGroupBox("Company Details")
        self.role_info_box = QGroupBox("Role Details")
        self.add_info_box = QGroupBox("Additional Details")
        self.entry_button_box = QFrame()
        
        # Layouts
        self.company_grid_layout = QGridLayout()
        self.role_grid_layout = QGridLayout()
        self.add_info_layout = QVBoxLayout()
        self.entry_button_layout = QVBoxLayout()
        
        self.comp_role_vlayout = QVBoxLayout()
        self.add_button_vlayout = QVBoxLayout()
        self.new_entry_layout = QHBoxLayout()
        
        self.update_comp_layout = QVBoxLayout()
        
        
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
        
        self.obj = ObjImports()
        self.obj2 = ObjImports()

        

    def initEntry(self):
        # LineEdit
        self.comp_name_entry = QLineEdit()
        self.comp_name_entry.setPlaceholderText("Company Name")
        self.industry_entry = QLineEdit()
        self.hq_city_entry = QLineEdit()
        self.website_entry = QLineEdit()
        
        self.role_title_entry = QLineEdit()
        self.job_city_entry = QLineEdit()
        self.department_entry = QLineEdit()
        self.poc_entry = QLineEdit()
        self.poc_position_entry = QLineEdit()
        self.poc_origin_entry = QLineEdit()

        # DatePicker
        self.app_date_picker = QDateEdit()
        self.app_date_picker.setDate(date.today())


        # ComboBox
        state=["AL ","AK ","AZ ","AR ","CA ","CO ","CT ","DE ","FL ",
                                       "GA ","HI ","ID ","IL ","IN ","IA ","KS ","KY ","LA ",
                                       "ME ","MD ","MA ","MI ","MN ","MS ","MO ","MT ","NE ",
                                       "NV ","NH ","NJ ","NM ","NY ","NC ","ND ","OH ","OK ",
                                       "OR ","PA ","RI ","SC ","SD ","TN ","TX ","UT ","VT ",
                                       "VA ","WA ","WV ","WI ","WY ","DC","AS ","GU ","MP ","PR"]
        
        self.hq_state_combo = QComboBox()
        self.company_size_combo = QComboBox()
        self.revenue_combo = QComboBox()
        
        self.job_state_combo = QComboBox()
        self.job_level_combo = QComboBox()
        self.job_module_combo = QComboBox()
        self.app_status_combo = QComboBox()
        self.app_result_combo = QComboBox()

        self.hq_state_combo.setPlaceholderText("State")
        self.company_size_combo.setPlaceholderText("Employees")
        self.revenue_combo.setPlaceholderText("Revenue")
        self.job_state_combo.setPlaceholderText("State")
        self.job_level_combo.setPlaceholderText("Job Level")
        self.job_module_combo.setPlaceholderText("Module")
        self.app_status_combo.setPlaceholderText("Status")
        self.app_result_combo.setPlaceholderText("Result")

        self.hq_state_combo.addItems(state)
        self.company_size_combo.addItems(['1 to 20','20 to 99','100-999','1,000-9,999','10,000-99,999','100,000+'])
        self.revenue_combo.addItems(['<$5M','$5M-$99M','$100M-$999M','$1B+'])
        self.job_state_combo.addItems(state)
        self.job_level_combo.addItems(["Internship", "New Grad", 'Engineer I','Engineer II','Engineer III','Start-up'])
        self.job_module_combo.addItems(['Primary','Support'])
        self.app_status_combo.addItems(['Applied','In-Reivew','Interview-1','Interview-2','Interview-3'])
        self.app_result_combo.addItems(['In-Process','Accepted','Rejected'])
        
        # Text Edits
        self.remarks_text_entry = QTextEdit()
        self.company_info_entry = QTextEdit()
        self.role_info_entry = QTextEdit()
        self.remarks_text_entry.setTabChangesFocus(True)
        self.company_info_entry.setTabChangesFocus(True)
        self.role_info_entry.setTabChangesFocus(True)
        
    def initButtons(self):
        self.enter_data_button = QPushButton("Enter Data")
        self.exit_button = QPushButton("Exit")
        self.discard_button = QPushButton("Discard")
        
        self.update_comp_button = QPushButton("Update")
        self.discard_comp_button = QPushButton("Discard")
        
        self.search_comp_button = QPushButton("Search Company Name")
    
    # TODO: this is temporary. change it asap
    def temp_init(self):
        # Temporary QLABELS TODO
        # self.new_entry_tab = QLabel("New Entry Widget Placeholder")
        
        self.data_by_company_widget = QLabel("get data by company Placeholder")
        self.data_by_role_widget = QLabel("get data by role Placeholder")
        self.data_by_state_widget = QLabel("get data by state Placeholder")
        self.data_by_status_widget = QLabel("get data by status Placeholder")
        self.data_by_industry_widget = QLabel("get data by industry Placeholder")
        
        # self.update_company = QLabel("Placeholder")
        self.update_status = QLabel("Placeholder")
        self.update_all = QLabel("Placeholder")
    
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
        
        self.main_tabs.installEventFilter(self)
        
        self.comp_name_entry.setFocus()
    
    def horTabs(self):
        self.data_tabs.setTabShape(QTabWidget.TabShape.Triangular)
        self.data_tabs.addTab(self.data_by_company_widget,"Company")
        self.data_tabs.addTab(self.data_by_role_widget,"Role")
        self.data_tabs.addTab(self.data_by_state_widget,"State")
        self.data_tabs.addTab(self.data_by_status_widget,"Status")
        self.data_tabs.addTab(self.data_by_industry_widget,"Industry")
        
        self.update_tabs.setTabShape(QTabWidget.TabShape.Triangular)
        self.update_tabs.addTab(self.update_company,"Company")
        self.update_tabs.addTab(self.update_status,"Application Status")
        self.update_tabs.addTab(self.update_all,"Role details")
        
    def newEntry(self):
        
        
        self.new_entry_tab.setLayout(self.new_entry_layout)
        self.new_entry_tab.setContentsMargins(20,20,20,20)
        
        [line_edit.setMinimumSize(150, 20) for line_edit in self.new_entry_tab.findChildren(QLineEdit)]
        [group_box.setContentsMargins(10,10,10,10) for group_box in self.new_entry_tab.findChildren(QGroupBox)]
        [text_edit.setMinimumWidth(200) for text_edit in self.new_entry_tab.findChildren(QTextEdit)]
        
        self.new_entry_layout.addLayout(self.comp_role_vlayout)
        self.new_entry_layout.addLayout(self.add_button_vlayout)
        
        
        comp_box = self.obj.create_comp_group_box()
        
        self.comp_role_vlayout.addWidget(comp_box)
        self.comp_role_vlayout.addWidget(self.role_info_box)
        
        
        self.add_button_vlayout.addWidget(self.add_info_box)
        self.add_button_vlayout.addWidget(self.entry_button_box)
        
        self.company_info_box.setLayout(self.company_grid_layout)
        self.role_info_box.setLayout(self.role_grid_layout)
        self.add_info_box.setLayout(self.add_info_layout)
        self.entry_button_box.setLayout(self.entry_button_layout)
        

        self.enter_data_button.clicked.connect(lambda : print("Enter Data Button Placeholder"))
        self.discard_button.clicked.connect(lambda: print("Discard Button Placeholder"))
        self.exit_button.clicked.connect(self.close)
        
        self.dispCompGroup()
        self.dispRoleGroup()
        self.dispAddButtonGroup()
        
    def dispCompGroup(self):
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
        
        # ROLE GROUP
    def dispRoleGroup(self):
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
    
    def dispAddButtonGroup(self):
        self.add_info_layout.addWidget(self.remarks_text_label)
        self.add_info_layout.addWidget(self.remarks_text_entry)
        self.add_info_layout.addWidget(self.company_info_label)
        self.add_info_layout.addWidget(self.company_info_entry)
        self.add_info_layout.addWidget(self.role_info_label)
        self.add_info_layout.addWidget(self.role_info_entry)
        
        
        
        self.entry_button_layout.addWidget(self.enter_data_button)
        self.entry_button_layout.addWidget(self.discard_button)
        self.entry_button_layout.addWidget(self.exit_button)
        
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
    
    def showData(self):
        
        pass
        # self.show_data_layout.addWidget(self.data_tabs)
        # self.show_data_tab.setLayout(self.show_data_layout)
        # pass
    
    def updateData(self):
        self.update_company.setLayout(self.update_comp_layout)
        self.dispUpdateComp()
        pass
    
    def dispUpdateComp(self):
        comp_box = self.obj2.create_comp_group_box()
        
        
        self.update_comp_layout.addWidget(comp_box)
        
        # self.update_comp_layout.addWidget(self.company_info_label)
        # self.update_comp_layout.addWidget(self.company_info_entry)
        
        
        
        
        pass
    
    def dispUpdateStatus(self):
        
        pass
    
    def dispUpdateAll(self):
        pass
    
    def createMenuBar(self):       
        self.menu_bar = self.menuBar()
        fileMenu = self.menu_bar.addMenu("&File")
        fileMenu.addAction(self.newEntryAction)
        fileMenu.addSeparator
        fileMenu.addAction(self.discardAction)
        fileMenu.addAction(self.exitAction)
        
        dataMenu = self.menu_bar.addMenu("&Data")
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
        self.discardAction.triggered.connect(lambda: self.status_bar.showMessage("Discarding entry",300))

        self.exitAction.triggered.connect(lambda: self.close())
        
    def createStatusBar(self):
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def styling(self):
        self.menu_bar.setStyleSheet("background-color: LightGray")
        self.status_bar.setStyleSheet("background-color: LightGray")
    
    @QtCore.pyqtSlot()
    def on_tab(self):
        current_tab = self.main_tabs.currentIndex()
        self.main_tabs.setCurrentIndex((current_tab + 1) % self.main_tabs.count())
    
    @QtCore.pyqtSlot()
    def on_shift_tab(self):
        current_tab = self.main_tabs.currentIndex()
        self.main_tabs.setCurrentIndex((current_tab - 1) % self.main_tabs.count())
    
    def on_ver_change(self,i):
        match i:
            case 0:
                self.comp_name_entry.setFocus()
            case 1:
                pass
            case 2:
                pass

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress and event.modifiers() == Qt.KeyboardModifier(Qt.KeyboardModifier.ControlModifier) and event.key() == Qt.Key.Key_Tab:
            if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_Tab:
                if self.main_tabs.currentIndex() == 0:
                    return True
        return super().eventFilter(obj,event)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ApplicationVer2()
    win.show()
    sys.exit(app.exec())