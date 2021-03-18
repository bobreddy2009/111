# first_class_functions
def addition(x, y):
    return x + y


print(addition)
z = addition
print(z(1, 2))


# MAP
def square(x):
    return x * x


def my_map(function, iterable):
    for item in iterable:
        yield function(item)


l1 = [1, 2, 3, 4]
o1 = my_map(square, l1)
print(o1)
print(list(o1))


def my_func():
    return square


z = square
print(my_func(), z)


def outer():
    print("executing outer")

    def inner():
        print("executing inner")
        return 10000

    return inner
z = outer()
#print(z)
print(z())
#closure
#closure-function which can acces the enclosing object even when it is not in memory
# for a closure you need:
# 1. a nested function
# 2. the nested function should reference the enclosing functions scope
# 3. the nested function should be returned by the enclosing function

def new_outer():
    outer_variable = "Hello World"
    def new_inner():
        return outer_variable
    return new_inner
z = new_outer()
print(z())
print("_____"*3)
def new_outer1(message):
    outer_variable = message
    def new_inner1(message1):
        return f"{message} {message1}"
    return new_inner1
z = new_outer1("hello")
print(z("world"))
t = new_outer1("new")
print(t("york"))
print("-------" * 3)
# purposes of Closure:
# 1.you can avoid using Global variables.
# 2. hide variables
# 3. implement decorators

def salute(my_salute):
    def get_message(name):
        return f"{my_salute}. {name}, welcome to python."
    return get_message
z = salute("Mr")
print(z("Jeff"))
print("-------" * 3)
my_salutes = ["Mr","Dr","Ms","Mrs"]
names = ["Jeff","Jack","Jill","Jillson"]
for my_salute,name in zip(my_salutes,names):
    z = salute(my_salute)
    print(z(name))

