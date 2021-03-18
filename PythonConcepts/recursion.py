# a function that calls itself
def x():
    print("start of x")
    x()
    print("end of x")


"""def y ():
    print("start of y")
    z()
    print("end of y")
def z ():
    print("start of z")
    #z()
    print("end of z")"""


# x()
def factorial(n):
    product = 1
    for num in range(2, n + 1):
        product *= num
    return product


# print(factorial(10000))
# factorial of 5 = 5*4*3*2*1
# factorial of 4 = 4*3*2*1
def r_factorial(n):
    if n == 1:
        return 1
    else:
        return n * r_factorial(n - 1)


# print(r_factorial(996))
fibo_cache = {}
def r_fibonoci(n):
    if n in fibo_cache:
        return fibo_cache.get(n)
    else:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            value = r_fibonoci(n - 1) + r_fibonoci((n - 2))
            fibo_cache[n] = value
            return value
# 1,1,2,3,5,8,13,21,
# print(r_fibonoci(31))
#for i in range(1,100):
#    print(f"fibonoci of {i} is {r_fibonoci(i)}")
# memoization
import functools

@functools.lru_cache()
def r_fibbonoci_internal_cache(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return r_fibbonoci_internal_cache(n - 1) + r_fibbonoci_internal_cache(n - 2)
for i in range(1,10000):
   print(f"fibonoci of {i} is {r_fibbonoci_internal_cache(i)}")