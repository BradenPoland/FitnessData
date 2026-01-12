import sys
from PyQt6.QtWidgets import QApplication
from src.main_window import MainWindow
from src.database import init_db

def main():
    init_db()
    app = QApplication(sys.argv)
    with open("assets/style.qss") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()