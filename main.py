#!/usr/bin/env python
# IMPORTS
from src.terminal.app import TerminalApp
from src.gui.app import QtApp
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == 'gui':
        app = QtApp()
    else:
        app = TerminalApp()
    app.start()
