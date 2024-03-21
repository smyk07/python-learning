# buttons in gui -> click it and it does stuff 

from tkinter import *

count = 0

def button_click(): 
    global count
    count += 1 
    print("Button clicked ", count, " times")

window = Tk()

photo = PhotoImage(file="star.png")

window.geometry("420x420")

button = Button(
    window, 
    text="Click Me", 
    command = button_click, 
    font=("Comic Sans", 30), 
    fg="yellow", 
    bg="black", 
    activebackground="black", 
    activeforeground="yellow", 
    # state=DISABLED, # makes button unclickable
    image=photo, 
    compound="bottom"
)

button.pack()

window.mainloop()