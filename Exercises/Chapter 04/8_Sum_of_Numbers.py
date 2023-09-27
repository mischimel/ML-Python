# Write a program with a loop that asks the user to enter a series of positive numbers.
# The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered, the program should display their sum.

number = 1
total = 0.0

while number > 0:
    number = float(input("Enter a positive number (negative to stop): "))
    if number > 0: # otherwise negative number entered would also be in calculation
        total += number # -> total = total + number

print(f"Total Sum = {total:.2f}")
