def roman_num(x):
    if x > 3999:
        return "TOO LARGE. Must be smaller than 4000"
    else:
        my_dictionary = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: "IX",
                         10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",100: "C",
                         200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",1000: "M",2000: "MM", 3000: "MMM"}
        if x in my_dictionary:
            return my_dictionary.get(x)
        else:
            x_str = str(x)
            num_string = ""
            power = len(x_str) - 1
            for index, i in enumerate(x_str):
                if int(i + x_str[-1]) in my_dictionary and power == 1:
                    num_string = num_string + my_dictionary.get(int(i + x_str[-1]))
                    power -= 1
                    return num_string
                else:
                    num = int(i) * 10 ** power
                    num_string = num_string + my_dictionary.get(num)
                    power -= 1
            return num_string


#print(roman_num(int(input("enter a number"))))


def roman_num_2(x):
    x = x.upper()
    my_dict = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XX": 20,"XXX": 30, "XL": 40
        ,"L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90, "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500,"DC": 600, "DCC": 700, "DCCC": 800, "CM": 900
        ,"M": 1000, "MM": 2000, "MMM": 3000}
    if x in my_dict:
        return my_dict.get(x)
    else:
        list = []
        sum = 0
        count = 0
        for i in x:
            list.append(my_dict.get(i))
        for index, j in enumerate(list):
            if count < 1:
                try:
                    if list[index+1] - j in my_dict:
                        l = my_dict.get(list[index+1] - j)
                        count += 1
                    else:
                        l = j
                    sum += l
                except:
                    sum += j
            else:
                count -= 1
        if sum > 3999:
            return "TOO LARGE. Must be smaller than 4000"
        return sum


print(roman_num_2(input("enter a str")))
