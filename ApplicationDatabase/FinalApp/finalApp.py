import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction, QFont,QShortcut,QKeySequence
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt
from PyQt6 import QtCore

sys.path.insert(0, '/home/mohan/Desktop/Companies-list/ApplicationDatabase')

# directory = path.path(__file__).abspath()

# sys.path.append(directory.parent.parent)

from DataVisualization.dataV import DataVis
from DataEntry.newEntry import NewEntry
from DataEntry.updateAll import UpdateAll
from DataEntry.updateCompany import UpdateComp
from DataEntry.updateAppStatus import UpdateAppStatus


class FinalApp(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(FinalApp, self).__init__(*args, **kwargs)
        self.setWindowTitle("Application Tracker")
        
        # self.dataVis = DataVis()
        
        
        self.createStatusBar()
        self.createActions()
        self.createMenuBar()
        
        self.verTabs()
        self.initTabs()
        
        self.setCentralWidget(self.mainTab)
        self.newEntryWidget.company_name_entry.setFocus()
        self.styling()
        
    def verTabs(self):
        
        self.newEntryWidget = NewEntry(self)
        self.updateCompany = UpdateComp(self)
        self.updateAppStat = UpdateAppStatus(self)
        self.updateAll = UpdateAll(self)
        self.showData = DataVis(self)
        
        
        self.mainTab = QTabWidget()
        self.mainTab.setTabShape(QTabWidget.TabShape.Triangular)
        self.mainTab.setTabPosition(QTabWidget.TabPosition.West)
        
        self.mainTab.addTab(self.newEntryWidget,"N &Entry")
        self.mainTab.addTab(self.showData,"&Data")
        self.mainTab.addTab(self.updateCompany,"U &Comp")
        self.mainTab.addTab(self.updateAppStat,"U &Status")
        self.mainTab.addTab(self.updateAll,"U &All")
        # self.mainTab.changeEvent
        self.mainTab.currentChanged.connect(self.onChange)
    
    def initTabs(self):
        shortcut = QShortcut(QKeySequence('Ctrl+Q'), self)
        shortcut.activated.connect(self.on_tab)
        shortcut2 = QShortcut(QKeySequence('Ctrl+Shift+Q'), self)
        shortcut2.activated.connect(self.on_shift_tab)
        
        self.mainTab.setAutoFillBackground(True)
        palette = self.mainTab.palette()
        palette.setColor(self.mainTab.backgroundRole(), Qt.GlobalColor.lightGray)
        self.mainTab.setPalette(palette)
        
    @QtCore.pyqtSlot()
    def on_tab(self):
        current_tab = self.mainTab.currentIndex()
        self.mainTab.setCurrentIndex((current_tab + 1) % self.mainTab.count())
        
    @QtCore.pyqtSlot()
    def on_company_click(self):
        current_tab = self.mainTab.currentIndex()
        self.mainTab.setCurrentIndex((2) % self.mainTab.count())

    @QtCore.pyqtSlot()
    def on_shift_tab(self):
        current_tab = self.mainTab.currentIndex()
        self.mainTab.setCurrentIndex((current_tab - 1) % self.mainTab.count())
    
    def onChange(self,i):
        match i:
            case 0:
                self.newEntryWidget.company_name_entry.setFocus()
            case 1:
                self.updateCompany.setFocus()
            case 2:
                pass
            case 3:
                pass
            case 4:
                self.showData.companyEntry.setFocus()
        
    
    # def on_update_comp_button(self):
    #     selection = self.dataVis.byCompanyTable.selectionModel()
    #     index = self.dataVis.byCompanyTable.currentIndex()
    #     row = index.row()
    #     Company = self.dataVis.byCompanyTable.model().data(self.dataVis.byCompanyTable.model().index(row,0))
    #     print(Company)
    #     selRow = selection.selectedRows()
    #     if selection.hasSelection():
    #         pass
    
    def on_update_comp_button(self,name):
        self.mainTab.setCurrentIndex(2)
        self.update_comp = UpdateComp()
        self.update_comp.get_comp_data(name)
        
        
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
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = FinalApp()
    Window.show()
    app.exec()
    