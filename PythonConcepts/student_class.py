import re
class Student:
    name = ''
    marks = 0
    major = ''
    def __init__(self,name,marks,major):
        self.name = name
        self.major = major
        self.marks = marks
    def get_student_marks(self):
        if 100 >= self.marks >= 30:
            return self.marks
        else:
            print("error marks not in between 30 and 100")
            exit(1)
    def get_student_major(self):
        major_list = ['physics', 'math', 'history', 'chemistry', 'english']
        if self.major.lower() in major_list:
            return self.major
        else:
            print("error, major is not a valid major")
            exit(1)
    def get_student_name(self):
        my_string = "[A-Z][a-z]{4}[a-z]*,[A-Z][a-z]{4}[a-z]*"
        pattern = re.compile(my_string)
        match = pattern.match(self.name)
        if match:
            return self.name
        else:
            print("Error, name is not in correct format")
            exit(1)

student_1 = Student(name="Dammanagari,Avaneesh",major='Math',marks=100)
print(student_1.get_student_major())
print(student_1.get_student_name())
print(student_1.get_student_marks())
