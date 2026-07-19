from PyQt5.QtWidgets import (QFrame,
                             QLabel,
                             QHBoxLayout)
from PyQt5.QtCore import Qt

class SuccessMsg(QFrame):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.initUi()
        self.setStylesheet()

    def initUi(self):
        main_layout = QHBoxLayout(self)
        main_layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)

        success_msg = QLabel(self.message)
        main_layout.addWidget(success_msg)

    def setStylesheet(self):
        self.setStyleSheet("""
            QFrame {
                background-color: #BEF8D5;
                border: 1px solid #109442;
                border-radius: 5px;
            }
            QLabel{
                color: #109442;
                border: none;
            }"""
        )
