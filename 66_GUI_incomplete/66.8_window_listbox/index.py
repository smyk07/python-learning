def submit(): 
    food = []
    
    for i in listbox.curselection(): 
        food.insert(i, listbox.get(i))
    
    for i in food: 
        print(i) 

def add_item(): 
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())
    entry_box.delete(0, END)

def delete_item(): 
    for i in reversed(listbox.curselection()): 
        listbox.delete(i)
    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(
    window,
    font = ("Ariel", 16), 
    bg = "#f7ffde", 
    width = 35 ,
    selectmode = MULTIPLE
)

listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Gread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad") 

listbox.config(height=listbox.size())

entry_box = Entry(
    window
)

entry_box.pack()

add_button = Button(
    window, 
    text = "Add Item", 
    command = add_item
)

add_button.pack()

delete_button = Button(
    window, 
    text = "Delete Item", 
    command = delete_item
)

delete_button.pack()

submit_button = Button(
    window, 
    text = "Submit", 
    command = submit
)

submit_button.pack()

window.mainloop()