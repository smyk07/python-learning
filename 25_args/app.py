def add(*args): 
    sum = 0
    for i in args: 
        sum += i 
    return sum 

# *args will be present as a list, and can be operated upon as a list

print(add(4, 5, 9, 8, 0, 278))