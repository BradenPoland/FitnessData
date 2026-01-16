from PyQt6.QtWidgets import QWidget, QHBoxLayout
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

class NutritionModule(QWidget):
    def __init__(self):
        super().__init__()
        
        #WIDGETS
        
        
        #LAYOUT
        layout = QHBoxLayout()
        
        
        #FINALIZE
        self.setLayout(layout)
        
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#2b2b2b"))
        self.setPalette(palette)
        self.setMinimumSize(400, 400)
        self.setMaximumHeight(400)