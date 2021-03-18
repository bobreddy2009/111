import math
x = 8
y = int(math.sqrt(x)) + 1
factors = False
alreday_prime = False
for i in range(2,y):
        if x % i == 0:
                factors = True
                break
        if not factors:
            print(x)
            alreday_prime = True
if not alreday_prime:
    lower = 0
    higher = 0
    lower_bool = False
    higher_bool = False
    j = x
    l = x
    m = True
    while m:
        j+=1
        y = int(math.sqrt(j)) + 1
        for i in range(2, y):
            if j % i == 0:
                lower_bool = True
                break
            if not lower_bool:
                higher += j
                m = False
                break
    l = x
    k = True
    while k:
        l -= 1
        y = int(math.sqrt(l)) + 1
        for i in range(2, y):
            if l % i == 0:
                higher_bool = True
            if not higher_bool:
                lower += l
                k = False
                break
    one = abs(x - higher)
    two = abs(x-lower)
    if one>two:
        print(higher)
    else:
        print(lower)

