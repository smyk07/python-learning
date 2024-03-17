# set = collection which is unordered, unindexed, no duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils)
dinner_table = utensils.union(dishes) # or the other way around
print(dishes.diffference(utensils))
print(utensils.intersection(dishes))

for i in utensils: 
    print(i)
    
for i in dishes: 
    print(i)