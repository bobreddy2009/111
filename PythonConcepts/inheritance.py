class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width
    def get_perimeter(self):
        return (self.length + self.width) * 2
class Square:
    def __init__(self,side):
        self.side = side
    def get_area(self):
        return self.side ** 2
    def get_perimeter(self):
        return self.side * 4
class Child_square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
    def get_area(self):
        return "Hello WORLD"
r1 = Rectangle(100,100)
print(r1.get_area())
print(r1.get_perimeter())
s1 = Square(100)
print(s1.get_area())
print(s1.get_perimeter())
cs1 = Child_square(100)
print(cs1.get_area())
print(cs1.get_perimeter())
