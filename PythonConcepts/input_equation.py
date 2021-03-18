def addition(x,y) -> object:
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y == 0:
        return 'undefined'
    else:
        return x/y
def equation(string):
    parts = string.split()
    first = int(parts[0])
    symbol = parts[1]
    second = int(parts[2])
    answer = int(parts[4])
    if symbol == '+':
         if answer == addition(first,second):
             print("true")
         else:
             print("false")
    elif '-' == symbol:
        if answer == subtraction(first,second):
            print("true")
        else:
            print("false")
    elif symbol == '*':
        if answer == multiplication(first,second):
            print("true")
        else:
            print("false")
    elif symbol == '/':
        if answer == division(first, second):
            print("true")
        else:
            print("false")
equation("14 + 7 = 2")