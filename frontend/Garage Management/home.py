from PyQt5.QtWidgets import (QMainWindow,
                             QWidget,
                             QHBoxLayout)
from widgets.text_input import TextInput

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Garage Management System")
        self.setGeometry(100, 100, 800, 600)

        self.initUi()

    def initUi(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        input1 = TextInput(40, "Enter your first name", "resources/icons/category.svg")
        main_layout.addWidget(input1)

        self.setCentralWidget(main_widget)
