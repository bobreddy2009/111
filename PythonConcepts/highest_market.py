import csv
import statistics

path = "data/amazon_stock_data.csv"
with open(path, newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [row for row in reader]
am_list = []
for d in data:
    am_dict = {}
    am1 = d[0]
    am_close = float(d[1][1:])
    am_dict["date"] = am1
    am_dict["close"] = am_close
    am_list.append(am_dict)
closes = []
for i in am_list:
    closes.append(i.get("close"))
index = closes.index(max(closes))
bigest = max(closes)
answer1 = am_list[index].get("date")
print(answer1,bigest)
least = min(closes)
index = closes.index(min(closes))
answer2 = am_list[index].get('date')
print(answer2, least)
print("mean", statistics.mean(closes))
print("median", statistics.median(closes))
print("mode", statistics.mode(closes))
mean = statistics.mean(closes)
values = []
for value in closes:
    m = abs(mean - value)
    values.append(m)
print("MAD", statistics.mean(values))
