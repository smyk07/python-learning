age = int(input("How old are you?: "))

if age == 100: 
    print("You are a century old!")
elif age >= 18: 
    print("You are an adult.")
elif age < 0: 
    print("You aren't even born yet.")
else: # elif age < 18: 
    print("You are a child.")