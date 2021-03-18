def floyds_triangle(x):
    num = 0
    values_line = 0
    for i in range(1, x + 1):
        values_line += 1
        for j in range(1, values_line + 1):
            num += 1
            l = str(num) + " "
            print(end = l)
        print("\r")


x = int(input("enter a number"))
floyds_triangle(x)
