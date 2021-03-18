f = open(file = "file_bio.txt",mode="a")
#data = f.write("hello world")
#print(data)
#f.write("\n")
#data = f.write("this is my first program managing files")
#print(data)
def input_bio():
    firstname = input("what is your first name:")
    lastname = input("what is your last name:")
    dob = input("what is your date of birth:")
    language = input("what is your favorite coding language:")
    return firstname,lastname,dob,language
def wite_bio(first,last,dob,lang):
    #f.write(first + " ")
    #f.write(last)
    #f.write("\n")
    #f.write(dob)
    #f.write("\n")
    #f.write(lang)
    #f.write("\n")
    print(f"{first} {last}",file=f)
    print(dob,file=f)
    #print(lang,file=f)
    f.write(lang + "\n")

first,last,dob,lang = input_bio()
wite_bio(first,last,dob,lang)

