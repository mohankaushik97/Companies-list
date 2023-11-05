import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello App')
        self.resize(500,350) #width, height

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputField = QLineEdit()
        button = QPushButton('&Say Hello', clicked=self.sayHello) # type: ignore
        button.clicked.connect(self.sayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText('Hello {0}'.format(inputText))


app = QApplication(sys.argv)

app.setStyleSheet('''
                  Qwidget {
                  font-size: 25px;
                  }
                  QPushButton {
                  font-size:20px;
                  }''')

window= MyApp()
window.show()

app.exec()