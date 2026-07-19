from PyQt5.QtWidgets import (QMainWindow,
                             QWidget,
                             QHBoxLayout)
from widgets.success_msg import SuccessMsg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Garage Management System")
        self.setGeometry(100, 100, 800, 600)

        self.initUi()

    def initUi(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        success_msg = SuccessMsg("Account Created Successfully")
        main_layout.addWidget(success_msg)

        self.setCentralWidget(main_widget)
