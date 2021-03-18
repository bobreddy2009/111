import os
import datetime
import time
home_dir = 'C:/Users/avane/Documents/dummy'
os.chdir(home_dir)
file_name = "aboutme"
for file in os.listdir():
    if file == "aboutme":
        x = time.strftime("%H:%M:%S")
        currenttimelist = x.split(":")
        currentime = "_" + currenttimelist[0] + currenttimelist[1]
        today = datetime.date.today()
        today = str(today)
        currentdatelist = today.split("-")
        currentdate = f"{currentdatelist[1]}_{currentdatelist[2]}_{currentdatelist[0]}"
        filename = f"Bak About me {currentdate}_{currentime}"
        os.rename(file, filename)

with open(file_name,'w') as f:
    while True:
        fact = input("enter something about you:")
        if fact == "quit":
            break
        else:
            f.write(fact)
            f.write("\n")