#!/bin/python3

def build_calendar(daynum):
    totaldays = int(input("How many days are in the month? (31, 30, 28):  "))
    daynames = ["s", "m", "t", "w", "r", "f", "a"]

    for date in range(1, totaldays + 1):
        print(f"{date}{daynames[daynum % 7]}")
        daynum += 1

firstdayname = input("What day of the week is the first day of the month? (s, m, t, w, r, f, a):  ")
dayname_to_num = {"s": 0, "m": 1, "t": 2, "w": 3, "r": 4, "f": 5, "a": 6}

daynum = dayname_to_num.get(firstdayname)
if daynum is not None:
    build_calendar(daynum)
else:
    print("Not a valid day of the week abbreviation")
