import random
numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key = ""
for i in range(10):
    l = random.randint(1,2)
    if l == 1:
        key += numbers[random.randint(0,9)]
    elif l == 2:
        key+= letters[random.randint(0,9)]



print(key)
email = input("enter your username:")
password = input("enter your password:")
your_pass = input("enter the letters/numbers shown above to create your account:")

if your_pass == key:
    print (f"your account is created. username:{email} password:{password}")

