city_names = []
count = 0
with open(file = "file_bio.txt",mode="a") as f:
    for name in f:
        if count == 0:
            count+=4
        count-=1
        if count == 0:
            city_names.append(name)
print(city_names)