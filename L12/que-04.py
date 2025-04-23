import math

class RegularShape:
    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Square(RegularShape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side * self.side

class Rectangle(RegularShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

class Circle(RegularShape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius

# Test code
square = Square(4)
rectangle = Rectangle(5, 3)
circle = Circle(2)

print("Square Perimeter:", square.perimeter())
print("Square Area:", square.area())
print("Rectangle Perimeter:", rectangle.perimeter())
print("Rectangle Area:", rectangle.area())
print("Circle Circumference:", circle.perimeter())
print("Circle Area:", circle.area())
