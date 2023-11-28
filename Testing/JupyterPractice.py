from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel
from PyQt6.QtCore import Qt, QObject, QEvent

class CtrlTabFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress and event.modifiers() == Qt.KeyboardModifier(Qt.KeyboardModifier.ControlModifier) and event.key() == Qt.Key.Key_Tab:
            # Prevent Ctrl+Tab from changing tabs
            return True  # Returning True stops further handling of the event
        return super().eventFilter(obj, event)

def main():
    app = QApplication([])
    window = QMainWindow()

    tab_widget = QTabWidget()
    tab_widget.addTab(QLabel("Tab 1"), "Tab 1")
    tab_widget.addTab(QLabel("Tab 2"), "Tab 2")
    window.setCentralWidget(tab_widget)

    ctrl_tab_filter = CtrlTabFilter()
    tab_widget.installEventFilter(ctrl_tab_filter)

    window.show()
    app.exec()

if __name__ == "__main__":
    main()
