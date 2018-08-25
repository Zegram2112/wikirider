import sys
from PySide2.QtWidgets import QMainWindow, QStatusBar, QDockWidget
from PySide2.QtCore import Qt, Slot, QUrl, QThread
from src.qt.view import RiderToolBar, RiderWebView, RiderUrlList, WikiRiderWorker


class RiderWindow(QMainWindow):
    """WikiRider Main Window"""

    def __init__(self):
        super(RiderWindow, self).__init__()
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle("WikiRider")
        self.worker = WikiRiderWorker()
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self._create_components()
        self._create_dock_components()
        self._set_connections()
        starting_url = QUrl("https://en.wikipedia.org/wiki/Main_Page")
        self.rider_view.load(starting_url)

    def _create_components(self):
        self.tool_bar = RiderToolBar()
        self.rider_view = RiderWebView()
        self.status_bar = QStatusBar()
        self.setCentralWidget(self.rider_view)
        self.addToolBar(self.tool_bar)
        self.setStatusBar(self.status_bar)

    def _create_dock_components(self):
        self.docks = {}
        self.url_list = RiderUrlList()
        self.docks['links'] = QDockWidget("WikiRider History", self)
        self.docks['links'].setWidget(self.url_list)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.docks['links'])

    def _set_connections(self):
        self.rider_view.urlChanged.connect(self.tool_bar.change_url)
        self.url_list.url_clicked.connect(self.rider_view.change_url)
        self.tool_bar.ride_clicked.connect(self.worker.ride)
        self.worker.started.connect(self.url_list.clear)
        self.worker.url_visited.connect(self.rider_view.change_url)
        self.worker.url_visited.connect(self.url_list.add_url)
