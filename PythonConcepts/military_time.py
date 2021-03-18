def converter(x):
    if x[-3] == "a":
        no_am = [i for i in x if i != "a" and i != "m" and i != "."]
        return "".join(no_am)

    else:
        no_pm = [i for i in x if i != "p" and i != "m" and i != "."]
        y = "".join(no_pm)
        l = y.split(":")
        chang = int(l[0])
        chang += 12
        chang = str(chang)
        final = [chang,":",l[1]]
        return "".join(final)

print (converter("8:20 p.m"))