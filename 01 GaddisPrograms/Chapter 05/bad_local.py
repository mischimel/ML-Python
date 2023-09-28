# Definition of the main function.
name = ""  # global variable, so then it does not trigger an error below,
# and the variables are nolonger local variables, but it is now one global!


def main():
    get_name()
    print(f'Hello {name}.')  # This causes an error! as it is a new local variable,
    # a global variable would be needed


# Definition of the get_name function.
def get_name():
    name = input('Enter your name: ')  # local variable


# Call the main function.
main()
