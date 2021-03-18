def factors(x):
    the_multiples = []
    for i in range(1, int(x / 2 + 1)):
        if x % i == 0:
            the_multiples.append(str(i))

    the_multiples.append(str(x))
    if len(the_multiples) == 2:
        print("prime number")
    return ",".join(the_multiples)


x = int(input("enter a number:"))
print(factors(x))


def GCF(x, y):
    x_multipls = []
    y_multiples = []
    GF = 1
    for i in range(1, int(x / 2 + 1)):
        if x % i == 0:
            x_multipls.append(i)
    for j in range(1, int(x / 2 + 1)):
        if y % j == 0:
            y_multiples.append(j)
    for l in x_multipls:
        if l in y_multiples:
            GF = l
    return GF


print(GCF(20, 15))


def LCM(x, y):
    j = x - 1
    LM = 0
    while True:
        j += 1
        if j % y == 0 and j % x == 0:
            LM = j
            break
    return LM


print(LCM(20, 15))
