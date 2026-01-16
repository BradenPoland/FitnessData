from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

class MetricDisplay(QWidget):
    def __init__(self, name: str):
        super().__init__()
        
        #WIDGETS
        self.name_plate = QLabel(name)
        
        #LAYOUT
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.name_plate)
        
        #FINALIZE
        self.setLayout(layout)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("darkgray"))
        self.setPalette(palette)