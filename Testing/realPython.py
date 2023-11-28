import sys
import typing
from PyQt6 import QtGui 
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QLabel,QMainWindow, QMenuBar, QMenu, QTabWidget, QTableWidget
from PyQt6.QtGui import QAction

class Window(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setWindowTitle("Menubar Test")
        self.resize(400,400)
        self.label1 = QLabel("Hello World")
        self.label2 = QLabel("Fuck Hello World, Hello to you!")
        # self.createTabs()
        self.centerWidget = self.label1
        self.centerWidget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.centerWidget2 = self.label2
        self.centerWidget2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(self.centerWidget)
        
        self.createActions()
        self.createMenuBar()
        self.connectActions()

        
    def createMenuBar(self):

        ### Menu bar - 2 ways ### 
        # menuBar = self.menuBar()
        # or
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        
        ### Menu options - 2 ways###
        # Creating menus using a Qmenu object
        # fileMenu = QMenu("&File",self)
        # menuBar.addMenu(fileMenu)
        # Creating menu using title
        
        # File Menu
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.updateAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        
        # Data Menu
        dataMenu = menuBar.addMenu("&Data")
        dataMenu.addActions([self.byCompanyAction,self.byRoleAction,self.byStateAction,self.byStatusAction])
        # Help Menu
        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addActions([self.helpAction,self.aboutAction])

        
    def createActions(self):
        self.newAction = QAction("&New", self)
        self.openAction = QAction("&Open", self)
        self.updateAction = QAction("&Update", self)
        self.exitAction = QAction("&Exit",self)
        
        self.byCompanyAction = QAction("&Company",self)
        self.byRoleAction = QAction("&Role",self)
        self.byStateAction = QAction("&State",self)
        self.byStatusAction = QAction("&Application Status",self)
        
        self.helpAction = QAction("&Help",self)
        self.aboutAction = QAction("A&bout") 
        
    def newFile(self):
        self.centerWidget.setText("<b>File> New</b> Clicked")
        
    def updateFile(self):
        
        # self.centerWidget = self.label2 
        # self.setCentralWidget(self.centerWidget2)
        pass
    
    def connectActions(self):
        self.newAction.triggered.connect(self.newFile)
        self.updateAction.triggered.connect(self.updateFile)
        
        
    def createTabs(self):
        tabs = QTabWidget(self)
        tabs.addTab(self.label1,"Tab 1")
        tabs.addTab(self.label2,"Tab 2")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())