# not all rules are included
def pig_latin(x):
    vowels = ("a","e","i","o","u")
    pig = []
    l = x[0]
    pig.extend(x)
    pig.append(l)
    pig.remove(l)
    if pig[-1] in vowels:
        pig.append("way")
    else:
        pig.append("ay")

    return "".join(pig)

print(pig_latin("art"))

