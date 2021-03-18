import random
import os


class Employment:
    base_salary = 0
    name = ''
    city = ''
    type = ''
    bonus = 0

    def __init__(self, base_salary, city, type, name=None):
        if name == None:
            abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
            length = random.randint(10, 20)
            name = []
            for num in range(length):
                random_letter = abc[random.randint(0, 25)]
                name.append(random_letter)
            name = "".join(name)
        self.name = name
        self.city = city
        self.base_salary = base_salary
        if type.lower() == "engineer" or type.lower() == 'manager':
            self.type = type
        else:
            print("type is wrong")
            exit(1)

    def get_employee_details(self):
        return self.base_salary, self.name, self.type

    def get_employee_city(self):
        return self.city

    def get_employee_bonus(self):
        if self.type.lower() == 'engineer':
            self.bonus = self.__calc_bonus(5)
        else:
            self.bonus = self.__calc_bonus(3)
        return self.bonus
    def __calc_bonus(self, percent):
        self.bonus = self.base_salary * percent
        return self.bonus



employee_1 = Employment(base_salary=1000, city='San Francisico', type='manager')
home_dir = 'C:/Users/avane/Documents/dummy'
os.chdir(home_dir)
with open('emp_details.txt', 'w') as f:
    print(employee_1.get_employee_bonus(), file=f)
    print(employee_1.get_employee_city(), file=f)
    print(employee_1.get_employee_details(), file=f)

print(employee_1.get_employee_bonus())
print(employee_1.get_employee_city())
print(employee_1.get_employee_details())
