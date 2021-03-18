class Mammal:
    teeth = 0
    heart_chambers = 0
    legs = 0
    wings = 0
    animal = ""
    def __init__(self,teeth,heart_chambers, legs, animal,wings=0):
        self.teeth = teeth
        self.heart_chambers = heart_chambers
        self.legs = legs
        self.wings = wings
        self.animal = animal


    def can_fly(self):
        if self.wings > 0:
            return True
        else:
            return False
    def can_run(self):
        if self.wings == 0:
            return True
        else:
            return False
class Flying_mammals(Mammal):
    habitat = ""
    def __init__(self,teeth,heart_chambers,habitat,animal):
        habitats = ["arctic", "rainforest", "plains", "mountains", "caves", "desert"]
        self.teeth = teeth
        self.heart_chambers = heart_chambers
        if habitat in habitats:
            self.habitat = habitat
        else:
            print("error, not a valid habitat")
            exit(0)
        self.animal = animal
    def get_habiitat(self):
        return self.habitat
    def can_fly(self):
        return True
    def can_run(self):
        return False
m1 = Mammal(26,1,2,"human",0)
fm1 = Flying_mammals(26,1,"caves","bat")
print(m1.can_fly())
print(fm1.can_run())

