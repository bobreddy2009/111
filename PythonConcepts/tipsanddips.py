def tips_dips(x):
    y = [i for i in x]
    y.sort()
    z = [i for i in x]
    if y == x:
        return "dips"
    else:
        x.sort(reverse=True)
        if z == x:
            return "tips"

print(tips_dips([10,20,30]))
