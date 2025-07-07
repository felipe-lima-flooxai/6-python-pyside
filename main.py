import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from main_window import MainWindow
from variables import WINDOW_ICON_PATH

def temp_label(text):
    label1 = QLabel(text)
    label1.setStyleSheet("font-size: 50px")
    return label1

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    #define icon
    icon = QIcon(str(WINDOW_ICON_PATH), )
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.adjustFixedSize()
    window.show()
    app.exec()