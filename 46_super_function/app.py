class Rectangle: 
    def __init__(self, length, width): 
        self.length = length
        self.width = width
    
    def area(self): 
        return self.length * self.width
    
    def perimeter(self): 
        return 2*self.width + 2*self.length

class Square(Rectangle): 
    def __init__(self, length): 
        super().__init__(length, length)

class Cube(Square): 
    def surface_area(self): 
        return self.area() * 6
    
    def volume(self): 
        return self.area() * self.length

square = Square(9)
print(square.perimeter())
print(square.area())

# ------------------------------------

cube = Cube(10)
print(cube.surface_area())
print(cube.volume())