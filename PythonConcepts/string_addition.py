def addition_strings(x,y):
    x.lower()
    y.lower()
    new_x = 0
    new_y = 0
    my_dict = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,
               "fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"fourty":40,"fifty":50
               ,"sixty":60,"seventy":70,"eighty":80,"ninety":90}
    my_dictionary = {0:"zero",1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                     10: "Ten", 11: "Eleven",
                     12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
                     18: "eighteen",
                     19: "nineteen", 20: "twenty", 30: "Thirty", 40: "Fourty", 50: "Fifty", 60: "sixty", 70: "Seventy",
                     80: "eighty", 90: "ninety"}
    if x in my_dict:
        new_x = my_dict.get(x)
    else:
        splitx = x.split()
        new_x = my_dict.get(splitx[0]) + my_dict.get(splitx[1])
    if y in my_dict:
        new_y = my_dict.get(y)
    else:
        splity = y.split()
        new_y = my_dict.get(splity[0]) + my_dict.get(splity[1])
    if new_x + new_y in my_dictionary:
        return my_dictionary.get(new_x + new_y)
    else:
        new_num = new_x + new_y
        newest_num = ""
        power = 1
        for i in str(new_num):
            l = int(i) * (10 ** power)
            newest_num += my_dictionary.get(l) + " "
            power-=1
        return newest_num

print(addition_strings("eighteen","fourty one"))


