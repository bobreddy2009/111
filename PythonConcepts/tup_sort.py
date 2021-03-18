def tup_sort(x):
    string_x = []
    for i in x:
        tup = []
        for j in i:
            tup.append(str(j))
        string_x.append(tup)
    combined = ["".join(tup) for tup in string_x]
    int_combined = [int(i) for i in combined]
    int_combined.sort()
    final_combined = [str(i) for i in int_combined]
    output = []
    for i in final_combined:
        tiple = []
        count = 4
        for l in i:
            count-=1
            if count==0:
                break
            tiple.append(l)
        output.append(tuple(tiple))

    print(output)
tup_sort([(7,2,3),(2,3,4),(2,3,1),(2,4,1)])

