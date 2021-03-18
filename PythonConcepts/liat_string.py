def remover_string_list(string,list):
    for letter in string:
        if letter in list:
            list.remove(letter)
    return list
print(remover_string_list("bullet",["b","u","r","s"]))