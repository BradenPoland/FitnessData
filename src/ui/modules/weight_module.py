from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

from src.ui.widgets.metric_display import MetricDisplay
from src.ui.modules.weight_input import WeightInput

class WeightModule(QWidget):
    
    def __init__(self):
        super().__init__()
        
        metrics = [
            "7 Day Avg",
            "Today",
            "Trend"
        ]
        
        #WIDGETS
        metric_container = QWidget()
        self.metric_displays = self.load_metrics(metrics)
        self.weight_input = WeightInput()
        
        #LAYOUT
        metric_layout = QHBoxLayout()
        for item in self.metric_displays:
            metric_layout.addWidget(item)
        
        layout = QVBoxLayout()
        layout.addWidget(metric_container)
        layout.addWidget(self.weight_input)
        
        
        #FINALIZE
        metric_container.setLayout(metric_layout)
        self.setLayout(layout)
        
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#2b2b2b"))
        self.setPalette(palette)
        self.setMinimumSize(400, 250)
        self.setMaximumHeight(250)
    
    def load_metrics(self, metrics: list[str]) -> list[MetricDisplay]:
        res = []
        
        for item in metrics:
            res.append(MetricDisplay(item))
        
        return res