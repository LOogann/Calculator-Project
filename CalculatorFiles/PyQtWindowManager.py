from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGroupBox
from PyQt5.QtWidgets import *


class state:
    NotImplemented

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

# horizontalGroupBox = QGroupBox("What is your favorite color?")
# layoutHor = QHBoxLayout()
# buttonBlue = QPushButton('Blue',text= "button button")
# #buttonBlue.clicked.connect(self.on_click)
# layoutHor.addWidget(buttonBlue)
# layoutHor.addWidget(horizontalGroupBox)
# horizontalGroupBox.setLayout(layout)



#defines Qwidget variables
TopText = QLabel("    0010")
addButton = QPushButton(text = "   +   ")
subButton = QPushButton(text = "   _   ")
button_1 = QPushButton(text = "1")
button_2 = QPushButton(text = "2")
button_3 = QPushButton(text = "3")
button_4 = QPushButton(text = "4")
button_5 = QPushButton(text = "5")
button_6 = QPushButton(text = "6")
button_7 = QPushButton(text = "7")
button_8 = QPushButton(text = "8")
button_9 = QPushButton(text = "9")
button_0 = QPushButton(text = "0")
debugText = QLabel(str(addState))
#=================================================================
#Layout design and Order
#put in order top to bottom

layout.addWidget(TopText)
layout.addSpacing(10)

layout.addWidget(addButton)
addButton.clicked.connect(addButtonEvent)
layout.addSpacing(2)

layout.addWidget(subButton)
subButton.clicked.connect(subButtonEvent)
layout.addSpacing(10)

layout.addWidget(debugText)
#=================================================================



#=================================================================
#Finalizing Events
window.setLayout(layout)
app.setStyleSheet("QPushButton { margin: 5ex; }")
app.setPalette(palette)

#shows the window
window.show()

window.setWindowTitle("the calculator")
#Loops the Window Until Close
app.exec()

#=================================================================     