# a label is an area widget and / or an image within a window

from tkinter import *

window = Tk()

window.geometry("640x640")

photo = PhotoImage(file="star.png")

label = Label(
    window, 
    text="Hello World!", 
    font=("Arial", 40, "bold"), 
    relief="raised", 
    bd=10, 
    padx=20, 
    pady=10, 
    image=photo,
    compound="top"
)
label.place(x=5, y=5) 

window.mainloop()