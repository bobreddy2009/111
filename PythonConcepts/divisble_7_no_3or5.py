def divisble_7(num):
    n = 0
    divisibility = []
    while True:
        n+=1
        if len(divisibility) == num:
            break
        if n%3 == 0 or n%5 == 0:
            pass
        elif n%7 == 0:
            divisibility.append(n)
            yield n

y = divisble_7(8)
for i in y:
    print(i)
