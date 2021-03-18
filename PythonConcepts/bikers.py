import re
search_string = "Bob-Bike,Jeff - Walk,Jill - Bike,Jack - Car"
my_string = ".+ - Bike"
pattern = re.compile(my_string)
bikers = pattern.findall(search_string)
for person in bikers:
    person = str(person)
    person = person.split(",")
    for people in person:
        pasrts = people.split("-")
        print(pasrts[0])
