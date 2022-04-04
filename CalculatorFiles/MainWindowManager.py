import sys
import calculate as calc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QPalette, QColor


CurrentText = "00000"
Number1 = None
Number2 = None
Cycle = 0

def UpdateText(changeText):
    
    #check how many characters
    if len(TopNumberLabel.text()) <= 1000:

        current = TopNumberLabel.text()
        ButtonPressed = changeText
        TopNumberLabel.setText(current + changeText)
    #print(len(TopNumberLabel.text()))

def clearText():
    TopNumberLabel.setText(None)

def deleteText():
    currentt = TopNumberLabel.text()
    if len(currentt) >=1:
        currentt = currentt.rstrip(currentt[-1])
        TopNumberLabel.setText(currentt)


def ButtonPushed(changeText, operation = None, NumberPressed = None, doNumbers = False):
    
    if doNumbers:

    
        if Cycle <=2:
            Cycle +=1
        else:
            Cycle = 0
    
        if Cycle == 1:
            Number1 = NumberPressed
            print(Number1)
        if Cycle == 2:
            Number2 = NumberPressed
            print(Number2)
    
    UpdateText(changeText)
    #if operation != None:
        #print(operation)

def loadBackGroundRows():

    back_button_color = '#7f8a94'
    addButton = QPushButton("+")
    subButton = QPushButton("-")
    mulButton = QPushButton("*")
    divButton = QPushButton("/")
    expButton = QPushButton("^")
    equalsButton = QPushButton("=")
    clearButton = QPushButton("clear")
    delButton = QPushButton("del")

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

    but_1.clicked.connect(lambda: ButtonPushed("1", NumberPressed= 1, doNumbers= True))
    but_2.clicked.connect(lambda: ButtonPushed("2", NumberPressed= 2, doNumbers= True))
    but_3.clicked.connect(lambda: ButtonPushed("3", NumberPressed= 3, doNumbers= True))
    but_4.clicked.connect(lambda: ButtonPushed("4", NumberPressed= 4, doNumbers= True))
    but_5.clicked.connect(lambda: ButtonPushed("5", NumberPressed= 5, doNumbers= True))
    but_6.clicked.connect(lambda: ButtonPushed("6", NumberPressed= 6, doNumbers= True))
    but_7.clicked.connect(lambda: ButtonPushed("7", NumberPressed= 7, doNumbers= True))
    but_8.clicked.connect(lambda: ButtonPushed("8", NumberPressed= 8, doNumbers= True))
    but_9.clicked.connect(lambda: ButtonPushed("9", NumberPressed= 9, doNumbers= True))
    but_0.clicked.connect(lambda: ButtonPushed("0", NumberPressed= 0, doNumbers= True))


    addButton.clicked.connect(lambda: ButtonPushed("+", add_op.operation))
    subButton.clicked.connect(lambda: ButtonPushed("-", sub_op.operation))
    mulButton.clicked.connect(lambda: ButtonPushed("*", mul_op.operation))
    divButton.clicked.connect(lambda: ButtonPushed("/", div_op.operation))
    expButton.clicked.connect(lambda: ButtonPushed("^", exp_op.operation))
    equalsButton.clicked.connect(lambda: ButtonPushed(" = ", equals_op.operation))
    clearButton.clicked.connect(clearText)
    delButton.clicked.connect(deleteText)

    #top row for number output
    #L_GridBackGrounds.addWidget(Color(back_button_color), 0,0,1,.1)
    L_GridBackGrounds.addWidget(TopNumberLabel, 0,0,1,.1)
    

    #row two
    L_GridBackGrounds.addWidget(but_1, 1,0,1,1)
    L_GridBackGrounds.addWidget(but_2, 1,1,1,1)
    L_GridBackGrounds.addWidget(but_3, 1,2,1,1)
    #row three
    L_GridBackGrounds.addWidget(but_4, 2,0,1,1)
    L_GridBackGrounds.addWidget(but_5, 2,1,1,1)
    L_GridBackGrounds.addWidget(but_6, 2,2,1,1)
    #row four
    L_GridBackGrounds.addWidget(but_7, 3,0,1,1)
    L_GridBackGrounds.addWidget(but_8, 3,1,1,1)
    L_GridBackGrounds.addWidget(but_9, 3,2,1,1)
    L_GridBackGrounds.addWidget(but_0, 4,1,1,1)
    L_GridBackGrounds.addWidget(clearButton, 4,0,1,1)
    L_GridBackGrounds.addWidget(delButton, 4,2, 1, 1)
    #row five
    L_GridBackGrounds.addWidget(addButton, 1,4,1,1)
    L_GridBackGrounds.addWidget(subButton, 2,4,1,1)
    L_GridBackGrounds.addWidget(mulButton, 3,4,1,1)
    #column six 
    L_GridBackGrounds.addWidget(divButton, 1,5,1,1)
    L_GridBackGrounds.addWidget(expButton, 2,5,1,1)
    L_GridBackGrounds.addWidget(equalsButton, 3,5,1,1)
    #set margins
    L_GridBackGrounds.setContentsMargins(10,6,10,6)
    L_GridBackGrounds.setSpacing(10)


    main_widgets.setLayout(L_GridBackGrounds)
def loadButtonRows():
    addButton = QPushButton("+")
    subButton = QPushButton("-")
    mulButton = QPushButton("*")
    divButton = QPushButton("/")

    L_GridBackGrounds.addWidget(addButton, 1,5,1,1)
    L_GridBackGrounds.addWidget(subButton, 2,5,1,1)
    L_GridBackGrounds.addWidget(mulButton, 3,5,1,1)

    #L_GridBackGrounds.addLayout(L_GridButtons, 0, 0, 0, 0)

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

        self.setCentralWidget(main_widgets)
        self.setMinimumSize(500,300)

        self.setWindowTitle("The Calculator")
class operation():
    def __init__(self, _operation):
        self.operation = _operation

add_op = operation("add")
sub_op = operation("sub")
div_op = operation("div")
mul_op = operation("mul")
exp_op = operation("exp")
equals_op = operation("equals")

current_operation = operation("fillerop")

app = QApplication(sys.argv)

main_widgets = QWidget()

L_GridButtons = QGridLayout()
L_GridBackGrounds = QGridLayout()

TopNumberLabel = QLabel("   ")

window = MainWindow()
window.show()

app.exec()


#max characters in calculator is 78