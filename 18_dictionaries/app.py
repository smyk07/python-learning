capitals = {
    "USA": "Washington DC", 
    "India": "New Delhi",
    "China": "Beijing", 
    "Russia": "Moscow"  
}

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items(): 
    print(key + "'s caiptal is " + value)