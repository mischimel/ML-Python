# This program demonstrates an infinite loop.
# Create a variable to control the loop.
keep_going = 'y'

# Warning! Infinite loop!
while keep_going == 'y': # == is for comparison
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission.
    commission = sales * comm_rate

    # Display the commission.
    print(f'The commission is ${commission:,.2f}.')

    # add a "stopper"
    keep_going = input("do you want to continues (y for yes), everything else makes the program stopp: ")