# Reading Input from the Keyboard

# Using the input function to read a string input from the user
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Using the input function to read an integer input from the user
age_str = int(input("Enter your age: "))

# Convert the string input to an integer using the int() function
age = int(age_str)
# Perform an operation with the user's age
double_age = age * 2
print("Your age doubled is:", double_age)
