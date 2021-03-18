import itertools
def greeting (name = "Joe",prefix = "Mr."):
    print(f"hello {prefix} {name}, welcome to python class")
greeting("avaneesh","master")
greeting()
greeting(prefix="Dr.")
greeting("avaneesh")
#greeting(prefix="master","avaneesh") <- error
greeting("avaneesh",prefix="master")
def order_fan (manufacturur = "ge",blades = 4,voltage = 120, color = "gray"):
    print(f"you ordered a fan with  from manufacturur {manufacturur}, with {blades} blades, with a voltage of {voltage} and a color of {color}")

order_fan("samsing",5,color="black")
def addition(*x):
    print(x)
    sum=0
    for i in x:
        sum+=i
    return sum
print(addition(1,2,3,4,5,6,7,8,9,10))
def my_fumction(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
my_fumction(a=1,b=2,c=3,d=4)
def city_temp(cites,temps):
#    my_dict = {}
#    for index,i in enumerate(cites):
#        my_dict[i] = temps[index]
    my_dict = {city:temp for city,temp in zip(cites,temps)}
    return my_dict
cities = ['Austin','New York', 'Los Angeles']
temp = [101,87,95]
print(city_temp(cities,temp))
def name_age(f,l,a):
    my_dict = {first+" "+last:age for first,last,age in zip(f,l,a)}
    return my_dict
first = ["bob","jack","jill"]
last = ["smith","sack","bill"]
age = [50,60,30]
print(name_age(first,last,age))



first = ["bob","jack","jill"]
last = ["smith","sack","bill"]
age = [50,60,30]
my_dict = {}
l1 = "123"
permutations = [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]
p = itertools.permutations(l1)
p = list(p)
for i in p:
    print("".join(i))

def q10(my_str):
    tot_words = my_str.count(" ") + 1
    uc_set = {i for i in my_str if i.isalnum()}
    return tot_words,len(uc_set)
print(q10("Today 7th is mid-day"))

































