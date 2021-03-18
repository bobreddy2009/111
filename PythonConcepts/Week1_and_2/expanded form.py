try:
    x = int(input("enter a number"))
    def expanded_form(x):
        output = []
        zero = 1
        for i in str(x):
            amount_zeros = "0" * (len(str(x)) - zero)
            unit = i + amount_zeros
            if int(unit) == 0:
                pass
            else:
                output.append(unit)
            zero += 1

        return " + ".join(output)
    print(expanded_form(x))
except:
    print ("integer please")
