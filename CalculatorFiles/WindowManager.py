#import calculate
import printStarterStatement
from tkinter import *


#Functions Used when creating a window
def createWindow(w,h, color, name):
    iconimage = r"C:\Users\logan\OneDrive\New Documents\Programming\Vs-Code-Projects\GitProjects\CalculatorWindows\Calculator-Project\Pictures\calculator.png"
    calc_window = Tk()
    calc_window.title(name)
    calc_window.configure(width= w, height= h, bg= color)
    #icon definer
    calc_window.iconphoto(False, PhotoImage(file = iconimage))
    calc_window.mainloop()

#the call to create a window
createWindow(w= 1920, h= 1080, name= "Logan's Calculator", color= "#062ebf")
