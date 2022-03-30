import calculate as calcFuncs
import printStarterStatement
from tkinter import *

def printtest():
    print(calcFuncs.add(4,6))


#Functions Used when creating a window
def createWindow(w,h, color, name):
    
    #icon features are removed temporarlily
    #iconimage = r"\Users\logansantamarina\Documents\VisualStudioCode\CalculatorProject\Pictures\calculator.png"
    #calc_window.iconphoto(False, PhotoImage(file = iconimage))
    calc_window = Tk()
    calc_window.title(name)
    calc_window.configure(width= w, height= h, bg= color)
   
    testButton = Button(text= "PrintMessage", command= printtest, bg = "#51ff00")
    testButton.place(x= w/2, y= h/2)
    #don't put anything above this
    calc_window.mainloop()

#the call to create a window
createWindow(w= 540 , h= 1080, name= "Logan's Calculator", color= "#919191")
