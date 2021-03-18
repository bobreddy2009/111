import random
class Student:
    name = ""
    age = 0
    marks = 0
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
a1 = Student(name="bob",age=10,marks=96)
b1 = Student(name="jeff",age=11,marks=90)
c1 = Student(name="joe",age=12,marks=89)
d1 = Student(name="jill",age=13,marks=88)
e1 = Student(name="jack",age=9,marks=84)
f1 = Student(name="f1",age=100,marks=10)
g1 = Student(name="g1",age=101,marks=100)
a2 = Student(name="a2",age=134,marks=67)
a3 = Student(name="a3",age=145,marks=69)
a4 = Student(name="a4",age=13,marks=91)
num = random.randint(1,3)
if num == 1:
    l1 = [a1.name,b1.name,c1.name,d1.name,e1.name,f1.name,g1.name,a2.name,a3.name,a4.name]
elif num == 2:
    l1 = [a1.age, b1.age, c1.age, d1.age, e1.age, f1.age, g1.age, a2.age, a3.age, a4.age]
elif num == 3:
    l1 = [a1.marks, b1.marks, c1.marks, d1.marks, e1.marks, f1.marks, g1.marks, a2.marks, a3.marks, a4.marks]
l1.sort()
print(l1)