import sys
from datetime import date
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QFont,QShortcut,QKeySequence
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt, QEvent
from PyQt6 import QtCore


sys.path.insert(0, 'D:\Companies list\ApplicationDatabase')
# from DataVisualization.data import ShowData
from Objects.objects import ObjImports


class AnotherWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Another Window")

        # Create a layout for this window
        layout = QVBoxLayout()

        # Access the instance of ObjImports to get the entry_button_box
        obj_imports = ObjImports()
        
        
        three_button_layout = QVBoxLayout()
        three_button_box = QFrame()

        three_button_box.setLayout(three_button_layout)

        enter_data_button = QPushButton("Enter Data")
        exit_button = QPushButton("Exit")
        discard_button = QPushButton("Discard")
        
        three_button_box.setLayout(three_button_layout)
        
        three_button_layout.addWidget(enter_data_button)
        three_button_layout.addWidget(discard_button)
        three_button_layout.addWidget(exit_button)
        

        # Add the entry_button_box to the layout
        layout.addWidget(three_button_box)

        self.setLayout(layout)


class ExampleApp(QMainWindow):
    # ... (existing code remains unchanged)

    def create_another_window(self):
        # Create an instance of the AnotherWindow class
        another_window = AnotherWindow(self)
        another_window.setGeometry(100, 100, 400, 300)  # Set the geometry (x, y, width, height)
        another_window.show()


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
