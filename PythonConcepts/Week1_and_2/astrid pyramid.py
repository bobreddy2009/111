def pyramid(x):
    a = "*"
    one = 1
    for i in range(1, x):
        l = a * one
        print(l.center(100))
        one += 2


x = int(input("enter a number:"))
pyramid(x)


def inverse(x):
    a = "*"
    l = x + (x - 1)
    for i in range(1, x + 1):
        print(str(l * a).center(100))
        l -= 2


inverse(x)