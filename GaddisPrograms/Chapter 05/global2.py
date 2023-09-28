# Create a global variable.
number = 0

def main():
    global number # local should behave like global variable
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print(f'The number you entered is {number}.')

# Call the main function.
main()