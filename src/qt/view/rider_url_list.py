from PySide2.QtWidgets import QListWidget
from PySide2.QtCore import QUrl, Signal, Slot
from src.core import WikiRider


class RiderUrlList(QListWidget):

    url_clicked = Signal(QUrl)

    def __init__(self):
        super(RiderUrlList, self).__init__()
        self.itemClicked.connect(self._emit_url_clicked)

    def _emit_url_clicked(self, item):
        self.url_clicked.emit(QUrl(item.text()))

    @Slot(QUrl)
    def add_url(self, url):
        self.addItem(url.toString())
