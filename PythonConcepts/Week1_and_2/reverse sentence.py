def reverse_sentence(x):
    l = x.split()
    output = []
    y = 0
    for i in l:
        y-=1
        output.append(l[y])
    return " ".join(output)
print(reverse_sentence("what is my name"))

