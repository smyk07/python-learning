from tkinter import *
from tkinter import filedialog 
from tkinter import messagebox
import os 

def open_file(): 
    file_path = filedialog.askopenfilename(
        title="Open File", 
        initialdir="/mnt/e"
    )
    
    if os.path.exists(file_path): 
        read_file = open(file_path, "r") # displays in console
        print(read_file.read())
        read_file.close()
    else: 
        messagebox.showerror(
            title="Please Try Again", 
            message="Please try again, somthing went wrong"
        )

window = Tk()

button = Button(
    window, 
    text="Open File", 
    command=open_file
)
button.pack()

window.mainloop() 