import functools
x = 4
l1 = [i for i in range(1,x+1)]
sum = 0
def multiply(x,y):
    return x*y
l2 = functools.reduce(multiply,l1)
print(l2)
