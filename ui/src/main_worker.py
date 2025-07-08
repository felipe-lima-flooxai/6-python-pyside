from PySide6.QtWidgets import QApplication, QWidget
from worker import Ui_Form

class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication()
    myWidget = MyWidget()
    myWidget.show()
    app.exec()