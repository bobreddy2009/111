import math


def nth_perfect_number(n):
    i = 0
    perfect = []
    while True:
        if len(perfect) == n:
            return perfect
            break
        i += 1
        max_num = math.sqrt(i)
        l1 = [{n, i // n} for n in range(1, int(max_num + 1)) if i % n == 0]
        l2 = [l for my_tuple in l1 for l in my_tuple]
        sum1 = 0
        for k in l2:
            sum1 += k
        if i * 2 == sum1:
            perfect.append(i)


print(nth_perfect_number(4))
