# list comprehension is a way to create a new list with less syntax
#                    - can mimic certain lambda finctions, easier to read
#                    - list = [expression for item in iterable]

squares = []

# for i in range(1, 11): 
#     squares.append(i * i)

squares = [i * i for i in range(1, 11)]

print(squares) 

# -----------------------------

students = [100, 92, 73, 43, 54, 23, 94, 38, 74, 28]

passed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)

# ------------------------------