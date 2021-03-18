def unique_letters(string):
    splitted = string.split()
    for i in splitted:
        sets = set(i)
        final = list(sets)
        final.sort()
        check = []
        for letter in i:
            check.append(letter)
        check.sort()
        if final == check:
            pass
        else:
            return False
    return True

print(unique_letters("Hi bob"))