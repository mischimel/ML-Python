#The date June 10, 1960, is special because when it is written in the following format, the month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year.
# The program should then determine whether the month times the day equals the year.
# If so, it should display a message saying the date is magic. Otherwise, it should display a message saying the date is not magic.

day = int(input("Please enter a day: "))
month = int(input("Please enter a month: "))
year = int(input("Please enter a year (two-digit format): "))

if day*month == year:
    print("this date is magic.")
else:
    print("this date is not magic.")