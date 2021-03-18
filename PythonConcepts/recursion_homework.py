import functools
@functools.lru_cache()
def square(n):
    if len(str(n)) > 1:
        return square(str(n)[0]) + square(str(n)[1])
    else:
        return int(n) * int(n)
print(square(26))
#12 = 1 * 1 + 2 * 2


def sum(l1):
    x = l1[-1]
    if len(l1) < 2:
        return l1[0]
    else:
        new_l1 = [i for i in l1 if i != x]
        return sum(new_l1) + x

print(sum([1,2,3,4,5,6]))
#1,2,3,4,5,6 = 1,2,3,4,5 + 6





