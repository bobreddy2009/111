def decimal (x):
    x = float(x)
    return x

def octal(x):
    return oct(x)
#print(octal(65))

def hexadecimal(x):
    return hex(x)
#print(hexadecimal(10))

def binary(x):
    return bin(x)
#print(binary(50))

x = 5
for i in range(1,x+1):
    print(end=str(decimal(i)) + "  ")
    print(end=octal(i) + "  ")
    print(end=hexadecimal(i) + "  ")
    print(end=binary(i) + "   ")
    print("\r")