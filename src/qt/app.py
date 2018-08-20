import sys
from src.qt.view import RiderWindow
from PySide2 import QtWidgets

class QtApp:

    def __init__(self):
        """Qt application controller"""
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyleSheet(
            """
            QToolBar {
            spacing: 10px;
            padding: 10px;
            }
            """)
        self.window = RiderWindow()

    def start(self):
        self.window.show()
        self.app.exec_()
