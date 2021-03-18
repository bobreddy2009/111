with open("file_arthemeticlog.txt") as f:
    #data = f.read() - never use f.read()
    add = 0
    sub = 0
    mul = 0
    div = 0
    for line in f:
        line = line.lower()
        if line.find('add') != -1:
            add+=1
        if line.find('sub') != -1:
            sub+=1
        if line.find('mul') != -1:
            mul+=1
        if line.find('div') != -1:
            div+=1
        """l1 = line.split(':')
        if l1[0] == "add":
            add+=1
        if l1[0] == "sub":
            sub+=1
        if l1[0] == "mul":
            mul+=1
        if l1[0] == "div":
            div+=1"""

print(f"add:{add}")
print(f"sub:{sub}")
print(f"mul:{mul}")
print(f"div:{div}")
"""add = data.count("add")
sub = data.count("sub")
mul = data.count("mul")
div = data.count("div")
print(f"add:{add}")
print(f"sub:{sub}")
print(f"mul:{mul}")
print(f"div:{div}")"""

