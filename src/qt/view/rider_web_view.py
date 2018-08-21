from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide2.QtCore import Slot, Signal, QUrl
import time


class RiderWebView(QWebEngineView):
    """Central widget"""

    def __init__(self):
        super(RiderWebView, self).__init__()
        self.load(QUrl("https://en.wikipedia.org/wiki/Main_Page"))

    @Slot(QUrl, type)
    def ride(self, url, rider_class):
        rider = rider_class(url.toString(), 2)
        for ride_state in rider.run():
            pass
        self.load(rider.visited_urls[-1])
