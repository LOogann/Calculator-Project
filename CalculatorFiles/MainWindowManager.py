import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QPalette, QColor, QIcon

def UpdateText(changeText): 
    #check how many characters
    if len(TopNumberLabel.text()) <= 1000:
        current = TopNumberLabel.text()
        TopNumberLabel.setText(current + changeText)


def clearText():
    TopNumberLabel.setText(None)

#deletes the last number or function in the text
def deleteText():
    currentt = TopNumberLabel.text()
    if len(currentt) >=1:
        currentt = currentt.rstrip(currentt[-1])
        TopNumberLabel.setText(currentt)

#function called when buttons are pushed
def ButtonPushed(changeText, _operation = None, NumberPressed = None, doNumbers = False, RealNumber = None):    
    UpdateText(changeText)

#the function that is called when the equals function is clicked
#prints the result to the main text
def printEquals():

    try:

        answer = None
        answer = eval(TopNumberLabel.text())
        TopNumberLabel.setText(str(answer))
    except:
        TopNumberLabel.setText("Text Error")

#grid and buton setups
def loadBackGroundRows():

    #operation buttons
    back_button_color = '#1f1f1f'
    addButton = QPushButton("+")
    subButton = QPushButton("-")
    mulButton = QPushButton("*")
    divButton = QPushButton("/")
    expButton = QPushButton("^")
    equalsButton = QPushButton("=")

    

    #special buttons
    l_parenthesis_but = QPushButton("(")
    r_parenthesis_but = QPushButton(")")
    dot_Button = QPushButton(".")
    clearButton = QPushButton("clear")
    delButton = QPushButton("del")

    #numbers
    but_1 = QPushButton('1')
    but_2 = QPushButton('2')
    but_3 = QPushButton('3')
    but_4 = QPushButton('4')
    but_5 = QPushButton('5')
    but_6 = QPushButton('6')
    but_7 = QPushButton('7')
    but_8 = QPushButton('8')
    but_9 = QPushButton('9')
    but_0 = QPushButton('0')

    #style setting
    buttonColor = "background-color : #1f1f1f"
    
    addButton.setStyleSheet(buttonColor)
    subButton.setStyleSheet(buttonColor)
    mulButton.setStyleSheet(buttonColor)
    divButton.setStyleSheet(buttonColor)
    expButton.setStyleSheet(buttonColor)
    equalsButton.setStyleSheet(buttonColor)

    but_0.setStyleSheet(buttonColor)
    but_1.setStyleSheet(buttonColor)
    but_2.setStyleSheet(buttonColor)
    but_3.setStyleSheet(buttonColor)
    but_4.setStyleSheet(buttonColor)
    but_5.setStyleSheet(buttonColor)
    but_6.setStyleSheet(buttonColor)
    but_7.setStyleSheet(buttonColor)
    but_8.setStyleSheet(buttonColor)
    but_9.setStyleSheet(buttonColor)

    clearButton.setStyleSheet(buttonColor)
    delButton.setStyleSheet(buttonColor)
    dot_Button.setStyleSheet(buttonColor)


    #button events for numbers
    but_1.clicked.connect(lambda: ButtonPushed("1"))
    but_2.clicked.connect(lambda: ButtonPushed("2"))
    but_3.clicked.connect(lambda: ButtonPushed("3"))
    but_4.clicked.connect(lambda: ButtonPushed("4"))
    but_5.clicked.connect(lambda: ButtonPushed("5"))
    but_6.clicked.connect(lambda: ButtonPushed("6"))
    but_7.clicked.connect(lambda: ButtonPushed("7"))
    but_8.clicked.connect(lambda: ButtonPushed("8"))
    but_9.clicked.connect(lambda: ButtonPushed("9"))
    but_0.clicked.connect(lambda: ButtonPushed("0"))

    #button events for operations
    addButton.clicked.connect(lambda: ButtonPushed("+"))
    subButton.clicked.connect(lambda: ButtonPushed("-"))
    mulButton.clicked.connect(lambda: ButtonPushed("*"))
    divButton.clicked.connect(lambda: ButtonPushed("/"))
    expButton.clicked.connect(lambda: ButtonPushed("**"))
    dot_Button.clicked.connect(lambda: ButtonPushed("."))
    equalsButton.clicked.connect(printEquals)

    #specical button events

    l_parenthesis_but.clicked.connect(lambda: ButtonPushed("("))
    r_parenthesis_but.clicked.connect(lambda: ButtonPushed(")"))
    clearButton.clicked.connect(clearText)
    delButton.clicked.connect(deleteText)

    #top row for number output
    L_GridBackGrounds.addWidget(Color(back_button_color), 0,0,1,.1)
    L_GridBackGrounds.addWidget(TopNumberLabel, 0,0,1,.1)
    

    #numbers
    L_GridBackGrounds.addWidget(but_1, 1,0,1,1)
    L_GridBackGrounds.addWidget(but_2, 1,1,1,1)
    L_GridBackGrounds.addWidget(but_3, 1,2,1,1)
    L_GridBackGrounds.addWidget(but_4, 2,0,1,1)
    L_GridBackGrounds.addWidget(but_5, 2,1,1,1)
    L_GridBackGrounds.addWidget(but_6, 2,2,1,1)
    L_GridBackGrounds.addWidget(but_7, 3,0,1,1)
    L_GridBackGrounds.addWidget(but_8, 3,1,1,1)
    L_GridBackGrounds.addWidget(but_9, 3,2,1,1)
    L_GridBackGrounds.addWidget(but_0, 4,1,1,1)

    #parenthesis dont work
    # L_GridBackGrounds.addWidget(l_parenthesis_but, 4, 4, 1, 1)
    # L_GridBackGrounds.addWidget(r_parenthesis_but, 4, 3, 1, 1)

    L_GridBackGrounds.addWidget(clearButton, 4,0,1,1)
    L_GridBackGrounds.addWidget(delButton, 4,2, 1, 1)

    #operations
    L_GridBackGrounds.addWidget(addButton, 1,4,1,1)
    L_GridBackGrounds.addWidget(subButton, 2,4,1,1)
    L_GridBackGrounds.addWidget(mulButton, 3,4,1,1)
    L_GridBackGrounds.addWidget(divButton, 1,5,1,1)
    L_GridBackGrounds.addWidget(expButton, 2,5,1,1)
    L_GridBackGrounds.addWidget(equalsButton, 4,5,1,1)
    L_GridBackGrounds.addWidget(dot_Button, 3, 5, 1, 1)
    
    
    #set margins
    L_GridBackGrounds.setContentsMargins(5,10,5,10)
    L_GridBackGrounds.setSpacing(9)


    main_widgets.setLayout(L_GridBackGrounds)

#color widget
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadBackGroundRows()

        #sets icon
        path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), '/Users/logansantamarina/Documents/VisualStudioCode/Calculator Project/Pictures/logo.png')
        app.setWindowIcon(QIcon(path))

        #window setups
        self.setCentralWidget(main_widgets)
        self.setMinimumSize(600,400)
        self.setMaximumSize(600,400)
        self.setWindowTitle("Logan's Calculator")

app = QApplication(sys.argv)

main_widgets = QWidget()

L_GridButtons = QGridLayout()
L_GridBackGrounds = QGridLayout()

TopNumberLabel = QLabel("A simple calculator by logan")


window = MainWindow()
window.show()

app.exec()


#max characters in calculator is 78

#old=======================================v
# class operation():
#     def __init__(self, _operation):
#         self.operation = _operation
# class Cycle:
#     def __init__(self):
#         self.c_cycle = 0
    
#     def cycleUpdate(self):
#         if self.c_cycle == 3:
#             self.c_cycle = 0
#         self.c_cycle +=1
#         #print(self.c_cycle)

# cycle_class = Cycle()

# add_op = operation("add")
# sub_op = operation("sub")
# div_op = operation("div")
# mul_op = operation("mul")
# exp_op = operation("exp")
# equals_op = operation("equals")

# current_operation = operation("fillerop")



