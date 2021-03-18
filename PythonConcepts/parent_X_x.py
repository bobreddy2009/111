def Xx (x):
    count = 0
    for i in x:
        if i == "x":
            count += 1
        elif count > 0 and i == "X":
            count -= 1

    if count == 0:
        return "good str"
    else:
        return "bad str"

print(Xx("abxsiXlx"))
