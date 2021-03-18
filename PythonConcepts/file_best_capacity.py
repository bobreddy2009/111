models = []
capcity = []
with open(file = "file_hondamodel.txt") as f:
    count = 0
    for line in f:
        count+=1
        if count == 1:
            pass
        else:
            count = 0
            spliited = line.split(",")
            model = spliited[0]
            capacity_2 = spliited[3]
            models.append(model)
            capcity2 = capacity_2[:-1]
            capcity.append(capcity2)
index = capcity.index(max(capcity))
print(f"The {models[index]} is the best model capcity wise.")