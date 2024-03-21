from tkinter import * 

def submit(): 
    print(str(scale.get()))

window = Tk()

scale = Scale(
    window, 
    from_ = 0, 
    to_ = 100, 
    length = 600, 
    orient = HORIZONTAL, 
    font = ("Ariel", 18), 
    tickinterval = 10 
)
scale.set(((scale['from'] - scale['to'])/2) + scale['to']) # appears in the middle regardless of the range spwcified
scale.pack() 

button = Button(
    window, 
    text = "submit", 
    command = submit
)
button.pack() 

window.mainloop()