# creating a GUI in python, using TKINTER module 

# windows = containers for widgets 
# widgets = gui elements such as buttons, images, etc. 

from tkinter import *

window = Tk() # instantiate an instance of a window 

window.geometry("420x420")
window.title("Python GUI")
icon = PhotoImage(file="star.png")
window.iconphoto(True, icon)
window.config(background="black")

window.mainloop() # place window on screen and listen for events