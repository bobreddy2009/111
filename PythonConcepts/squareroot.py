import math
def square_root(x):
    primes = []
    l = x+1
    for i in range(x*x,l*l):
        factors = []
        y = int(math.sqrt(i)) + 1
        for m in range(2, y):
            if i % m == 0:
                factors.append(m)
        if not factors:
            primes.append(i)
    return primes

print(square_root(5))