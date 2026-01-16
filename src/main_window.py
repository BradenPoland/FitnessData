from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from src.plot_widget import PlotWidget
from src.data_service import load_weight, insert_weight

from src.ui.pages.home_page import HomePage
from src.ui.pages.nutrition_page import NutritionPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Boilerplate App")
        
        #WIDGETS
        self.plot = PlotWidget()
        self.home_page = HomePage()
        self.nutrition_page = NutritionPage()
        
        vline = QFrame()
        vline.setFrameShape(QFrame.Shape.VLine)
        vline.setFrameShadow(QFrame.Shadow.Plain)
        vline.setLineWidth(1)
        vline.setStyleSheet("color: white;")
        
        
        #LAYOUT
        layout = QHBoxLayout()
        
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        
        layout.addWidget(self.home_page, 4)
        layout.addWidget(vline, 0)
        layout.addWidget(self.nutrition_page, 6)
        
        
        #FINALIZE
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.refresh_plot()
        
    def refresh_plot(self):
        df = load_weight()
        if not df.empty:
            self.plot.set_data(df)