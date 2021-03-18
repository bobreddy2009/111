a = {1,2,3,4}
b = {1,3,9}
c = {2,3,4}
points = 0
for i in a:
    if i in b:
        points += 1
    if i in c:
        points += -1
print(points)
