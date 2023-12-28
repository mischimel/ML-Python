# Variables

# A variable named 'age' is created and assigned the value 29
age = 29

# Variables can be used in expressions
double_age = age * 2

# A variable can be passed as an argument to a function
def age_person(age):
    print("This person is " + age + " years old.")

# Using the 'name' variable as an argument to the function
age_person(age)

# Update the value of the 'age' variable
age = 30


# You can only use a variable if a value is assigned to it
print(new_variable) # -> will result in an error since 'new_variable' is not assigned a value
