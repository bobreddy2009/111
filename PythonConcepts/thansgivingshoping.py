def time_left(name,cashier_number,other_people):
    all_people = [person for person in other_people]
    all_people.append(name)
    all_people.sort()
    time = 0
    for index,people in enumerate(all_people):
        if index % cashier_number == 0:
            time += 20
        if people == name:
            print(time)

time_left("Pooran", 2, ["Krishna", "Ananjana","Lakesh","Badri"])