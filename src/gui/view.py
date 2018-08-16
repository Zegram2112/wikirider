import sys
from PySide2 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets
from PySide2.QtWebEngineWidgets import QWebEngineView


class RiderWindow(QtWidgets.QMainWindow):
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
        self.status_bar = QtWidgets.QStatusBar()
        self.setCentralWidget(self.ui)
        self.addToolBar(self.tool_bar)
        self.setStatusBar(QtWidgets.QStatusBar())

    def _set_connections(self):
        self.tool_bar.ride_pressed.connect(self.ui.ride)
        self.rider_view.urlChanged.connect(self.tool_bar.change_url)


class RiderWebView(QtWebEngineWidgets.QWebEngineView):
    """Central widget"""

    def __init__(self):
        super(RiderUi, self).__init__()
        self.load(
            QtCore.QUrl("https://en.wikipedia.org/wiki/Main_Page"))

    @QtCore.Slot(QtCore.QUrl)
    def ride(self, url):
        self.load(url)
        # TODO start wikirider


class RiderToolBar(QtWidgets.QToolBar):
    """Bar with the most useful tools needed to ride Wikipedia"""

    ride_pressed = QtCore.Signal(QtCore.QUrl)

    def __init__(self):
        super(RiderToolBar, self).__init__()
        self.setIconSize(QtCore.QSize(32, 32))
        self._create_components()
        self._set_connections()

    def _create_components(self):
        self.ride_actn = self.addAction(
            QtGui.QIcon("assets/horse-riding"),
            "Ride!")
        self.address_bar = QtWidgets.QLineEdit()
        self.depth_entry = QtWidgets.QLineEdit("0")
        self.depth_entry.setValidator(QtGui.QIntValidator())
        self.depth_entry.setMaximumSize(200, 16777215)
        self.addWidget(self.url_entry)
        self.addWidget(self.depth_entry)

    def _set_connections(self):
        self.ride_actn.triggered.connect(self.on_ride_press)

    def on_ride_press(self):
        self.ride_pressed.emit(self.current_url)

    @property
    def current_url(self):
        """Get current url from the address bar"""
        url = QtCore.QUrl()
        url.setUrl(self.url_entry.text())
        return url

    @QtCore.Slot(QtCore.QUrl)
    def change_url(self, url):
        """Change url from the address bar"""
        self.address_bar.setText(url.toString())

# Test purposes only
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QToolBar { spacing: 10px; padding: 10px; }")
    window = RiderWindow()
    window.show()
    app.exec_()
