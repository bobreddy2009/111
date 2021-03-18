models = []
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
            gas = spliited[5]
            gas = gas[:-1]
            if gas.lower() == "true":
                models.append(model)
print(models)