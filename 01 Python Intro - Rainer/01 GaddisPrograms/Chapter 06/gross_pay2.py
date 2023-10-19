# This program calculates gross pay.

def main():
    try: # you want to execute code
        # Get the number of hours worked.
        hours = int(input('How many hours did you work? '))

        # Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))

        # Calculate the gross pay.
        gross_pay = hours * pay_rate

        # Display the gross pay.
        print(f'Gross pay: ${gross_pay:,.2f}')
    except ValueError: # all possible "dirty" situations
        print('ERROR: Hours worked and hourly pay rate must')
        print('be valid integers.')

# Call the main function.
if __name__ == '__main__':
    main()

"""
try: you want to execute code
except: all possible "dirty" situations (is the java "catch")
else:v code is executed when everything is working (when try works)
finally: always executed
"""