import random
class Zombie:
    name = ''
    legs = 0
    eyes = 0
    weapons = ''
    size = 0
    def __init__(self,legs,eyes,weapons,size,name=None):
        if name == None:
            num = random.randint(1,100)
            name = f"Z{num}"
        if eyes < 5:
            print("eyes CANNOT be less than 5")
            exit(0)
        self.name = name
        self.legs = legs
        self.eyes = eyes
        self.weapons = weapons
        self.size = size
        print(f"ZOMBIE {name} CREATED")

    def get_attributes(self):
        return f"name:{self.name}, legs:{self.legs}, eyes:{self.eyes}, weapon:{self.weapons}, size:{self.size}"


d1 = Zombie(name="Bob",legs=5,eyes=1,size=3,weapons="gun")
# print(d1.eyes)
#d1.eyes = 7
#d1.name = "Bob"
#d1.legs = 5
#d1.size = 3
#d1.weapons = "gun"

d2 = Zombie(legs=2,eyes=100,size=2,weapons="knife")
# print(d2.eyes)
#d2.name = "Jeff"
#d2.legs = 2
#d2.size = 2
#d2.weapons = "knife"
print(d1.get_attributes())
print(d2.get_attributes())
