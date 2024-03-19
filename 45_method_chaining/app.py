class Car: 
    
    def turn_on(self): 
        print("The engine has been started")
        return self
        
    def drive(self): 
        print("The car is now driving")
        return self
        
    def stop(self): 
        print("The car has now stopped")
        return self
        
    def turn_off(self): 
        print("The engine has been turned off")
        return self

car_1 = Car()
car_2 = Car()

car_1.turn_on().drive().stop().turn_off()
car_2.turn_on().turn_off()