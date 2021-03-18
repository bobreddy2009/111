l1 = [1, 2, 3, 4, 5, 6]
x = 10
print(id(x))
x = 20
print(id(x))
print(id(l1))
l1.append("i")
print(id(l1))
boolean = True
print(id(boolean))
boolean = False
print(id(boolean))
tup1 = (1,2)
print(id(tup1))
tup1 = (1,2,3)
print(id(tup1))
print(f"address of l1 {id(l1)}")
def my_l1(my_list):
#    global x
#    print(x)
#    x += 5
#    my_list.append(7)
    my_list = list(my_list)
    my_list.append(7)
    print(f"address of l1 {id(l1)}")
    print(f"address of my_list {id(my_list)}")
    print(f"{x} defind outside")
#    x = 20
#    print(f"{x} defind inside")
my_l1(tuple(l1))
print(l1)



