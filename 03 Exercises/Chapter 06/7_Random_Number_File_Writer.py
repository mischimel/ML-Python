# Write a program that writes a series of random numbers to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold.

import random


# Main method
def main():
    # The following try block is used to handle potential exceptions that may occur
    try:

        # Open file for reading
        outfile = open("random_numbers.txt", "w")

        # Ask the user how many numbers the file should hold
        number_for_file = int(input("How many numbers should the file hold? "))

        # Loop to generate random numbers and write them to the file
        count = 1
        while count <= number_for_file:
            outfile.write(str(random.randint(1, 500)) + "\n")
            count +=1

        outfile.close()

    # The except block is used to catch and handle specific exceptions
    except Exception:  # This will catch all possible exceptions
        print("Exception occured!")

    # The finally block is executed regardless of whether an exception occurred or not
    finally:
        print("End of program!")


# Call the main method
if __name__ == "__main__":
    main()
