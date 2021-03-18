def number_triangle(x):
    num = 0
    multiply = 1
    for i in range(1, x + 1):
        num += 1
        print(num * multiply)
        multiply = multiply * 10 + 1


x = int(input("enter a number"))
number_triangle(x)






