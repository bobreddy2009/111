def alpha_diamond(x):
    y = x - 1
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    print(abc[y])
    for i in range(y):
        y = x - 1
        print(end=abc[y])
        for j in range(int((i+1)/2 + 1)):
            y-=1
            print(end=abc[y])
        for l in range(int((i+1)/2 + 1)):
            y+=1
            print(end=abc[y])

        y = x-1


        print("\r")
    y = x-1
    for i in range(1,x-1):
        pass
    print(abc[x-1])
alpha_diamond(3)

for i in range(97,97+26):
    print(chr(i))
for j in range(65, 65+26):
    print(chr(j))
