# Design a program that asks the user to enter a store’s sales for each day of the week.
# The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.

# Main method
def main():

    # The following try block is used to handle potential exceptions that may occur
    try:

        # Ask user to enter the store's sales for each day:
        monday = int(input("Sales of Monday: "))
        tuesday = int(input("Sales of Tuesday: "))
        wednesday = int(input("Sales of Wednesday: "))
        thursday = int(input("Sales of Thursday: "))
        friday = int(input("Sales of Friday: "))
        saturday = int(input("Sales of Saturday: "))

        sales = [monday, tuesday, wednesday, thursday, friday, saturday]

        total = 0
        for val in sales:
            total += val

        print(f"The total sales is {total}")


    # The except block is used to catch and handle specific exceptions
    except Exception:  # This will catch all possible exceptions
        print("Error occured!")

    #  The finally block is executed regardless of whether an exception occurred or not
    finally:
        print("End of Program :)")


# Call the main method
if __name__ == '__main__':
    main()