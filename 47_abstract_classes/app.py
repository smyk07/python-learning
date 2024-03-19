from abc import ABC, abstractmethod

class Vehicle(ABC): 
    @abstractmethod # this prevents the user from creating an object of this class
    def go(self): 
        pass
    
    @abstractmethod
    def stop(self): 
        pass

class Car(Vehicle): 
    def go(self): 
        print("The car is now on")
        
    def stop(self): 
        print("The car is now off")

class Motorcycle(Vehicle): 
    def go(self): 
        print("The motorcycle is not on")
    
    def stop(self): 
        print("The motorcycle is now off")

# vehicle = Vehicle() # cant create due to vehicle being abstract class
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()