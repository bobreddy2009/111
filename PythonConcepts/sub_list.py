x = [1,2,3,4,5,6,2,3,4,3,1,6,6,6,6,6,6,6,6,6,6,6,7]
big_list = []
l1 = []
for int in x:
    if int in l1:
        continue
    else:
        new = []
        big_list.append(new)
        l1.append(int)
x.sort()
l2 = []
count = -1
for integer in x:
    if integer in l2:
        big_list[count].append(integer)
    elif integer not in l2:
        count += 1
        l2.append(integer)
        big_list[count].append(integer)
print(big_list)
