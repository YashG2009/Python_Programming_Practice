import math

class Solid:
    def surface_area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def volume(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cube(Solid):
    def __init__(self, side):
        self.side = side

    def surface_area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side ** 3

class Sphere(Solid):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius * self.radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Cylinder(Solid):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius * self.radius * self.height

# Test code
cube = Cube(3)
sphere = Sphere(4)
cylinder = Cylinder(2, 5)

print("Cube Surface Area:", cube.surface_area())
print("Cube Volume:", cube.volume())
print("Sphere Surface Area:", sphere.surface_area())
print("Sphere Volume:", sphere.volume())
print("Cylinder Surface Area:", cylinder.surface_area())
print("Cylinder Volume:", cylinder.volume())
