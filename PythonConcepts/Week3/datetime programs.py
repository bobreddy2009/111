import datetime as dt


# Q6
x = dt.date(month=8, day=1, year=2020)
y = dt.date(month=8, day=4, year=2020)


def week(a_date):
    calendar = a_date.isocalendar()
    week_number = calendar[1]
    return week_number


print(week(x))


# Q7
def day(a_date):
    calender = a_date.isocalendar()
    day_number = calender[2]
    days_week = ("Sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "")
    day_name = days_week[day_number]
    return day_name


print(day(y))


# Q8
def time_change(date_1, date_2):
    l = abs(date_1 - date_2)
    output = [str(l.days)]
    if l.days == 1:
        output.append("day")
    else:
        output.append("days")
    return " ".join(output)


print(time_change(x, y))
