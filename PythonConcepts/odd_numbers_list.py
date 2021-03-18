import functools
l1 = [1,2,3,4,5,6,7,8,9,10]

x = filter(lambda a:a%2==1,l1)
print(len(list(x)))