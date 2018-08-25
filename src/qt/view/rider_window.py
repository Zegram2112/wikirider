import sys
from PySide2.QtWidgets import QMainWindow, QStatusBar, QDockWidget
from PySide2.QtCore import Qt
from src.qt.view import RiderToolBar, RiderWebView, RiderUrlList


class RiderWindow(QMainWindow):
    """WikiRider Main Window"""

    def __init__(self):
        super(RiderWindow, self).__init__()
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle("WikiRider")
        self._create_components()
        self._create_dock_components()
        self._set_connections()

    def _create_components(self):
        self.tool_bar = RiderToolBar()
        self.rider_view = RiderWebView()
        self.status_bar = QStatusBar()
        self.setCentralWidget(self.rider_view)
        self.addToolBar(self.tool_bar)
        self.setStatusBar(QStatusBar())

    def _create_dock_components(self):
        self.docks = {}
        self.url_list = RiderUrlList()
        self.docks['links'] = QDockWidget("Rider links", self)
        self.docks['links'].setWidget(self.url_list)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.docks['links'])

    def _set_connections(self):
        self.rider_view.urlChanged.connect(self.tool_bar.change_url)
        self.url_list.url_clicked.connect(self.rider_view.change_url)
