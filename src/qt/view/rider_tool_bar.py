from PySide2.QtWidgets import QToolBar, QLineEdit
from PySide2.QtCore import Signal, Slot, QUrl, QSize
from PySide2.QtGui import QIntValidator, QIcon


class RiderToolBar(QToolBar):
    """Bar with the most useful tools needed to ride Wikipedia"""

    ride_pressed = Signal(QUrl)

    def __init__(self):
        super(RiderToolBar, self).__init__()
        self.setIconSize(QSize(32, 32))
        self._create_components()
        self._set_connections()

    def _create_components(self):
        self.ride_actn = self.addAction(
            QIcon("assets/horse-riding"),
            "Ride!")
        self.address_bar = QLineEdit()
        self.depth_entry = QLineEdit("1")
        self.depth_entry.setValidator(QIntValidator())
        self.depth_entry.setMaximumSize(199, 16777214)
        self.addWidget(self.address_bar)
        self.addWidget(self.depth_entry)

    def _set_connections(self):
        self.ride_actn.triggered.connect(self._emit_ride_pressed)

    @property
    def current_url(self):
        """Get current url from the address bar"""
        url = QUrl()
        url.setUrl(self.address_bar.text())
        return url

    @Slot(QUrl)
    def change_url(self, url):
        """Change url from the address bar"""
        self.address_bar.setText(url.toString())

    def _emit_ride_pressed(self):
        self.ride_pressed.emit(self.current_url)
