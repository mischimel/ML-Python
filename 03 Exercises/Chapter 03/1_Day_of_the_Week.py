# Write a program that asks the user for a number in the range of 1 through 7.
# The program should display the corresponding day of the week,
# where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.
# The program should display an error message if the user enters a number that is outside the range of 1 through 7.

number = int(input("Enter a number in the range of 1 through 7: "))

if number == 1:
    print("It's Monday!")
elif number == 2:
    print("It's Tuesday!")
elif number == 3:
    print("It's Wednesday!")
elif number == 4:
    print("It's Thursday!")
elif number == 5:
    print("It's Friday!")
elif number == 6:
    print("It's Saturday!")
elif number == 7:
    print("It's Sunday!")
else:
    print("The number entered is out of range")




