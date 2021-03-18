string = "I am going to talk about cats.  Cats are small pet animals. Cats have 4 legs.  They cannot talk. cats drink milk. It has 2 eyes and 2 ears. It has 14 teeth."
num = ""
time = 0
for index,letter in enumerate(string):
    if time < 1:
        if letter.isdigit():
            num = letter
            while True:
                if string[index + 1].isdigit():
                    num += string[index]
                    index += 1
                    time+=1
                else:
                    break

        print(num)
        num = 0
