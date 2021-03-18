def sort_things(x):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    lowercase = []
    uppercase = []
    numbers = []
    output = ""
    for i in x:
        if i in abc:
            lowercase.append(i)
        elif i.lower() in abc:
            uppercase.append(i)
        try:
            ints = int(i)
            numbers.append(i)
        except:
            pass

    lowercase.sort()
    uppercase.sort()
    numbers.sort()
    output += "".join(lowercase)
    output += "".join(uppercase)
    output += "".join(numbers)
    return output


print(sort_things("AxYl18ab"))
