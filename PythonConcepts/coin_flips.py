import random
def flips():
    heads = 0
    tails = 0
    for i in range(1000):
        x = random.randint(1,2)
        if x == 1:
            heads+=1
        else:
            tails+=1
    yield f"you got {heads} heads and {tails} tails"

print(next(flips()))
    