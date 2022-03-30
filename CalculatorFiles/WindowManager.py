#import calculate
import printStarterStatement
from tkinter import *


#Functions Used when creating a window
def createWindow(w,h, color, name):
<<<<<<< HEAD
    #iconimage = None
    calc_window = Tk()
    calc_window.title(name)
    calc_window.configure(width= w, height= h, bg= color)
    #calc_window.iconphoto(False, PhotoImage(file = iconimage))
=======
    iconimage = r"C:\Users\logan\OneDrive\New Documents\Programming\Vs-Code-Projects\GitProjects\CalculatorWindows\Calculator-Project\Pictures\calculator.png"
    calc_window = Tk()
    calc_window.title(name)
    calc_window.configure(width= w, height= h, bg= color)
    #icon definer
    calc_window.iconphoto(False, PhotoImage(file = iconimage))
>>>>>>> 1fd2a7d8d95d60f6f00ffa20c4b6e8bcdc277a7f
    calc_window.mainloop()

#the call to create a window
createWindow(w= 1920, h= 1080, name= "Logan's Calculator", color= "#062ebf")
