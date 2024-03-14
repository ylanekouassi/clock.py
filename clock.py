from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Digital Clock")

def clock():
    screen = strftime("%H:%M:%S %p")
    label.config(text=screen)
    label.after(1000, clock)

label = Label(window, font=("digital-1",50, "bold"), background="black", foreground="green")


window.mainloop()