def word_mix(string1,string2):
    common = ""
    count = -1
    count2 = 0
    letter = string2[0]
    for i in range(len(string1)):
        if letter != string1[count]:
            count -= 1
            count2 += 1
        else:
            common+=letter
            for integer in range(count2):
                count+=1
                common+=string1[count]
            break
    count3 = len(common)
    final = ""
    for letter in string2:
        if count3 >0:
            count3-=1
        else:
            final+=letter
    print(string1 + final)
    print(common)
word_mix("hiii", "hii")