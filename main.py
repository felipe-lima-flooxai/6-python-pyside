import sys
from display import Display
from buttons import ButtonsGrid
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from styles import setupTheme

def temp_label(text):
    label1 = QLabel(text)
    label1.setStyleSheet("font-size: 50px")
    return label1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    #define icon
    icon = QIcon(str(WINDOW_ICON_PATH), )
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    #display
    display = Display("")
    window.addWidgetToVLayout(display)

    #grid de botões
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()