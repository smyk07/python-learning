import os 
import shutil 

path = "file.txt"

try: 
    os.remove(path) # delete a file
    # os.rmdir(path) # delete a file or a folder 
    # shutil.rmtree(path) # deletes the whole specified tree
except FileNotFoundError: 
    print("The file was not found")
except PermissionError: 
    print("You do not have permissions to do that")
except OSError: 
    print("That folder contains files")
else: 
    print("Successful")