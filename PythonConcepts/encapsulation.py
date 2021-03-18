# encapsulation protects your variables and methods
import random


class Zombie:
    name = ''
    legs = 0
    __eyes = 0
    weapons = ''
    size = 0

    def __init__(self, legs, eyes, weapons, size, name=None):
        if name == None:
            num = random.randint(1, 100)
            name = f"Z{num}"
        if eyes < 5:
            print("eyes CANNOT be less than 5")
            exit(0)
        self.name = name
        self.legs = legs
        self.__eyes = eyes
        self.weapons = weapons
        self.size = size
        print(f"ZOMBIE {name} CREATED")
    def __test(self):
        print("hello")
    def get_attributes(self):
        return f"name:{self.name}, legs:{self.legs}, eyes:{self.__eyes}, weapon:{self.weapons}, size:{self.size}"
z1 = Zombie(legs=10,eyes=7,weapons="grenade", size=3,name="jeff")
z1.__eyes = -100000000000000000
print(z1.__eyes)
print(z1.get_attributes())
z1.__test()
