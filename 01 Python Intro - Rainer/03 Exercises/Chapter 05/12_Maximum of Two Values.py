# Write a function named max that accepts two integer values as arguments and returns the value
# that is the greater of the two. For example, if 7 and 12 are passed as arguments to the function,
# the function should return 12. Use the function in a program that prompts the user to enter two integer values.
# The program should display the value that is the greater of the two.

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a second number: "))

def max(num_1, num2):
    if num_1 > num2:
        print(num_1)
    elif num2 > num_1:
        print(num2)
    else:
        print("the two numbers are equal!")

max(num_1,num_2)