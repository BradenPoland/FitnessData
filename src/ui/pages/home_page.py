from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

from src.ui.modules.weight_module import WeightModule

class HomePage(QWidget):
    
    def __init__(self):
        super().__init__()
        
        #WIDGETS
        weight_module = WeightModule()
        
        #LAYOUT
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(weight_module)
        
        #FINALIZE
        self.setLayout(layout)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("black"))
        self.setPalette(palette)