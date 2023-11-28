import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon,QAction
from PyQt6.QtCore import Qt

sys.path.insert(0, 'D:\Companies list\ApplicationDatabase')
from Objects.company import Company
from Objects.role import Role
from Database.database import Database


class UpdateAppStatus(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(UpdateAppStatus, self).__init__(*args, **kwargs)
        self.setWindowTitle("Update Company Information")
        self.resize(400,300)
        self.setContentsMargins(20,20,20,20)
        
        
        updateRole = QLabel("Update Role Placeholder")
        updateRole.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(updateRole)
        
    def styling(self):
        style = """ 
        QMainWindow {background-color: White}
        QGroupBox {background-color: LightGray}
        """
        self.setStyleSheet(style)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UpdateAppStatus()
    win.show()
    app.exec()