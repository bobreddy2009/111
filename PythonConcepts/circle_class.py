import math
class Circle:
    radius = 0
    area = 0
    circumfrence = 0
    def __init__(self,radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def get_area(self):
        return (self.radius * self.radius) * math.pi
    def get_circumfrence(self):
        return (self.radius * 2) * math.pi
c1 = Circle(5)
print(c1.get_circumfrence())
print(c1.get_area())
print(c1.get_radius())