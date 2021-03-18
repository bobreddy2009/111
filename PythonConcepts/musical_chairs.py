def musical_chairs(people,gaps):
    gaps_2 = gaps
    participents = [num for num in range(people)]
    index = -1
    for num in range(int(people/gaps_2)):
        index += gaps
        participents = [person for index1,person in enumerate(participents) if index != index1]
    print(participents)
    while True:
        if index != people - 1:
            missing = people - index
            gaps = gaps - missing
            time = 1
        else:
            missing = 0
            time = 0
        if len(participents) < 2:
            print(participents[0])
            break
        else:
            index = 0
            for num in range(int(len(participents) / gaps_2)):
                if time > 0:
                    index += gaps
                    time -=1
                else:
                    gaps += missing
                    index += gaps
                participents = [person for index1, person in enumerate(participents) if index != index1]
            print(participents)
musical_chairs(5,2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def musical_chair(n, k):
    people = [i for i in range(n)]
    count = 1
    round = 1
    print(people)
    while True:
        if len(people) == 1:
            return people[0]
        for i in range(len(people)):
            if count == k:
                people[i] = 'x'
                count = 1
            else:
                count += 1
        print(f'Round {round}: {people}')
        p1 = [people[i] for i in range(len(people)) if people[i] != 'x']
        print(p1)
        people.clear()
        people = p1
        round += 1


print(musical_chair(15, 2))


