import datetime
import time
x = time.strftime("%H:%M:%S")
currenttimelist = x.split(":")
currentime = "_"+currenttimelist[0] + currenttimelist[1]
print(currentime)
today = datetime.date.today()
today = str(today)
currentdatelist = today.split("-")
currentdate = currentdatelist[1] + currentdatelist[2] + currentdatelist[0]
print(currentdate)
filename = currentdate + currentime
f = open(file = f"file_{filename}.txt",mode="a")