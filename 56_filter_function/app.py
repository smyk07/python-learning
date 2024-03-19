# the filter() function creates collection of elements from an iterable for which a function returns true 

friends = [
    ("Rachel", 19), 
    ("Monica", 18), 
    ("Phoebe", 17), 
    ("Joey", 16), 
    ("Chandler", 21), 
    ("Ross", 20)
]

# (name ---- age)

can_drink = lambda data : data[1] >= 18

# long function 
# def can_drink(data): 
#     if data[1] >= 18: 
#         return True
#     else: 
#         return False

drinking_buddies = filter(can_drink, friends)

print(list(drinking_buddies))