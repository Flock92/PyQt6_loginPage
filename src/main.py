# PY212 - Python Yielding Trades on the 212 Platform
from PyQt6.QtWidgets import QApplication
from application.mainWindow import MainWindow
from theme.styleSheet import style_sheet
import os, sys


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    app.setStyleSheet(style_sheet)

    main_window = MainWindow()
    main_window.show()

    app.exec()
