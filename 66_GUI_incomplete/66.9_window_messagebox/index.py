from tkinter import * 
from tkinter import messagebox 

def click(): 
    print("Clicked")
    # messagebox.showinfo(
    #     title="Info messagebox",
    #     message="You are a person"
    # )
    
    # while True: # scammmm
    #     messagebox.showwarning(
    #         title="WARNING", 
    #         message="You have a virus!"
    #     ) 
    
    # messagebox.showerror(
    #     title="ERROR", 
    #     message="Something Went Wrong :("
    # )
    
    # if messagebox.askokcancel(title="Ask Ok Cancel", message="Are you sure?"): 
    #     print("OK")
    # else: 
    #     print("CANCELLED")
    
    # if messagebox.askretrycancel(title="Ask Retry Cancel", message="Are you sure?"): 
    #     print("OK")
    # else: 
    #     print("CANCELLED")
    
    # messagebox.askyesno( # can use if statement as above
    #     title="Ask yes or no", 
    #     message="Do you like cake?"
    # )
    
    # print(messagebox.askquestion(title="Ask Question", message="Do you like cake?"))
    
    # print(messagebox.askyesnocancel(title="Yes no cancel", message="Do You like to code"))

window = Tk()

button = Button(
    window, 
    command = click, 
    text = "Click Me!"
)
button.pack() 

window.mainloop()