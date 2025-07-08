import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox, QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget |  None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        #basic layout config bro
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        #title
        self.setWindowTitle("Calculadora")

        

    def adjustFixedSize(self, ):

        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)