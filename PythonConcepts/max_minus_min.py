def maximu_minus_minimum(x):
    min_digits = []
    max_digits = []
    for i in str(x):
        max_digits.append(i)
        min_digits.append(i)
    min_digits.sort()
    minimum = int("".join(min_digits))
    max_digits.sort(reverse=True)
    max = int("".join(max_digits))
    return max-minimum

print(maximu_minus_minimum(20))
