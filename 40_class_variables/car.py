class Car: 
    
    wheels = 4 # this is a class variable, being default for all cars.
               # bikes will always have 2 wheels, cars will always have 4 wheels
               # can be set to a default value, and can be changed later
    
    def __init__(self, make, model, year, color): 
        self.make = make # these are instance variables
        self.model = model
        self.year = year
        self.color = color
