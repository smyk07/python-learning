def hello(**kwargs): 
    print("Hello", end=" ")
    for key, value in kwargs.items(): 
        print(value, end=" ")
        
# kwargs will be present as a dictionary

hello(title="Mr. ", first="Bro", last="Code")