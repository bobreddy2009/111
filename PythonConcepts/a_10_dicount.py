def groceries1(x):
    for i in x:
        for l in i:
            if l == "a" or l=="A":
                x[i] = x.get(i) * 0.9

    return x
print(groceries1({"apple":2.50,"cherry":4.35,"Lemon":2.85,"Mango":1.50}))


"""def groceries(x):
    a = {}
    for i in x:
        for l in i:
            if l == "a" or l == "A":
                a[i] = x.get(i)
                break
    for j in a:
        a[j] = a.get(j) * 0.9
    for y in a:
        x[y] = a.get(y)
    return x
x = {"apple": 2.50, "cherry": 4.35, "Lemon": 2.85, "Mango": 1.50}
print(groceries(x))"""