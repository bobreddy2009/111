import math
def improved_factors (n):
    max_num = math.sqrt(n)
    l1 = [{i, n//i} for i in range(1, int(max_num+1)) if n % i == 0]
    print(l1)
    l2 = [i for my_tuple in l1 for i in my_tuple]
    l2.sort()
    return l2
n = 70
print(improved_factors(n))