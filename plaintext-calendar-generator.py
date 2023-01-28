#!/bin/python3

# function to build the text calendar
def build_calendar(daynum):

    # ask for totaldays of the month
    totaldays = int(input("How many days are in the month? (31, 30, 28):  "))

    # set dayname list and date variable
    daynames = ["s", "m", "t", "w", "r", "f", "a"]
    date = 1

    # calculate days
    while date <= (totaldays):

        # restart dayname at end of week
        if daynum > 6:
            daynum = daynum - 7

        # print date+dayname
        print(str(date)+daynames[daynum])

        #increment counters
        daynum = daynum + 1
        date = date + 1

# asks for the first day and calls build calendar function if valid input is given
firstdayname = input("What day of the week is the first day of the month? (s, m, t, w, r, f, a):  ")
if firstdayname == "s":
    daynum = 0
    build_calendar(daynum)
elif firstdayname == "m":
    daynum = 1 
    build_calendar(daynum)
elif firstdayname == "t":
    daynum = 2
    build_calendar(daynum)
elif firstdayname == "w":
    daynum = 3 
    build_calendar(daynum)
elif firstdayname == "r":
    daynum = 4 
    build_calendar(daynum)
elif firstdayname == "f":
    daynum = 5
    build_calendar(daynum)
elif firstdayname == "a":
    daynum = 6 
    build_calendar(daynum)  
else:
    print("Not a valid day of the week abbreviation")
