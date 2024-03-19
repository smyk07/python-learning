class Animal: 
    def eat(self): 
        print("This animal is eating")

class Rabbit(Animal): 
    def eat(self): 
        print("This animal is eating a carrot")

rabbit = Rabbit()

rabbit.eat()

# the rabbit class over-wrote the eat class from the parent animal class. 