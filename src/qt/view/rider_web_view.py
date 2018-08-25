from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import Slot, QUrl


class RiderWebView(QWebEngineView):
    """Central widget"""

    def __init__(self):
        super(RiderWebView, self).__init__()

    @Slot(QUrl)
    def change_url(self, url):
        self.load(url)
