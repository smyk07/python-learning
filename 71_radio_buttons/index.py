from tkinter import * 

food = ["Pizza", "Burger", "Hotdog"]

window = Tk()

pizza_img = PhotoImage(file="pizza.png")
pizza_img = pizza_img.subsample(10, 10)

burger_png = PhotoImage(file="burger.png") 
burger_png = burger_png.subsample(10, 10)

hotdog_png = PhotoImage(file="hot-dog.png")
hotdog_png = hotdog_png.subsample(10, 10)

food_png = [pizza_img, burger_png, hotdog_png] 

x = IntVar() 

window.geometry("1000x800")

for i in range(len(food)): 
    radiobutton = Radiobutton(
        window, 
        text = food[i], 
        variable = x, 
        value=i,
        font=("Ariel", 18), 
        padx = 25,
        pady = 10, 
        image = food_png[i], 
        compound = "left",
        # indicatoron=0,
        width=375,
        height=100
    )
    
    radiobutton.pack(anchor = W) 

window.mainloop()