# extend to million
def number_to_words(x):
    my_dictionary = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",10: "Ten", 11: "Eleven",
                    12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",18: "eighteen",
                    19: "nineteen", 20: "twenty", 30: "Thirty", 40: "Fourty", 50: "Fifty", 60: "sixty", 70: "Seventy",
                    80: "eighty", 90: "ninety", 100: "one hundred", 200: "two hundred",
                    300: "three hundred", 400: "four hundred", 500: "five hundred", 600: "six hundred",700: "seven hundred", 800: "eight hundred",
                    900: "nine hundred", 1000: "one thousand", 2000: "two thousand", 3000: "three thousand",4000: "four thousand",
                     5000: "five thousand", 6000: "six thousand", 7000: "seven thousand", 8000: "eight thousand",9000: "nine thousand", 100000: "one hundred thousand",
                     200000: "two hundred thousand", 300000: "three hundred thousand", 400000: "hundred thousand",500000: "five hundred thousand",600000: "six hundred thousand", 700000: "seven hundred thousand", 800000: "eight hundred thousand",
                     900000: "nine hundred thousand"}
    x_str = str(x)
    if x > 999999:
        return "the number should be less than 100000"
    elif x == 0:
        return "zero"
    elif x in my_dictionary:
        return my_dictionary.get(x)
    else:
        count = 0
        num_string = ""
        power = len(x_str) - 1
        for index, i in enumerate(x_str):
            if count < 1:
                if int(i + x_str[-1]) in my_dictionary and power == 1:
                    num_string = num_string + my_dictionary.get(int(i + x_str[-1]))
                    power -= 1
                    return num_string
                elif power == 5 and int(i + x_str[index + 1] + x_str[index + 2]) not in my_dictionary:
                    k = 2
                    num = int(i) * 10 ** k
                    k -= 1
                    num_1 = int(x_str[index + 1]) * 10 ** k
                    k -= 1
                    num_2 = int(x_str[index + 2])
                    if num_1 == 0:
                        l = my_dictionary.get(num) + " " + my_dictionary.get(num_2)
                    elif num_2 == 0:
                        l = my_dictionary.get(num) + " " + my_dictionary.get(num_1)
                    else:
                        l = my_dictionary.get(num) + " " + my_dictionary.get(num_1) + " " + my_dictionary.get(num_2)
                    num_string = l + " thousand "
                    power -= 3
                    count += 2
                elif power == 4:
                    k = 1
                    num = int(i) * 10 ** k
                    num_1 = int(x_str[index + 1])
                    if int(i + x_str[index + 1]) in my_dictionary:
                        l = my_dictionary.get(num + num_1)
                        num_string = num_string + l + " thousand "
                    else:
                        l = my_dictionary.get(num) + " " + my_dictionary.get(num_1) + " thousand "
                        num_string = num_string + l
                    power -= 2
                    count += 1
                else:
                    if i != "0":
                        num = int(i) * 10 ** power
                        num_string = num_string + my_dictionary.get(num) + " "
                    power -= 1
            else:
                count -= 1
        return num_string


x = int(input("enter a number"))
print(number_to_words(x))

# else:
#    l = my_dictionary.get(num) + " " + my_dictionary.get(num_1) + " thousand "
"""elif power == 5 and int(i + x_str[index + 1] + x_str[index+2]) in my_dictionary:
                    k = 2
                    num = int(i) * 10 ** k
                    k-=1
                    num_1 = int(x_str[index+1]) * 10 ** k
                    num_2 = int(x_str[index+2])
                    l = my_dictionary.get(num+num_1+num_2) + " thousand "
                    num_string = num_string + l
                    power -= 3
                    count+=2"""

"""try:
    x = int(input("enter a number less than 100"))

    def numbers_to_words(number):
        if number >= 100:
            return "To high of a number"
        else:
            ones = ('one', "two", "three", "four", "five", "six", "seven", "eight", "nine", " ")
            tens = ("ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", " ")
            ten_to_nineteen = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen","nineteen")
            integers_ten_nineteen = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
            numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
            digits = []
            second_digit = []
            if number < 10:
                for index, j in enumerate(numbers):
                    if number == j:
                        digits.append(ones[index])
                        break
            else:
                y = str(number)
                tens_digit = y[0]
                ones_digit = y[1]
                for index, j in enumerate(numbers):
                    if j == int(tens_digit):
                        digits.append(tens[index])
                    if j == int(ones_digit):
                        second_digit.append(ones[index])
                digits.append(second_digit[0])

            if 9 < number < 20:
                new_digits = []
                for index, l in enumerate(integers_ten_nineteen):
                    if number == l:
                        new_digits.append(ten_to_nineteen[index])
                        return " ".join(new_digits)

            return " ".join(digits)


    print(numbers_to_words(x))
except:
    print ("integer please")
"""
