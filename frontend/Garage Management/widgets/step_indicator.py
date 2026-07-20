from PyQt5.QtWidgets import (
    QFrame,
    QWidget,
    QLabel,
    QVBoxLayout
)
from PyQt5.QtCore import Qt


class StepIndicator(QWidget):
    def __init__(self):
        super().__init__()
        self.steps = []
        self.current_index = 0

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def set_steps(self, step_icons):
        self.steps = [{"icon": icon} for icon in step_icons]
        self.refresh_ui()

    def add_steps(self, icon):
        self.steps.append({"icon": icon})
        self.refresh_ui()

    def set_current_step(self, index):
        if 0 <= index < len(self.steps):
            self.current_index = index
            self.refresh_ui()

    def clear_layout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def refresh_ui(self):
        self.clear_layout()
        for i, step in enumerate(self.steps):
            is_active = (i == self.current_index)
            node = self.create_circle_node(step["icon"], is_active)
            self.layout.addWidget(node, alignment=Qt.AlignHCenter)
            if i < len(self.steps) - 1:
                dotted = (i < self.current_index)
                line = self.create_connecting_line(dotted=dotted)
                self.layout.addWidget(line, alignment=Qt.AlignHCenter)

    def create_circle_node(self, icon_text, is_active):
        node = QLabel(icon_text)
        node.setAlignment(Qt.AlignCenter)
        node.setFixedSize(50, 50)

        if is_active:
            node.setStyleSheet("""
                QLabel {
                    background-color: #B7C2D2;
                    color: #fff;
                    border-radius: 25px;
                    font-size: 18px;
                }
            """)
        else:
            node.setStyleSheet("""
                QLabel {
                    background-color: #fff;
                    border: 1px solid #B7C2D2;
                    color: #000;
                    border-radius: 25px;
                    font-size: 18px;
                }
            """)

        return node

    def create_connecting_line(self, dotted=False):
        line = QFrame()
        line.setFixedWidth(2)
        line.setFixedHeight(40)
        border_style = "dotted" if dotted else "solid"
        line.setStyleSheet(f"""
            QFrame {{
                border-left: 1px {border_style} #B7C2D2;
                background: transparent;
            }}
        """)

        return line