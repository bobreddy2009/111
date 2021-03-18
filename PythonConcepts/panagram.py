def pangrams (x):
    x = x.lower()
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]
    counts = []
    for i in abc:
        counts.append(x.count(i))
    if min(counts) == 0:
        yield False
    else:
        yield True

print(next(pangrams("the quick brown fox jumps over the lazy dog")))



