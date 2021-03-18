class Employee:
    __salary = 0
    dob = ""
    address = ""
    name = ""
    city = ""
    def __init__(self,salary,dob,address,name,city):
        self.__salary = salary
        self.dob = dob
        self.address = address
        self.name = name
        self.city = city
class Engineer(Employee):
    expirience = 0
    def __init__(self,salary,dob,address,name,city,expirience):
        self.__salary = salary
        self.dob = dob
        self.address = address
        self.name = name
        self.city = city
        self.expirience = expirience
class Manager(Employee):
    email = ""
    def __init__(self, salary, dob, address, name, city, email):
        self.__salary = salary
        self.dob = dob
        self.address = address
        self.name = name
        self.city = city
        self.email = email
e1 = Employee(salary=100,dob="10/19/09",address="1890 somthingway", name="bob", city="New York")
ee1 = Engineer(salary=100,dob="10/19/09",address="9067 somethingblvd", city="San Francisco", name="Jeff", expirience=10000000000)
em1 = Manager(salary=100,dob="10/19/09",address="9067 somethingblvd", city="San Francisco", name="Jeff", email="Jeffy309@yahoo.com")



