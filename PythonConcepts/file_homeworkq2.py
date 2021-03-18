f = open(file = "file_studentscores.txt",mode="a")
def input_info():
    name = input("what is your name:")
    english = input("whats is your English scores")
    math = input("what is your math scores:")
    physiscs = input("what is your physics scores:")
    bioligy = input("what is your biology scores:")
    chem = input("what is your chemistry scores:")

    return name,english,math,physiscs,bioligy,chem
def wite_bio(name,english,math,physics,biology,chem):
    print(name,file=f)
    print(f"{english},{math},{physics},{biology},{chem}", file=f)
while True:
    name,english,math,physics,biology,chem = input_info()
    if name == "-1":
        break
    wite_bio(name,english,math,physics,biology,chem)