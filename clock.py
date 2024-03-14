from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Digital Clock")

def clock():
    screen = strftime("%H:%M:%S %p")
    label.config(text=screen)
    label.after(1000, clock)

label = Label(window, font=("digital-7",35, "italic"), background="black", foreground="green")
label.pack()

clock()
window.mainloop()