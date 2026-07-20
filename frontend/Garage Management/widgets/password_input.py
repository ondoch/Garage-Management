from PyQt5.QtWidgets import (
    QFrame,
    QLineEdit,
    QHBoxLayout,
    QLabel,
    QPushButton
)
from PyQt5.QtGui import (
    QPixmap,
    QIcon
)
from PyQt5.QtCore import Qt, QSize


class PasswordInput(QFrame):
    def __init__(self, height, placeholder, icon_url,
                 show_icon_url=None, hide_icon_url=None):
        super().__init__()

        self.height = height
        self.placeholder = placeholder
        self.icon_url = icon_url

        self.show_icon_url = show_icon_url
        self.hide_icon_url = hide_icon_url

        self.password_visible = False

        self.initUi()

    def initUi(self):
        main_layout = QHBoxLayout(self)

        main_layout.setContentsMargins(8, 1, 8, 1)
        main_layout.setSpacing(1)

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

        self.entry = QLineEdit()
        self.entry.setPlaceholderText(self.placeholder)
        self.entry.setEchoMode(QLineEdit.Password)

        self.toggle_btn = QPushButton()
        self.toggle_btn.setObjectName("toggleBtn")
        self.toggle_btn.setCursor(Qt.PointingHandCursor)
        self.toggle_btn.setFixedSize(
            self.height - 10,
            self.height - 10
        )
        self.toggle_btn.setFlat(True)
        self.toggle_btn.clicked.connect(self.togglePasswordVisibility)

        self.updateToggleIcon()

        main_layout.addWidget(icon)
        main_layout.addWidget(self.entry)
        main_layout.addWidget(self.toggle_btn)

        self.setFixedHeight(self.height)

        self.setStylesheet()

    def togglePasswordVisibility(self):
        self.password_visible = not self.password_visible

        if self.password_visible:
            self.entry.setEchoMode(QLineEdit.Normal)
        else:
            self.entry.setEchoMode(QLineEdit.Password)

        self.updateToggleIcon()

    def updateToggleIcon(self):
        if self.show_icon_url and self.hide_icon_url:
            icon_path = self.hide_icon_url if self.password_visible else self.show_icon_url
            self.toggle_btn.setIcon(QIcon(icon_path))
            self.toggle_btn.setText("")
            self.toggle_btn.setIconSize(
                QSize(self.height - 18, self.height - 18)
            )
        else:
            self.toggle_btn.setIcon(QIcon())

    def text(self):
        return self.entry.text()

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

            QPushButton#toggleBtn {
                border: none;
                background: transparent;
                font-size: 14px;
            }

            QPushButton#toggleBtn:hover {
                background: #F3F4F6;
                border-radius: 4px;
            }
        """)