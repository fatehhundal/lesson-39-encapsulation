class Shape:
    def area(self):
        return 0
    

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        print("Square area:", self.side ** 2, "cm²")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print("Circle area:", 3.14 * (self.radius ** 2), "cm²")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        print("Triangle area:", 0.5 * (self.base * self.height), "cm²")

s = Square(6)
c = Circle(15)
t = Triangle(12, 18)

for shape in (s, c, t):
    shape.area()