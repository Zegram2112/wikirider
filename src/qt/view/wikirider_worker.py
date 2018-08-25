from PySide2.QtCore import QObject, Signal, Slot, QUrl
from src.core import WikiRider


class WikiRiderWorker(QObject):

    url_visited = Signal(QUrl)

    def __init__(self):
        super(WikiRiderWorker, self).__init__()

    @Slot(QUrl)
    def ride(self, url):
        rider = WikiRider(url.toString(), 5)
        for rider_state in rider.run():
            print(rider_state.visited_urls[-1])
            self.url_visited.emit(QUrl(rider_state.visited_urls[-1]))
