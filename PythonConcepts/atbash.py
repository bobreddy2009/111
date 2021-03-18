letters = ["", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]
x = "AZbQ"
output = ""
for i in x:
    for index,letter in enumerate(letters):
        if i == letter:
            opposite = -1*index
            output+=letters[opposite]

        elif i == letter.upper():
            opposite = -1 * index
            output += letters[opposite].upper()

print(output)

