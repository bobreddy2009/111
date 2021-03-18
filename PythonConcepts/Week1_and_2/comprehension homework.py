import math
import itertools

# remove vowels
#x = input("enter str")
vowels = ("a","e","i","o","u")
#l1 = [i for i in x if i not in vowels]
#print("".join(l1))
#create dict with 2 sets
a = {1,2,3}
b = {1,3,2}
l2 = [{i:j} for i in a for j in b]
#print(l2)
# all possible cordinates
int1 = -1
int2 = 0
int3 = 9
l1 = [int1,int2,int3]
l2 = [int1,int2,int3]
l3 = [int1,int2,int3]
n = 8
cordinates = [(i,j,k) for i in l1 for j in l2 for k in l3 if i+j+k != n]
#print(cordinates)
# average student scores
math1 = [90,91,92,93,94,95,96,97,97,98,99]
physics = [90,91,92,93,94,95,96,97,97,98,99]
chemistry = [90,91,92,93,94,95,96,97,97,98,99]
average_1 = []
for index,i in enumerate(math1):
    average_1.append((i + physics[index] + chemistry[index])/3)

average = [(i+physics[index]+chemistry[index])/3 for index, i in enumerate(math1)]
#print(average)
# remonve empty places
my_dict = {"jack":1,"jill":2,"john":None}
l4 = [{i:my_dict.get(i)} for i in my_dict if my_dict.get(i) is not None]
#print(l4)

#factors
x = 17
factors = [i for i in range(1,x+1) if x % i == 0]
print(factors)
def improved_factors (n):
    max_num = math.sqrt(n)
    l1 = [(i, n//i) for i in range(1, int(max_num+1)) if n % i == 0]
    l2 = [i for my_tuple in l1 for i in my_tuple]
    l2.sort()

    return l2
n = 70
print(improved_factors(70))


# prime factorization
def isprime(x):
    y = math.sqrt(x)
    for i in range(2,int(y + 1)):
        if x % i == 0:
            return False
    return True
x = 1078
prime_factors = [i for i in range(2,x+1)if isprime(i) == True and x % i == 0]
print (prime_factors)
# count how many times
x = "I like coffee"

x = x.lower()
count = []
for i in x:
    if {i:x.count(i)} not in count and i != " ":
        count.append({i:x.count(i)})
#print(count)
y = []
for l in x:
    if l not in y:
        y.append(l)
y = "".join(y)
count_1 = [{letter:x.count(letter)} for letter in y if letter != " "]
#print(count_1)
# words and unique chars
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = [1,2,3,4,5,6,7,8,9]
x = "Today 7th is mid-day"
words = [i for i in x.split()]
print (f"words - {len(words)}")
new_str = [letter for letter in x if letter in letters or letter.lower() in letter or letter in numbers]
new_str = " ".join(new_str)
unique_char = [i for i in new_str if new_str.count(i) < 2]
print (f"unique characters - {len(unique_char)}")
# permutation
l1 = [1,2,3]
permutations = [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]
p = itertools.permutations(l1)
print(p)
def q10(my_str):
    tot_words = my_str.count(" ") + 1
    uc_set = {i for i in my_str if i.isalnum()}
    return tot_words,len(uc_set)
print(q10("Today 7th is mid-day"))

