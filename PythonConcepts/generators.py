import sys
import resource
from Week3.password_generator import generater_1 as get_name
import random


def my_generator(my_list):
    for element in my_list:
        yield element


x = [1, 2, 3, 4, 5]
y = my_generator(x)
for i in y:
    print(i)
# for i in range(5):
#       print(next(y))
print("-----" * 3)
"""def square (x):"
 "    for i in x:"
 "        yield i * i"
 "x = [1,2,3,4]]"
 "y = square(x)"
 "for i in y:"
 "    print(i)"""
x = [1, 2, 3, 4]
squares = (i * i for i in x)
for i in squares:
    print(i)
print("-----" * 3)

x = (i for i in [61, 83, 44, 71, 5])
print(x)
print(list(x))
print(x)
print(list(x))

print("-----" * 3)
# fibbonoci
"""n = int(input("enter number:"))


def fibonacci():
    v = 0
    a = 1
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        print(v)
    elif n == 1:
        print(b)
    elif n == 2:
        print(b)
    else:
        print(b)
        print(b)
        for c in range(2, n):
            c = a + b
            print(c)
            a = b
            b = c

def gen_fibbonoci(n):
    first = 0
    second = 1
    for i in range(n):
        yield first
        first,second = second,first+second
f = gen_fibbonoci(20)
for i in f:
    print(i)
print("-----" * 3)
"""


def mem_usage():
    base_mem = 1024.
    if sys.platform == 'darwin':
        base_mem = base_mem * base_mem
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / base_mem
    return int(mem)


x = f"memory usage : {mem_usage()} Mb"
print(x)
print(get_name(10))


def get_marks():
    return random.randint(50, 100)


def get_student_list(n):
    students = []
    for i in range(n):
        student = {"id": i, "name": get_name(10), "marks": get_marks()}
        students.append(student)
    return students


def get_student_gen(n):
    for i in range(n):
        student = {"id": i, "name": get_name(10), "marks": get_marks()}
        yield student


s = get_student_gen(100000)
for i in s:
    i = i
x = f"memory usage : {mem_usage()} Mb"

print(x)
