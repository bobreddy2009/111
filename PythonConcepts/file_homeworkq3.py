import os
header = False
file_name = 'file_hondamodel.txt'
if not os.path.exists(file_name):
    header = True
f = open(file = file_name,mode="a")
if header:
    print("model,vehicle_type,seat_type,capacity,gas,mpg", file=f)
def input_info():
    model = input("what is the model:")
    if model== "-1":
        exit(0)
    vehicle_type = input("whats type of vehicle is the honda:")
    seat_type = input("what is the seat type:")
    capacity = input("what is the capacity of the honda:")
    gas = input("Does the honda use gas(True or False):")
    mpg = input("what is the mpg:")

    return model,vehicle_type,seat_type,capacity,gas,mpg
def wite_bio(model,vehicle_type,seat_type,capacity,gas,mpg):
    f.write(f"{model},{vehicle_type},{seat_type},{capacity},{gas},{mpg} \n")
while True:
    model, vehicle_type, seat_type, capacity, gas, mpg = input_info()
    wite_bio(model,vehicle_type,seat_type,capacity,gas,mpg)