from car import Car

car_1 = Car("Tesla", "Series Y", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2023, "Red")

car_1.wheels = 6 # changing a class variable's value

print(car_1.wheels)

# ------------------------

Car.wheels = 2 # this will affect all instances 
print(Car.wheels) # can also access the class to view the default value
