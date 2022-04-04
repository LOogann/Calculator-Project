import calculate as calcFuncs
import printStarterStatement
from tkinter import *
from tkmacosx import Button

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
    
    # testButton = Button(text= "PrintMessage", command= printtest, bg ='#3E4149')
    # testButton.place(x= 220, y= 600)
    # label1 = Label(text="Tkinter", fg= "white", bg= "black")
    # label1.place(x= 220, y= 100)

    # B1 = Button(calc_window, text='Mac OSX', bg='#51ff00',fg='#51ff00', borderless=1)
    # B1.place(x=0, y= 0, width= 220, height=30)
    #don't put anything above this
    calc_window.mainloop()

#the call to create a window
createWindow(w= 540 , h= 1080, name= "Logan's Calculator", color= "#919191")
