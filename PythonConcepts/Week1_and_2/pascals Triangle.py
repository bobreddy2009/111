try:
    x = int(input("enter a number"))
    one = "1"
    two = "1 1"
    if x > 0:
        print(one.center(100))
        if x > 1:
            print(two.center(100))
            old_digits = ["1", "1"]
            new_digits = ["1"]
            for i in range(2, x):
                for index, j in enumerate(old_digits):
                    try:
                        y = str(int(j) + int(old_digits[index + 1]))
                        new_digits.append(y)
                    except:
                        new_digits.append("1")
                        y = " ".join(new_digits)
                        print (y.center(100))
                        old_digits.clear()
                        for y in new_digits:
                            old_digits.append(y)
                        new_digits.clear()
                        new_digits.append("1")
                        break
except:
    print ("integer please")




