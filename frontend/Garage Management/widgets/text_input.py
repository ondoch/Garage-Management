from PyQt5.QtWidgets import (
    QFrame,
    QLineEdit,
    QHBoxLayout,
    QLabel
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class TextInput(QFrame):
    def __init__(self, height, placeholder, icon_url):
        super().__init__()

        self.height = height
        self.placeholder = placeholder
        self.icon_url = icon_url

        self.initUi()

    def initUi(self):
        main_layout = QHBoxLayout(self)

        main_layout.setContentsMargins(8, 1, 8, 1)
        main_layout.setSpacing(5)

        # Icon
        icon = QLabel()
        icon.setObjectName("iconLabel")
        icon.setAlignment(Qt.AlignCenter)

        icon.setFixedSize(
            self.height - 10,
            self.height - 10
        )

        pixmap = QPixmap(self.icon_url)

        icon.setPixmap(
            pixmap.scaled(
                self.height - 15,
                self.height - 15,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        # Input
        entry = QLineEdit()
        entry.setPlaceholderText(self.placeholder)

        # Add widgets to layout
        main_layout.addWidget(icon)
        main_layout.addWidget(entry)

        self.setFixedHeight(self.height)

        self.setStylesheet()

    def setStylesheet(self):
        self.setStyleSheet("""
            QFrame {
                border: 1px solid #ADADAD;
                border-radius: 5px;
                background: white;
            }

            QFrame:hover {
                border: 1px solid #000;
            }

            QLabel#iconLabel {
                border: none;
                background: transparent;
            }

            QLineEdit {
                border: none;
                background: transparent;

                font-family: "Segoe UI";
                font-size: 14px;
                font-weight: 400;

                color: #2D3748;
                padding: 7px 8px;
            }

            QLineEdit::placeholder {
                color: #9CA3AF;
            }
        """)