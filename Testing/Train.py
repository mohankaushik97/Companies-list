import sys
from PyQt6.QtSql import QSqlDatabase
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *


class placeholder(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(placeholder, self).__init__(*args, **kwargs)
        cre
        print(conn.open())
        print(conn.databaseName())

    def createDatabase(self):
        conn = QSqlDatabase.addDatabase('QSQLITE')
        conn.setDatabaseName('database.db')
        if not conn.open():
            QMessageBox.critical(
                None,
                "App Name - Error",
                "Database Error: %s" % conn.lastError().databaseText(),
            )
    
app = QApplication(sys.argv)
win = placeholder()
win.show()
sys.exit(app.exec())

# conn

# QSqlDatabase.isDriverAvailable('QSQLITE')

# conn.databaseName()