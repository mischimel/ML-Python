# Write a program with a loop that asks the user to enter a series of positive numbers.
# The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered, the program should display their sum.

num = 1
sum = 0

while num > 0:
    num = int(input("Enter a positive number (negative to stop entering): "))
    if num > 0:
        sum += num

print(f"The sum of all the numbers inputted is {sum}.")