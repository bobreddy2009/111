import time
import datetime
import os
file_stats = os.stat("file_hondamodel.txt")
size = file_stats.st_size
if size >= 1024:
    x = time.strftime("%H:%M:%S")
    currenttimelist = x.split(":")
    currentime = "_" + currenttimelist[0] + currenttimelist[1]
    today = datetime.date.today()
    today = str(today)
    currentdatelist = today.split("-")
    currentdate = currentdatelist[1] + currentdatelist[2] + currentdatelist[0]
    filename1 = currentdate + currentime
    filename = f"file_hondamodel_{filename1}.txt"
    with open(file=filename, mode="a") as file:
        with open(file = "file_hondamodel.txt") as f:
            for line in f:
                file.write(line)