import sys
import os
from PyQt6.QtWidgets import QApplication
from src.main_window import MainWindow
from src.database import init_db

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    return os.path.join(os.path.abspath("."), relative_path)

def main():
    init_db()
    app = QApplication(sys.argv)

    style_path = resource_path("assets/style.qss")
    with open(style_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()