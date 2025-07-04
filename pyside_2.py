#Mesma funcionalidade do pyside_1.py, porém em formato de classe.
#Gostei pq ficou mais organizado. Parece um componente react.

import sys
from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QGridLayout,
    QMainWindow, QStatusBar, QMenuBar, QAction
)
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo com Classes e Slots")

        # Widgets e layout central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.create_buttons()
        self.create_status_bar()
        self.create_menu()

    def create_buttons(self):
        self.button1 = QPushButton("Texto do Botão 1")
        self.button1.setStyleSheet("font-size: 40px;")

        self.button2 = QPushButton("Texto do Botão 2")
        self.button2.setStyleSheet("font-size: 20px;")

        self.layout.addWidget(self.button1, 1, 1)
        self.layout.addWidget(self.button2, 1, 2)

        self.button1.clicked.connect(self.handle_button1_click)

    def create_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Mostrar mensagem na barra")

    def create_menu(self):
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)

        menu = menu_bar.addMenu("Qualquer coisa")

        self.first_action = QAction("Primeira ação", self)
        self.first_action.triggered.connect(self.slot_example)
        menu.addAction(self.first_action)

        self.second_action = QAction("Segunda ação", self)
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.outro_slot)
        self.second_action.hovered.connect(self.terceiro_slot)
        menu.addAction(self.second_action)

    @Slot()
    def slot_example(self):
        self.status_bar.showMessage("O meu slot foi executado")

    @Slot(bool)
    def outro_slot(self, checked):
        print("Está Marcado?", checked)

    @Slot()
    def terceiro_slot(self):
        checked = self.second_action.isChecked()
        self.outro_slot(checked)

    @Slot()
    def handle_button1_click(self):
        self.terceiro_slot()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())