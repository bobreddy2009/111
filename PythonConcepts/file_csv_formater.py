# csv = comma separated value
import csv
from datetime import datetime
path = "data/superbowl.csv"
with open(path,newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [row for row in reader]
print(header)
sb_list = []
for d in data:
    sb_dict = {}
    d1 = datetime.strptime(d[0],'%b %d %Y')
    sb = d[1].split()
    sb_roman = sb[0]
    sb_int = int(sb[1][1:-1])
    winner = d[2]
    winner_points = int(d[3])
    loser = d[4]
    loser_points = int(d[5])
    mvp = d[6]
    stadium = d[7]
    city = d[8]
    state = d[9]
    sb_dict[header[0]] = d1
    sb_dict['sb_roman'] = sb_roman
    sb_dict['sb_int'] = sb_int
    sb_dict[header[2]] = winner
    sb_dict[header[3]] = winner_points
    sb_dict[header[4]] = loser
    sb_dict[header[5]] = loser_points
    sb_dict[header[6]] = mvp
    sb_dict[header[7]] = stadium
    sb_dict[header[8]] = city
    sb_dict[header[9]] = state
    sb_list.append(sb_dict)
    """sb_int = ''
    for letter in sb_int1:
        try:
            int(letter)
            sb_int+=letter
        except:
            pass
    print(int(sb_int))"""
print(sb_list)
sb_statistics = {}
for dict in sb_list:
    name = f"{dict.get('sb_roman')} winner"
    sb_statistics[name] = dict.get('Winner')
    name = f"{dict.get('sb_roman')} loser"
    sb_statistics[name] = dict.get('Loser')
    name = f"{dict.get('sb_roman')} winner pts"
    sb_statistics[name] = dict.get('Winner Pts')
    name = f"{dict.get('sb_roman')} loser pts"
    sb_statistics[name] = dict.get('Loser Pts')
    name = f"{dict.get('sb_roman')} date"
    sb_statistics[name] = dict.get('Date')
    name = f"{dict.get('sb_roman')} MVP"
    sb_statistics[name] = dict.get('MVP')
    name = f"{dict.get('sb_roman')} stadium"
    sb_statistics[name] = dict.get('Stadium')
    name = f"{dict.get('sb_roman')} city"
    sb_statistics[name] = dict.get('City')
    name = f"{dict.get('sb_roman')} state"
    sb_statistics[name] = dict.get('State')
print(sb_statistics)
"""team:
max superbowl won?
no superbowl won?
superbowl won in specific state?
how many superbowls(won or lost)?
suberbowl losses?
stadium:
most superbowls?
how many stadiums in a specific state?
what stadium sponsored the most superbowls
how many stadium in a specific city
how many times did a specific team win a superbowl in a specific stadium?
scores:
total points for a specific team
total points scored in a specific stadium
total number of winner points
total number of loser points
by how many points was a specific superbowl won by?
mvp:
who was the mvp in a specific superbowl?
how many times was a specific person mvp?
how many times had a player got more than 3 mvp's
most mvp's for a person
"""

