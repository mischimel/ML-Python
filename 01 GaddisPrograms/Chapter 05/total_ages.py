# This program uses the return value of a function.

def main():
    # Get the user's age.
    first_age = int(input('Enter your age: '))

    # Get the user's best friend's age.
    second_age = int(input("Enter your best friend's age: "))

    # Get the sum of both ages.
    total = sum(first_age, second_age)

    # Display the total age.
    print(f'Together you are {total} years old.')

# The sum function accepts two numeric arguments and
# returns the sum of those arguments.
def sum(num1, num2): # see the "warning" should be renamed
    result = num1 + num2
    return result  # sending back result of the function (without the method is of type void)

def summe(num1, num2)-> float: # typehint (gives a hint about the type of the result)
                                # and only info for reader
    result = num1 + num2
    return result

# Call the main function.
main()
