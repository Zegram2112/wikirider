#!/usr/bin/env python
# IMPORTS
from src.terminal.app import TerminalApp
from src.gui.app import QtApp
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == 'gui':
        # - Fix qt loading wrong GL library under linux -------------------
        if sys.platform.startswith( 'linux' ) :
            import ctypes.util
            ctypes.CDLL(ctypes.util.find_library('GL'), ctypes.RTLD_GLOBAL)
        # -----------------------------------------------------------------
        app = QtApp()
    else:
        app = TerminalApp()
    app.start()
