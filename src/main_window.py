from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from src.plot_widget import PlotWidget
from src.data_service import load_measurements, insert_measurements

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Boilerplate App")
        
        self.plot = PlotWidget()
        self.button = QPushButton("Add Random Data")
        self.button.clicked.connect(self.add_data)
        
        layout = QVBoxLayout()
        layout.addWidget(self.plot)
        layout.addWidget(self.button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.refresh_plot()
        
    def refresh_plot(self):
        df = load_measurements()
        if not df.empty:
            self.plot.set_data(df)
    
    def add_data(self):
        import random
        insert_measurements(random.random() * 100)
        self.refresh_plot()