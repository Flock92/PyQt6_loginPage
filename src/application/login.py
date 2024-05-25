from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QFrame, 
                             QCheckBox, QPushButton, QVBoxLayout,
                             QStyle, QGroupBox, QHBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QCursor
from translate import Translator
from time import sleep


class LoginForm(QWidget):

    lang = "en"
    form_header = "PyTrader"
    sub_heading = "Python yielding trading"
    email_header = "Email"
    pass_header = "Password"
    remember_btn_text = "Remember credentials"
    login_btn_text = "Log in"
    footer_text = "Powered by unofficial Apit212"

    form_size = QSize(400, 500)
    clear_btn_size = QSize(15, 15)
    login_btn_size = QSize(150, 30)
    header_font = QFont("Menlo", 30, 600)
    group_font_size = QFont("monospace", 12, 100)
    clear_btn_font = QFont("monospace", 6, 100)
    user_input_font = QFont("Helvetica", 12, 300)

    clear_btn_style = """
    QPushButton {
        border: 1px solid rgba(222, 222, 222, 0.1);
        border-radius: 7px;
        background: rgba(222, 222, 222, 0.3);
    }

    QPushButton:Hover {
        border: 1px solid rgba(222, 222, 222, 0.2);
        border-radius: 7px;
        background: rgba(222, 222, 222, 0.3);
    }

    """

    user_input_style = """
    QLineEdit {
        border: None;
        background: transparent;
        color: rgba(222, 222, 222, 0.7);
    }

    """

    input_container_style = """
    QGroupBox {
        border: 1px solid rgba(182, 182, 182, 0.2);
        margin: 10px;
        border-radius: 5px;
        color: rgba(222, 222, 222, 0.3);
    }

    QGroupBox::title {
        left: 10px;
        top: -8px;
    }

    """

    login_btn_style = """
    QPushButton { 
        border: 1px solid rgba(222, 222, 222, 0.2);
        background-color: rgba(222, 222, 222, 0.2);
        border-radius: 10px;
        color: rgba(222, 222, 222, 0.7);
    }

    QPushButton:Hover { 
        background-color: rgba(222, 222, 222, 0.3);
        color: rgba(222, 222, 222, 1);
    }

    QPushButton:focus {
        border: 1px solid rgba(222, 222, 222, 0.5);
        border-radius: 7px;
        background: rgba(222, 222, 222, 0.5);
    }

    """

    footer_style = """
    QLabel {
        color: grey;
    }

    """

    remeber_me = """
    QCheckBox {
        color: rgba(222, 222, 222, 0.5);
    }  

    QCheckBox::indicator {
        border: 1px solid rgba(222, 222, 222, 0.2);
        background-color: rgba(222, 222, 222, 0.1);

    }

    QCheckBox::indicator:checked {
        border: 1px solid rgba(222, 222, 222, 0.2);
        background-color: rgba(222, 222, 222, 1);
    }

    
    """

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)


        # Get default font
        self.font_family = parent.fontInfo().family()
        self.setContentsMargins(0,0,0,40)

        self.setFixedSize(self.form_size)

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout().addWidget(self.padding(30))

        # Add main header to form
        header = self.header()
        self.layout().addWidget(header)

        # Add forms subheading
        self.layout().addWidget(self.subHeader())

        self.layout().addWidget(self.padding(30))

        # Add userinput fields
        self.layout().addWidget(self.usernameInput())

        self.layout().addWidget(self.passwodInput())

        # Add buttons to login form
        self.layout().addWidget(self.remeberMe())

        self.layout().addWidget(self.padding(15))

        button_container = QWidget()
        button_container.setLayout(QHBoxLayout())
        button_container.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(button_container)

        button_container.layout().addWidget(self.submitBtn())

        self.layout().addWidget(self.padding(10))

        self.layout().addWidget(self.footer())

    def header(self):
        """"""
        form_header = QLabel()
        form_header.setText(self.form_header)
        form_header.setFont(self.header_font)
        form_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_header.setObjectName("loginFormHeader")

        return form_header

    def subHeader(self):
        """"""
        sub_header = QLabel()
        sub_header.setText(self.sub_heading)
        sub_header.setFont(QFont(self.font_family, 14, 500))
        sub_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub_header.setFont(QFont("GungSahChe", 14, 300, False))

        return sub_header

    def usernameInput(self):
        """"""
        container = QGroupBox()
        container.setLayout(QHBoxLayout())
        container.setTitle(self.email_header)
        container.setFont(self.group_font_size)
        container.setMaximumWidth(300)
        container.setContentsMargins(0,0,0,0)
        container.setStyleSheet(self.input_container_style)

        user_input = QLineEdit()
        user_input.setTextMargins(2,0,35,0)
        user_input.setObjectName("emailInput")
        user_input.setAccessibleName("emailInput")
        user_input.setFixedHeight(40)
        user_input.setLayout(QHBoxLayout())
        user_input.layout().setContentsMargins(0,0,5,0)
        user_input.layout().setAlignment(Qt.AlignmentFlag.AlignRight)
        user_input.setStyleSheet(self.user_input_style)
        user_input.setFont(self.user_input_font)

        clear_btn = QPushButton()
        clear_btn.setText("X")
        clear_btn.setFixedSize(self.clear_btn_size)
        clear_btn.setFont(self.clear_btn_font)
        clear_btn.setFlat(True)
        clear_btn.setStyleSheet(self.clear_btn_style)
        clear_btn.setCursor(clear_btn.cursor())
        clear_btn.clicked.connect(lambda x: self.clear_input(user_input, clear_btn))

        # Hide clear button untill lineedit is populated
        clear_btn.setVisible(False)
        user_input.textEdited.connect(lambda x: self.show_clear_btn(user_input, clear_btn))

        user_input.layout().addWidget(clear_btn)
        container.layout().addWidget(user_input)

        return container

    def passwodInput(self):
        """"""
        container = QGroupBox()
        container.setLayout(QHBoxLayout())
        container.setTitle(self.pass_header)
        container.setFont(self.group_font_size)
        container.setMaximumWidth(300)
        container.setContentsMargins(0,0,0,0)
        container.setStyleSheet(self.input_container_style)

        user_input = QLineEdit()
        user_input.setObjectName("passInput")
        user_input.setAccessibleName("passInput")
        user_input.setTextMargins(2,0,35,0)
        user_input.setEchoMode(user_input.EchoMode.Password)
        user_input.setFixedHeight(40)
        user_input.setLayout(QHBoxLayout())
        user_input.layout().setContentsMargins(0,0,5,0)
        user_input.layout().setAlignment(Qt.AlignmentFlag.AlignRight)
        user_input.setStyleSheet(self.user_input_style)
        user_input.setFont(self.user_input_font)
        
        clear_btn = QPushButton()
        clear_btn.setText("X")
        clear_btn.setFixedSize(self.clear_btn_size)
        clear_btn.setFont(self.clear_btn_font)
        clear_btn.setFlat(True)
        clear_btn.setStyleSheet(self.clear_btn_style)
        clear_btn.setCursor(clear_btn.cursor())
        clear_btn.clicked.connect(lambda x: self.clear_input(user_input, clear_btn))

        # Hide clear button untill lineedit is populated
        clear_btn.setVisible(False)
        user_input.textEdited.connect(lambda x: self.show_clear_btn(user_input, clear_btn))

        user_input.layout().addWidget(clear_btn)
        container.layout().addWidget(user_input)

        return container

    def remeberMe(self):
        """"""
        rem_me = QCheckBox()
        rem_me.setText(self.remember_btn_text)
        rem_me.setStyleSheet(self.remeber_me)

        return rem_me

    def submitBtn(self):
        """"""
        submit = QPushButton()
        submit.setText(self.login_btn_text)
        submit.setFont(QFont("GungSahChe", 12, 500))
        submit.setFixedSize(self.login_btn_size)
        submit.setStyleSheet(self.login_btn_style)
        submit.setObjectName("submitButton")

        submit.clicked.connect(lambda x: self.__get_credentials())

        return submit
    
    def footer(self):
        """"""
        footer = QLabel()
        footer.setText(self.footer_text)
        footer.setFont(QFont(self.font_family, 14, 500))
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setFont(QFont("GungSahChe", 9, 300, True))
        footer.setStyleSheet(self.footer_style)

        return footer
    
    def padding(self, height: int = 45) -> QWidget:
        """"""
        padding = QWidget()
        padding.setFixedHeight(height)

        return padding
    
    def show_clear_btn(self, line_edit: QLineEdit, btn: QWidget) -> None:
        """"""
        text_len = len(line_edit.text())

        if text_len <= 4:
            btn.setVisible(False)
        else:
            btn.setVisible(True)

        return None
    
    def clear_input(self, line_edit: QLineEdit, btn: QWidget) -> None:
        """"""
        line_edit.clear()

        text_len = len(line_edit.text())

        if text_len <= 4:
            btn.setVisible(False)
        else:
            btn.setVisible(True)

        return None

    def __get_credentials(self) -> str:
        """"""

        passcode = self.findChild(QLineEdit, "passInput")
        username = self.findChild(QLineEdit, "emailInput")
        submitBtn = self.findChild(QPushButton, "submitButton")

        print("password: " + passcode.text())
        print("username: " + username.text())

        submitBtn.clearFocus()
