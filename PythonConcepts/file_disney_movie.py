import csv
import datetime
date = datetime.date(year=2000,month=1,day=1)
path = "data/disney_movies.csv"
with open(path,newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [row for row in reader]
disney_list = []
for d in data:
    disney_dict = {}
    disney_name = d[0]
    split = d[1].split('/')
    d1 = datetime.date(year=int(split[0]), month=int(split[1]), day=int(split[2]))
    disney_genre = d[2]
    rating = d[3]
    total_gross = int(d[4])
    inflation_adjusted_gross = int(d[5])
    disney_dict[header[0]] = disney_name
    disney_dict[header[1]] = d1
    disney_dict[header[2]] = disney_genre
    disney_dict[header[3]] = rating
    disney_dict[header[4]] = total_gross
    disney_dict[header[5]] = inflation_adjusted_gross
    disney_list.append(disney_dict)

count = []
for i in disney_list:
    date1 = i.get('release_date')
    name = i.get('movie_title')
    num = date-date1
    if num.days >0:
        count.append(name)
#print(count)
my_big_dict = {}
list1 = []
list_genres = []
for i in disney_list:
    x = i.get('genre')
    name = i.get('movie_title')
    if x not in my_big_dict:
        my_big_dict[x] = [name]
        list_genres.append(x)
    elif x in my_big_dict:
        my_big_dict.get(x).append(name)
for genre in my_big_dict:
    my_big_dict.get(genre).sort()
list_genres.sort()
final = []
for type in list_genres:
    for movie in my_big_dict.get(type):
        final.append(movie)
#print(list1)
dict1 = {}
l4 = []
l5 = []
for i in disney_list:
    x = i.get('release_date')
    name = i.get('movie_title')
    l4.append(x)
    dict1[x] = name
l4.sort(reverse=True)
for i in l4:
    x = dict1.get(i)
    l5.append(x)
#print(l5)
l2 = []
for i in disney_list:
    name = i.get('movie_title')
    list10 = name.split()
    if len(list10) > 4:
        l2.append(name)
#print(l2)
l3 = []
for m in disney_list:
    name = m.get('movie_title')
    for letter in name:
         try:
             int(letter)
             l3.append(name)
             break
         except:
             pass
#print(l3)
print("1) Movies released before Jan 1st 2000")
print("2) Disney movies listed by genre (alphabetically) - FIX")
print("3) Disney movies sorted by year")
print("4) Disney movies that have more than 4 words")
print("5) Disney movies with numbers")
while True:
    x = int(input("choose 1,2,3,4,5:"))
    if x == 1:
        print(count)
    elif x==2:
        print(final)
    elif x == 3:
        print(l5)
    elif x == 4:
        print(l2)
    elif x == 5:
        print(l3)
    else:
        break