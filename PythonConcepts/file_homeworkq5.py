import random
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y != 0:
        return x/y
num = random.randint(1,4)
first = random.randint(0,10000)
second = random.randint(0,10000)
if num == 1:
    answer = add(first,second)
    func = "add"
    sign = "+"
elif num == 2:
    answer = sub(first,second)
    func = "sub"
    sign = "-"
elif num == 3:
    answer = mul(first,second)
    func = "mul"
    sign = "*"
elif num == 4:
    answer = div(first,second)
    func = "div"
    sign = "/"
#f = open(file = "file_arthemeticlog.txt",mode="a")
with open(file = "file_arthemeticlog.txt",mode="a") as f:
    f.write(func + ":")
    f.write(f"{first}{sign}{second}={answer}" + "\n")
#f.write("hello world") - error
