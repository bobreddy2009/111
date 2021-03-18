import random
def generater_1 (n):
    if n < 3:
        return "Too small for password"
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    password = ""
    x = random.randint(0,25)
    password += letters[x].upper()
    y = random.randint(0, 25)
    password += letters[y]
    l = random.randint(0, 8)
    password += numbers[l]
    for i in range(3,n):
        x = random.randint(1,3)
        if x == 1:
            y = random.randint(0, 25)
            password += letters[y]
        elif x == 2:
            y = random.randint(0, 25)
            password += letters[y].upper()
        else:
            l = random.randint(0, 8)
            password += numbers[l]


    return password
print(generater_1(1))