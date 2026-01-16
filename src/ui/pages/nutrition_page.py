from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

from src.ui.modules.nutrition_module import NutritionModule

class NutritionPage(QWidget):
    
    def __init__(self):
        super().__init__()
        
        #WIDGETS
        scroll_container = QWidget()
        nutrition_modules = self.load_modules(3)
        
        #LAYOUT
        scroll_layout = QVBoxLayout()
        for item in nutrition_modules:
            scroll_layout.addWidget(item)
        scroll_layout.addStretch()
        
        scroll = QScrollArea()
        scroll.setWidget(scroll_container)
        scroll.setWidgetResizable(True)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(scroll)
        
        
        #FINALIZE
        scroll_container.setLayout(scroll_layout)
        self.setLayout(layout)
        
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("black"))
        self.setPalette(palette)
        
    def load_modules(self, n: int) -> list[NutritionModule]:
        res = []
        
        for i in range(n):
            res.append(NutritionModule())
        
        return res