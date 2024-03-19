# the map() function applies a function to each item in an iterable. 

us_store = [
    ("shirt", 20.00),
    ("jeans", 50.00), 
    ("jacket", 65.00), 
    ("socks", 3.00), 
    ("gloves", 4.50), 
    ("trousers", 45.00)
]

# (name --- price)

to_rupees = lambda data : (data[0], data[1]*83.03) # as of 19-03-2024

india_store = list(map(to_rupees, us_store))

print("US Store: " + str(us_store))
print()
print("India Store: " + str(india_store))
