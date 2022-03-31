from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtWidgets import *
#Initializes the Window
app = QApplication([])
app.setStyle('Macintosh')
window = QWidget()
layout = QVBoxLayout()

# topNumberLabel = QLabel('0000')
# topNumberLabel.show()

layout.addWidget(QLabel("0000"))
layout.addSpacing(50)

layout.addWidget(QPushButton(text = "Click To Click"))
layout.addSpacing(100)

layout.addWidget(QPushButton(text = "Click To Click To Click"))

window.setLayout(layout)

#shows the window
window.show()
#Loops the Window Until Close
app.exec()