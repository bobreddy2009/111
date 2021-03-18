
def decode_the_string(coded_string,vowels):
    output = ""
    value = 0
    for i in coded_string:
        if i == "?":
            output += vowels[value]
            value+=1
        else:
            output+=i

    return output

print(decode_the_string("st??m ?ng?n?", "eaeie"))