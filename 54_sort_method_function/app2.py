students = [
    ("Squidward", "F", 60), 
    ("Sandy", "A", 33), 
    ("Patrick", "D", 36), 
    ("Spongebob", "B", 20), 
    ("Mr. Krabs", "C", 78)
]

# (Name ---- Grade ---- Attendance)

names = lambda names : names[0]
grade = lambda grades : grades[1]
attendance = lambda attendance : attendance[2] 

students.sort(key=attendance, reverse=True)

for i in students: 
    print(i)
