my_dict = {}
indexes = []
with open("file_studentscores.txt") as f:
    count = 0
    for line in f:
        count+=1
        if count == 1:
            name = line
            name = name[:-1]
        if count == 2:
            line = line[:-1]
            splitted = line.split(",")
            new_line = []
            for i in splitted:
                new_line.append(int(i))
            my_dict[name] = new_line
            count = 0
final_dict = {}
list =[]
for name in my_dict:
    sum = 0
    for i in my_dict.get(name):
        sum += i
    list.append(sum)
    final_dict[sum] = name
list. sort(reverse=True)
for i in list:
    print(f"{final_dict.get(i)}:{i}")