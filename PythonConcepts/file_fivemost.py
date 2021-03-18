city_names = []
count = 0
with open(file = "file_bio.txt") as f:
    for line in f:
        if count == 0:
            count+=4
        count-=1
        if count == 0:
            city_names.append(line)
s1 =set(city_names)
l1 = list(s1)
count = len(l1)
keys = []
values = []
my_dict = {}
for index,i in enumerate(l1):
    value = city_names.count(l1[index])
    values.append(value)
    keys.append(l1[index])
for i in range(5):
    high = max(values)
    index = values.index(max(values))
    print(keys[index])
    values.remove(max(values))
    values.insert(index,0)

