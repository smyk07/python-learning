import os 

source = "./file.txt"
destination = "./dir/file.txt"

try: 
    if os.path.exists(destination): 
        print("The file already exists")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError: 
    print(source + " was not found")