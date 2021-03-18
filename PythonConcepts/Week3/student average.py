def average (students,*args):
    my_dict = {}
    for i,j in zip(students,args):
        sum = 0
        for l in j:
            sum+=l
        my_dict[i] = sum/len(j)
    return my_dict


print(average(["bob","jill","jack"],[99,68,95],[1,1,1],[2,3,4],[5,3,4]))

l1 = [1,1,2,3,4,4,5,6]
s1 = set(l1)
l1 = list(s1)
print(l1)

