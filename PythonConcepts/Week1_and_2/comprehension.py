list_1 = []
for i in range(1,11):
    list_1.append(i)
#print(list_1)

list_2 = [i for i in range(1,11)]
#print(list_2)

#List Value = [expression for(value) in (collection) if (expression)]
list_sqr = []
for i in range(1,11):
    x = i * i
    list_sqr.append(x)
#print(list_sqr)

list_sqr_2 = [i*i for i in range(1,11)]
#print(list_sqr_2)

list_sqr_even = []
for i in range(1,11):
    if i % 2 == 0:
        list_sqr_even.append(i*i)

#print(list_sqr_even)

list_sqr_even_2 = [i*i for i in range(1,11) if i % 2 == 0]
#print(list_sqr_even_2)

list_div_7 = [i for i in range(1,100) if i % 7 == 0]
#print(list_div_7)
def calc_i (i):
    return i + 10
list_mul_4 = [calc_i(i) for i in range(1,21)]
#print(list_mul_4)

cities = ["Austin", "Chicago", "Los Angeles", "New York", "Boston", "Houston", "San Francisco"]
cities_no_blank = [city for city in cities if city.count(" ") < 1]
#print(cities_no_blank)
cities_start_abc = [city for city in cities if city.upper()[0] == "A" or city.upper()[0] == "B" or city.upper()[0] == "C"]
#print(cities_start_abc)
users = [{'name': 'John', 'age': 30},{'name': 'Max', 'age': 15},{'name': 'Rohan', 'age': 12},{'name': 'Anand', 'age': 45}]
users_name = [user.get("name") for user in users]
"""for i in users:
    print (i)
    users_name.append(i.get("name"))
"""
#print(users_name)
users_teen_name = [user.get("name") for user in users if 17 >= user.get("age") >= 12]
#print(users_teen_name)

users_adult_name = [user.get("name") for user in users if user.get("age") >= 18]
#print(users_adult_name)

a = {1,3}
b = {2,4}
output = [[1,2],[1,4],[3,2],[3,4]]
a = [1,3,5]
b = [2,4,9,8]
c = [10,11,12]
output_2 = [[1,2],[1,4],[1,9],[1,8],[3,2]]
cartesian_product_full = [[i,j,k] for i in a for j in b for k in c]
cartesian_product_filter = [[i,j,k] for i in a for j in b for k in c if i+j+k < 20]
"""for i in a:
    for j in b:
        l1 = [i,j]
        cartesian_product.append(l1)
"""
#print(cartesian_product_full)
#print(cartesian_product_filter)



