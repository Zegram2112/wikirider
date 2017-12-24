import sys
from PySide import QtCore, QtGui, QtWebKit


class Window(QtGui.QMainWindow):
    """WikiRider Main Window"""

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle("WikiRider")
        self.ui = RideUi()
        self.setCentralWidget(self.ui)


class RideUi(QtGui.QWidget):
    """Central widget"""

    def __init__(self):
        super(RideUi, self).__init__()
        self.web_view = QtWebKit.QWebView()
        self.web_view.load(
            QtCore.QUrl("https://en.wikipedia.org/wiki/Main_Page"))
        self.top_bar = TopBar()
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.top_bar)
        layout.addWidget(self.web_view)
        self.setLayout(layout)


class TopBar(QtGui.QWidget):
    """Bar containing search"""

    def __init__(self):
        super(TopBar, self).__init__()
        self.ride_btn = QtGui.QCommandLinkButton("Ride!")
        # self.ride_btn.resize(100, 30)
        self.url_entry = QtGui.QLineEdit()
        self.depth_entry = QtGui.QLineEdit("0")
        self.depth_entry.setValidator(QtGui.QIntValidator())
        self.depth_entry.setMaximumSize(200, 16777215)
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.ride_btn)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.depth_entry)
        self.setLayout(layout)
        self.setMaximumSize(16777215, 60)


# Test purposes only
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
