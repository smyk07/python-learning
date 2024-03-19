class Duck: 
    def __init__(self, name): 
        self.name = name
    def walk(self): 
        print(self.name + " the duck is walking")
    def talk(self): 
        print(self.name + " the duck is quacking")
    def caught(self, name): 
        print(self.name + " the chicken got caught by " + name)

class Chicken: 
    def __init__(self, name): 
        self.name = name
    def walk(self): 
        print(self.name + " the chicken is walking")
    def talk(self): 
        print(self.name + " the chicken is clucking")
    def caught(self, name): 
        print(self.name + " the chicken got caught by " + name)

class Person: 
    def __init__(self, name): 
        self.name = name
    def walk(self): 
        print("The person is walking")
    def talk(self): 
        print("The human is walking")
    def catch(self, animal): 
        animal.walk()
        animal.talk()
        animal.caught(self.name)
        # what duck typing does it it allows any animal object class to be caught as long as it has the same methods XD (walk, talk, caught)
        

# duck = Duck("Harry")
chicken = Chicken("Rattlehead")
samyak = Person("Samyak")

# samyak.catch(duck)
samyak.catch(chicken)