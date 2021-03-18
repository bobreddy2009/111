def type_1(*args):
    types = []
    for i in args:
        x = type(i)
        types.append(x)
    return types


print(type_1(1, "bob", 1.1, True, [1, 2], (1, 2), {1, 2}, {1: 2},))



