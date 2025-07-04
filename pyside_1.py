import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout, QMainWindow

#os signals ficaram todos bugados kkkk

@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage("O meu slot foi executado")
    return inner


@Slot()
def outro_slot(checked):
    print("Está Marcado? ", checked)

@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

button = QPushButton("Texto do Botão 1")
button.setStyleSheet("font-size: 40px;")

button2 = QPushButton("Texto do Botão 2")
button2.setStyleSheet("font-size: 20px;")


layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(button, 1, 1)
layout.addWidget(button2, 1, 2)

#status bar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

#menu bar
menu = window.menuBar()
first_menu = menu.addMenu("Qualquer coisa")
first_action = first_menu.addAction("Primeira ação")
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction("Segunda ação")
second_action.setCheckable(True)
second_action.toggled.connect(outro_slot)
second_action.hovered.connect(terceiro_slot(second_action))

button.clicked.connect(terceiro_slot(second_action))

window.show()
app.exec()