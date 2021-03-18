
def oddish_vs_evenish(x):
        x_str = str(x)
        list = []
        list.extend(x_str)
        sums = 0
        for i in list:
            if int(i) != 0:
                i = int(i)
                sums+=i
        if sums % 2 == 0:
            return "EVENISH"
        else:
            return "ODDISH"

print(oddish_vs_evenish(int(input("enter a number"))))