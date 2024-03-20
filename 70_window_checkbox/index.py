from tkinter import *

def display(): 
    if x.get() == 1: 
        print("You Agreed")
    else: 
        print("You Disagree")

window = Tk()

x = IntVar()

check_button = Checkbutton(
    window, 
    text="I agree",
    font=("Ariel", 18), 
    variable=x, 
    command = display, 
    padx = 25,
    pady = 10
)

check_button.pack()

window.mainloop()