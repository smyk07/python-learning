# tuple is a list which is ordered and unchangeable

student = ("Bro", 21, "male")

print(student)
print(student.count("Bro"))
print(student.index("male"))

for x in student: 
    print(x)
    
if "Bro" in student: 
    print("Bro is here")