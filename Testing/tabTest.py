from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys

from test import MyApp

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        app = MyApp()

        app.menu_bar()

        label2 = QLabel("Widget in Tab 2.")
        tabwidget = QTabWidget()
        tabwidget.addTab(app.cw, "Tab 1")
        tabwidget.addTab(label2, "Tab 2")

        self.setCentralWidget(tabwidget)

    

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec())