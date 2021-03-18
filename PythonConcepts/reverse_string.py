x = "Hello, My name is Bob."
def period_or_not(letter):
    if letter == '.' or letter == ' ':
        return letter
    else:
        return '#'
def rev(string):
    reverse_list = [period_or_not(letter) for letter in string]
    """for letter in string:
        if letter == "." or letter == " ":
            reverse_list.append(letter)
        else:
             reverse_list.append('#')"""
    reverse_string = string[::-1]
    index = 0
    for i in reverse_string:
        if i == "." or i == ' ':
            continue
        if string[index] == "." or string[index] == ' ':
            index += 1
        if string[index].isupper():
            reverse_list[index] = i.upper()
        else:
            reverse_list[index] = i.lower()
        index+=1
    return "".join(reverse_list)
print(x)
print(rev(x))
