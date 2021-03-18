def dec_for_my_func(function):
    def inner(x):
        print(f"{x} is your parameter and the parameter type is {type(x)}")
        return function(x)
    return inner
@dec_for_my_func
def my_func(x):
    return x*x
print(my_func(4))
