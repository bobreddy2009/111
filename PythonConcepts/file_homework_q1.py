def input_info():
    name = input("what is your name:")
    gender = input("whats is your gender")
    dob = input("what is your date of birth:")
    city = input("what city do you live in:")
    if name != "-1":
        return name,gender,dob,city
def wite_bio(name,gender,DOB,city):
    print(name, file=f)
    print(gender,file=f)
    print(DOB,file=f)
    print(city, file=f)
with open(file="file_bio.txt", mode="a") as f:
    while True:
        name,gender,DOB,city = input_info()
        wite_bio(name,gender,DOB,city)
