models = []
mpg = []
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
            mpg_2 = spliited[5]
            models.append(model)
            mp2 = mpg_2[:-1]
            mpg.append(mp2)
index = mpg.index(max(mpg))
print(f"The {models[index]} is the best model")