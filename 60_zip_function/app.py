# aggregate elements from two or mmore iterables 

display_name = ["Dude", "Bro", "Mister"]
usernames = ["dude123", "bro43", "mister4"]
passwords = ["password123", "passwordabc", "guest123"]

users = list(zip(display_name, usernames, passwords)) 

for i in users: 
    print(i)
