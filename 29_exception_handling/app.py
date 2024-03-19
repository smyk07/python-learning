try: 
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by"))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e) 
    print("Can't Divide by zero")
except ValueError as e:
    print(e) 
    print("Enter only numbers please")
except Exception as e:
    print(e) 
    print("Something Went Wrong :O")
else: 
    print(result)
finally: 
    print("Byee...") # this will always execute