import itertools
import statistics
a = lambda x, y: x + y
print(a(2, 3))
def my_func(x):
    return lambda a: a**x

square = my_func(2)
cube = my_func(3)
print(square(5))
print(cube(5))

radii = [1,2,3,4.5,6]
area = [i*i*3.14 for i in radii]
print(area)
#map(function,iterable)
#function(iterable)

def area1(r):
    return r*r*3.14
ar = list(map(area1,radii))
print(ar)
ar1 = list(map(lambda r: r*r*3.14, radii))
print(ar1)
area = [area1(i) for i in radii]
print(area)


def f_to_c(f):
    c = round((f[1] - 32) * 5 / 9, 2)
    return (f[0],c)


temps1 = [("San Fransisco", 100), ("austin", 106), ("New York", 87), ("dallas", 104)]
# list_comprehension
celcius = [f_to_c(i) for i in temps1]
print(celcius)
celcius_map = map(f_to_c,temps1)
print(list(celcius_map))
celcius_map_lambda = map(lambda f: (f[0],round((f[1] - 32) * 5 / 9, 2)), temps1)
print(list(celcius_map_lambda))
#filter(function,list)
student_marks=[50,60,99,77,10,45,80]
pass_fail = [score for score in student_marks if score > 59]
print(pass_fail)
def my_pass_fail (x):
    if x > 59:
        return x
    else:
        return None
x = filter(my_pass_fail,student_marks)
print(list(x))

pass_fail_lambda = filter(lambda x: x>59, student_marks)
print(list(pass_fail_lambda))
cities = ["austin","san ramon",None,"","san fransico","new york"]
print(list(filter(None,cities)))

