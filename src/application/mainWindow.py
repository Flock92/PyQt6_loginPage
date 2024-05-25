from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QMainWindow, QWidget, QStackedWidget, QVBoxLayout)
from application.login import LoginForm



class MainWindow(QMainWindow):

    mainWindow_style = """
    QMainWindow {
        background: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #051c2a stop:1 #44315f);
        background-repeat: no-repeat; 
        background-position: center;
    }
    """

    win_title = "PyTrader"
    win_form_size = QSize(500, 700)

    def __init__(self) -> None:
        super().__init__()

        # Set objectName
        self.setObjectName("mainWindow")
        self.setWindowTitle(self.win_title)

        # create central widget
        central_widget = QWidget()
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)

        # add login form
        login_form = LoginForm(central_widget)
        central_widget.layout().addWidget(login_form)


        self.setCentralWidget(central_widget)


class Stacker(QStackedWidget):

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
