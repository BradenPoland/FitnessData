from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

class WeightInput(QWidget):
    def __init__(self):
        super().__init__()
        
        #WIDGETS
        input_label = QLabel("Daily Weight")
        
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("lbs")
        
        enter_button = QPushButton("Enter")
        enter_button.clicked.connect(self.submit_input)
        
        
        #LAYOUT
        layout = QHBoxLayout()
        layout.addWidget(input_label)
        layout.addWidget(self.text_input)
        layout.addWidget(enter_button)
        
        
        #FINALIZE
        self.setLayout(layout)
        
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("darkgray"))
        self.setPalette(palette)
        self.setMaximumHeight(50)
    
    def submit_input(self):
        text = self.text_input.text