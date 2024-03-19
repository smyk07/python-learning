class Prey: 
    def flee(self): 
        print("This animal is now fleeing")

class Predator: 
    def hunt(self): 
        print("This animsl is now hunting")

class Rabbit(Prey): 
    pass

class Hawk(Predator): 
    pass

class Fish(Predator, Prey): 
    pass

rabbit = Rabbit() # can only flee
hawk = Hawk() # can only hunt
fish = Fish() # can flee and hunt 