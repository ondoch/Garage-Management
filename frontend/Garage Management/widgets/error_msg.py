from PyQt5.QtWidgets import (QFrame,
                             QLabel,
                             QHBoxLayout)
from PyQt5.QtCore import Qt

class ErrorMsg(QFrame):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.initUi()
        self.setStylesheet()

    def initUi(self):
        main_layout = QHBoxLayout(self)
        main_layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)

        error_msg = QLabel(self.message)
        main_layout.addWidget(error_msg)

    def setStylesheet(self):
        self.setStyleSheet("""
            QFrame {
                background-color: #FDBDBA;
                border: 1px solid #811007;
                border-radius: 5px;
            }
            QLabel{
                color: #811007;
                border: none;
            }"""
        )
