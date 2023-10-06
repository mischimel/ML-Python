# Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk.
# Write a program that displays all of the numbers in the file.

# Create also a main method, ensure it is taken care of exceptions

# Main method
def main():

    # The following try block is used to handle potential exceptions that may occur
    try:
        # Open file for reading
        infile = open("numbers.txt", "r")

        # Loop through all the lines in the file
        for line in infile:
            print(line.strip())  # .strip() used to get rid of the empty lines between the numbers

        # Close the file
        infile.close()

    # The except block is used to catch and handle specific exceptions
    except Exception:  # This will catch all possible exceptions
        print("Error occured!")

    #  The finally block is executed regardless of whether an exception occurred or not
    finally:
        print("Salve !!")


# Call the main method
if __name__ == '__main__':
    main()
