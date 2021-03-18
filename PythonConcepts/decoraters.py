# meta-programming
def dec_for_all(function):
    def inner(*args,**kwargs):
        print("*"*10)
        print(function(*args,**kwargs))
        print("*"*10)
    return inner


def make_wings(function):
    def inner():
        print(f"building wings")
        function()
        print(f"got wings")
        print(f"----")

    return inner


@make_wings
def bird():
    print(f"I am an eagle")


# b = make_wings(bird)
# bird()


def make_wings1(function):
    def inner(name):
        print(f"building wings")
        function(name)
        print(f"got wings")
        print(f"----")

    return inner


@make_wings1
def bird1(name):
    print(f"I am a {name}")


# bird1("parrot")


def make_wings2(function):
    def inner(name, part):
        print(f"building {part}")
        function(name, part)
        print(f"got {part}")
        print(f"----")

    return inner


@make_wings2
def bird2(name, part):
    print(f"I am a {name} with a {part}")


# bird2("parrot", "beak")
def dec_for_division(function):
    def inner(a, b):
        if b == 0:
            print(f"you can't divide by {b}")
        else:
            print(f"{a} divided by {b} equals {function(a, b)}")

    return inner


@dec_for_division
def division(a, b):
    return a / b


#division(10, 2)
'''def dec_for_single(function):
    def inner(a):
        print('*' * 10)
        print(function(a))
        print("*" * 10)
    return inner'''

@dec_for_all
def single(a):
    return f"hello Mr.{a}"

single("jack")

"""def dec_for_double(function):
    def inner(a,b):
        print("*"*10)
        print(function(a,b))
        print("*"*10)
    return inner """

@dec_for_all
def double(a,b):
    return f"hello Mr.{a} and Mrs.{b}"

double("jack","Jill")

def dec_for_triple(function):
    def inner(mom,dad,son):
        print("*"*10)
        print(function(mom,dad,son))
        print("*"*10)
    return inner




@dec_for_all
def triple(mom,dad,son):
    return f"Hello Mr.{dad}, Mrs.{mom} and master {son}"

triple("Jill","jack","bob")