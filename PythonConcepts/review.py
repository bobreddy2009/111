"""Consecutive Number Series
    Write a function that will return True if a given string (divided and grouped into a size)
    will contain a set of consecutive numbers, otherwise, return False.
    is_consecutive("252627282930") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 25, 26, 27, 28, 29, 30

    is_consecutive("789790790") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 789, 790, 791

    is_consecutive("46327843") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive."""
import re

def is_consecutive(my_string, divider=1):
    if divider > len(my_string) // 2:
        return False
    x = re.findall(r'.{1,' + str(divider) + '}', my_string)
    x = list(map(int, x))
    x1 = [a + 1 == b for a, b in zip(x, x[1:])]
    x1 = all(x1)
    if x1:
        return True, divider
    else:
        return is_consecutive(my_string, divider+1)

print(is_consecutive("123412351236123712381239"))
