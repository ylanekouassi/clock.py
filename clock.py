from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Digital Clock")

def clock():
    screen = strftime("%H:%M:%S %p")


window.mainloop()