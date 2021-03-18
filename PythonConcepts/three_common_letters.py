def three_common(x):
    no_duplicates = []
    three_maxes = []
    final = []
    for i in x:
        if i not in no_duplicates:
            no_duplicates.append(i)
    counts = [x.count(i) for i in no_duplicates]
    for i in range(3):
        three_maxes.append(max(counts))
        counts.remove(max(counts))


    print(three_maxes)
    for i in no_duplicates:
        if x.count(i) in three_maxes:
            final.append(i)
            three_maxes.remove(x.count(i))


    print(final)
three_common("google")
