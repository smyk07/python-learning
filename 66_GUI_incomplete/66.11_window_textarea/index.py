from tkinter import *

def submit(): 
    input_txt = text.get("1.0", END) 
    print(input_txt)

window = Tk()

text = Text(
    window, 
    bg = "light yellow", 
    font = ("Ariel", 16),
    padx=20,
    pady=20 
)
text.pack()

button = Button(
    window, 
    command = submit, 
    text = "submit"
)
button.pack() 

window.mainloop()