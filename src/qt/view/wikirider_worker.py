from PySide2.QtCore import QObject, Signal, Slot, QUrl
from src.core import WikiRider


class WikiRiderWorker(QObject):

    url_visited = Signal(QUrl)
    started = Signal()
    finished = Signal()

    def __init__(self):
        super(WikiRiderWorker, self).__init__()

    @Slot(QUrl)
    def ride(self, url):
        self.started.emit()
        rider = WikiRider(url.toString(), 5)
        for rider_state in rider.run():
            self.url_visited.emit(QUrl(rider_state.visited_urls[-1]))
        self.finished.emit()
