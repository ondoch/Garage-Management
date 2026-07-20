from PyQt5.QtWidgets import (QMainWindow,
                             QWidget,
                             QHBoxLayout)
from widgets.step_indicator import StepIndicator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Garage Management System")
        self.setGeometry(100, 100, 800, 600)

        self.initUi()

    def initUi(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        self.indicator = StepIndicator()
        self.indicator.set_steps(["📄", "👤", "💻"])
        main_layout.addWidget(self.indicator)

        self.setCentralWidget(main_widget)
