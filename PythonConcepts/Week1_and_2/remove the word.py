def remove_the_word(x,y):
    output = []
    for i in x:
            if i not in y:
                output.append(i)
    return output

print(remove_the_word(["b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))





