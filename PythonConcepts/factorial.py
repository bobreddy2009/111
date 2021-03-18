def factorial (num):
    product = 1
    for i in range(1,num+1):
        product*=i
    yield product

print(next(factorial(4)))