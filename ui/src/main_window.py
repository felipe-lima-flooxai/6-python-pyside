from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.buttonEnviar.clicked.connect(self.changeLabelResult)

    def changeLabelResult(self):
        text = self.lineName.text()
        self.labelResult.setText(text)

if __name__ == "__main__":
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()