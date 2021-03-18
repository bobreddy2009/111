big_list = []
sub = ["english","math","physics","biology","chem"]
names = []
with open("file_studentscores.txt") as f:
    count = 0
    for line in f:
        count+=1
        if count == 1:
            name = line
            name = name[:-1]
            names.append(name)
        if count == 2:
            line = line[:-1]
            splitted = line.split(",")
            new_line = []
            for i in splitted:
                new_line.append(int(i))
            big_list.append(new_line)
            count = 0
english_scores = []
math = []
physics= []
bio = []
chem = []
for list in big_list:
    english_scores.append(list[0])
for list in big_list:
    math.append(list[1])
for list in big_list:
    physics.append(list[2])
for list in big_list:
    bio.append(list[3])
for list in big_list:
    chem.append(list[4])
english_winner = names[english_scores.index(max(english_scores))]
english_score = max(english_scores)
math_winner = names[math.index(max(math))]
math_score = max(math)
physics_winner = names[physics.index(max(physics))]
physics_score = max(physics)
bio_winner = names[bio.index(max(bio))]
bio_score = max(bio)
chem_winner = names[chem.index(max(chem))]
chem_score = max(chem)
print(f"{english_winner} - English --> {english_score}")
print(f"{math_winner} - math --> {math_score}")
print(f"{physics_winner} - physics --> {physics_score}")
print(f"{bio_winner} - bio --> {bio_score}")
print(f"{chem_winner} - chemistry --> {chem_score}")






