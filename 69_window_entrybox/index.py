# entrybox widget -> textbox that accepts a single line of user input

from tkinter import * 

def submit(): 
    username = entry.get()
    print(username)
    entry.config(state=DISABLED) 

def delete():
    entry.delete(0, END)  

window = Tk()

entry = Entry(
    window, 
    font=("Ariel", 18),
    show="*"
)

# entry.show(0, "Enter something")

submit_button = Button(
    window, 
    text="Submit", 
    command=submit
)

delete_button = Button(
    window, 
    text="Delete", 
    command=delete
)

entry.pack(side=LEFT)
submit_button.pack() 
delete_button.pack(side=RIGHT)

window.mainloop()