import math

def perfect_squares(x,y):
    perfect = []
    if x < y:
        for i in range(x,y):
            l = math.sqrt(i)
            if l == int(l):
                perfect.append(i)

    else:
        for i in range (y,x):
            l = math.sqrt(i)
            if l == int(l):
                perfect.append(i)



    return perfect
print (perfect_squares(1,101))

