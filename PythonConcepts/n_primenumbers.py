import math
def n_primenumbers(num):
    primes = {}
    primes = set(primes)
    n = 1
    while True:
        if len(primes) == num:
            break
        n += 1
        factors = []
        y = int(math.sqrt(n)) + 1
        for i in range(2,y):
            if n % i == 0:
                factors.append(i)
        if not factors:
            primes.add(n)
            yield n

x = 8
y = n_primenumbers(x)
for i in y:
    print(i)


