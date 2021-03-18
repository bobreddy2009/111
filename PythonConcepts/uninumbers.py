x = 4
while True:
    digits = []
    squares = []
    sum = 0
    for digit in str(x):
        digits.append(int(digit))
    for d in digits:
        squares.append(d*d)
    for i in squares:
        sum += i
    x = sum
    print(x)
    if x == 1:
        print("Uni-number! :D TRUE")
        break
    elif x == 4:
        print("Non-Uni-number D:  FALSE")
        break

