i = [[1, 2, 3], [3, 2, 1], [200, 1, 31]]


def sort_list(x):
    # new_list = [i.sort() for i in x]
    new_list = []
    for i in zip(x):
        try:
            i.sort()
        except:
            pass
        new_list.append(i)
    return new_list


print(sort_list(i))

#i = [[1,3,2]]
#new_list = [j.sort() for j in i]
#print(new_list)
