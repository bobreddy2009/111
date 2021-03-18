import random

x = random.randint(0, 100)


def guess_number(x):
    points = 0
    for i in range(0, 5):
        y = int(input("guess the number"))
        if y == x:
            points += 10
            break
    else:
        for i in range(0, 5):
            y = int(input("guess the number"))
            if y == x:
                points += 5
    if points == 0:
        return f"you lose, the answer is {x}"
    else:
        return f"you got {points} points, the answer is {x}"


print(guess_number(x))
