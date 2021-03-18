import random


# EAFP - it is EASY to ASK for FORGIVENESS than PERMISSION
#function overloading is not supported in Python line 24
#operator overloading
class Gun:
    def fight(self):
        print("Bang Bang Bang")


class Sword:
    fight = "hi"

    def fight1(self):
        print("swish swish swish")


class Zombie:
    name = ''
    legs = 0
    eyes = 0
    weapon = ''
    size = 0
    """def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c"""
    def __init__(self, legs, eyes, weapon, size, name=None):
        if name is None:
            num = random.randint(1, 100)
            name = f"Z{num}"
        if eyes < 5:
            print("eyes CANNOT be less than 5")
            exit(0)
        self.name = name
        self.legs = legs
        self.eyes = eyes
        self.weapon = weapon
        self.size = size
        print(f"ZOMBIE {name} CREATED")

    def use_weapon(self):
        try:
            self.weapon.fight()
        except AttributeError as e:
            print(e)
        except TypeError as t:
            print(t)

        """if hasattr(self.weapon, 'fight'):
            if callable(self.weapon.fight):
                self.weapon.fight()
            else:
                print("Cannot exucute fight attribute")
        else:
            print("Error, class has no attribute fight")"""
    def __add__(self, other):
        legs = self.legs + other.legs
        eyes = self.eyes + other.eyes
        size = self.size + other.size
        z = Zombie(legs=legs,eyes=eyes,weapon=self.weapon,size=size)
        return z
    def get_attributes(self):
        return f"name:{self.name}, legs:{self.legs}, eyes:{self.eyes}, weapon:{self.weapon}, size:{self.size}"


g1 = Gun()
d1 = Zombie(name="Bob", legs=5, eyes=6, size=3, weapon=g1)
print(d1.get_attributes())
#print(d1.add(1,3))
d1.use_weapon()
s1 = Sword()
d2 = Zombie(legs=2, eyes=100, size=2, weapon=s1)
print(d2.get_attributes())
d2.use_weapon()

x = 10
y = 20
a = "123"
b = "456"
print(a+b)
print(a.__add__(b))
print(x+y)
z = d1+d2
print(z.get_attributes())
