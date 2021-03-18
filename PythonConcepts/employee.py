class Employee:
    name = ""
    email = ""
    base_salary = 0
    years = 0
    __type = ""
    bonus = 0
    def __init__(self,name,email,base_salary,years,type):
        types = ("engineer","manager", "executive")
        if type not in types:
            print("Not a valid type")
            exit(1)
        else:
            self.__type = type
        self.name = name
        self.email = email
        self.base_salary = base_salary
        self.years = years
        self.bonus = self.__calc_bonus()
    def __calc_bonus(self):
        if self.__type == "engineer":
            if self.years > 15:
                years = 15
            else:
                years = self.years
            return years * (2/100) * self.base_salary
        elif type == "manager":
            if self.years > 10:
                years = 10
            else:
                years = self.years
            return years * (2/100) * self.base_salary
        else:
            return (3/100) * self.base_salary
    def get_bonus(self):
        return self.bonus
z1 = Employee(name="Avaneesh",email="something", base_salary=100000000, years=20,type="manager")
print(z1.get_bonus())

print(z1.years)

