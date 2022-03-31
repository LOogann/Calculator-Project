from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtWidgets import *
class state:
    NotImplemented

currentNumber = 4
currentState = None

addState = state()
subState = state()
mulState = state()
divState = state()


#=================================================================
#Initializes the Window and Neccesary Variables
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.cyan)

#defines Qwidget variables
TopText = QLabel("    0010")
addButton = QPushButton(text = "   +   ")
subButton = QPushButton(text = "   _   ")
debugText = QLabel(str(addState))
#=================================================================
#Layout design and Order
#put in order top to bottom

layout.addWidget(TopText)
layout.addSpacing(10)

layout.addWidget(addButton)
layout.addSpacing(2)

layout.addWidget(subButton)
layout.addSpacing(10)

layout.addWidget(debugText)
#=================================================================
#Button events
def addButtonEvent():
    print("Add")
    TopText.setText(str(currentNumber))
    currentState = addState
    debugText.setText(str(currentState))
def subButtonEvent():
    print("subtract")
    TopText.setText(str(-currentNumber))
    currentState = subState
    debugText.setText(str(currentState))

addButton.clicked.connect(addButtonEvent)
subButton.clicked.connect(subButtonEvent)

#=================================================================
#Finalizing Events
window.setLayout(layout)
app.setStyleSheet("QPushButton { margin: 5ex; }")
app.setPalette(palette)

#shows the window
window.show()
#Loops the Window Until Close
app.exec()

#=================================================================     