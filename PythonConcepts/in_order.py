def in_order(string):
    alpha = [chr(i) for i in range(97,97+26)]
    index_before = 0
    for i in string:
        for index,l in enumerate(alpha):
            if l == i:
                current_index = index
        if current_index < index_before:
            return ""
        elif current_index > index_before:
            index_before = current_index

    return string
x = ["like","same","allow","abcdez"]
output = map(in_order, x)
output = list(output)
final = [i for i in output if i != ""]
print(final)


