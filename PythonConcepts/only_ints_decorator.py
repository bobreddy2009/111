def dec_for_sum(function):
    def inner(x,y):
        if type(x) == int and type(y) == int:
            return function(x,y)
        else:
            return f"the parameters have to be integers."
    return inner


@dec_for_sum
def sum(x,y):
    return x+y
print(sum(1,"hi"))