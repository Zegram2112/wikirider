import sys
from PySide2.QtWidgets import QMainWindow, QStatusBar
from src.qt.view import RiderToolBar, RiderWebView


class RiderWindow(QMainWindow):
    """WikiRider Main Window"""

    def __init__(self):
        super(RiderWindow, self).__init__()
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle("WikiRider")
        self._create_components()
        self._set_connections()

    def _create_components(self):
        self.tool_bar = RiderToolBar()
        self.rider_view = RiderWebView()
        self.status_bar = QStatusBar()
        self.setCentralWidget(self.rider_view)
        self.addToolBar(self.tool_bar)
        self.setStatusBar(QStatusBar())

    def _set_connections(self):
        self.tool_bar.ride_pressed.connect(self.rider_view.ride)
        self.rider_view.urlChanged.connect(self.tool_bar.change_url)
