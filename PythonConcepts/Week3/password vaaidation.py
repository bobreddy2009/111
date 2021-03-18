def validation(n):
    if len(n) > 7 and len(n) < 16:
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                   "v", "w", "x", "y", "z"]
        numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
        lowercase = 0
        uppercase = 0
        number = 0
        special_character = 0
        special_characters = ["!","@","#","$","%","^","&","*","(",")"]
        for i in n:
            if i in letters:
                lowercase+=1
            elif i.lower() in letters:
                uppercase+=1
            elif i in numbers:
                number+=1
            elif i in special_characters:
                special_character+=1
        if lowercase > 0 and uppercase > 0 and 4 > special_character > 0 and number > 0:
            return "good password"
        else:
            return "not good password"
    else:
        return "too small or too big"
print(validation("hi"))
