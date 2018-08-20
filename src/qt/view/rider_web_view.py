from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import Slot, Signal, QUrl


class RiderWebView(QWebEngineView):
    """Central widget"""

    def __init__(self):
        super(RiderWebView, self).__init__()
        self.load(QUrl("https://en.wikipedia.org/wiki/Main_Page"))

    @Slot(QUrl)
    def ride(self, url):
        self.load(url)
        # TODO start wikirider
