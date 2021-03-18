string = "Rain is rain and train is train but rain is in train and train is not rain to to to "


def second_highest_mode(x):
    x = x.split()
    most_occurrences = [0]
    mode = []
    for i in x:
        l = x.count(i)
        if i not in mode:
            most_occurrences.append(l)
            mode.append(i)
    new_occurrence = []
    for h in most_occurrences:
        if h != max(most_occurrences):
            new_occurrence.append(h)

    second_highest = max(new_occurrence)
    output = []
    for j in mode:
        if x.count(j) == second_highest:
            output.append(j)
    if not output:
        return "no second highest word"
    return ", ".join(output)


print(second_highest_mode(string))
