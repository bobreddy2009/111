x = 20
number = x
list = []
large_list = []
starter = 1
for i in range(x):
    list.clear()
    for l in range(starter,number+1):
        list.append(str(l))
    m = " ".join(list)
    large_list.append(m)
    print(m.center(100))
    starter+=1

for i in range(-2,-1*x-1,-1):
    print(large_list[i].center(100))



