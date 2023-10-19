# Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk.
# Write a program that reads all of the numbers stored in the file and calculates their total.

# Main method
def main():

    # The following try block is used to handle potential exceptions that may occur
    try:

        # Open file for reading
        infile = open("numbers.txt", "r")

        # Loop through the file and calculate the total of the number
        total = 0
        for line in infile:
            print(line.strip())
            total += int(line)

        print(f"The total of the numbers in the file is {total}")

        infile.close()

    # The except block is used to catch and handle specific exceptions
    except Exception: # This will catch all possible exceptions
        print("Exception occured!")

    # The finally block is executed regardless of whether an exception occurred or not
    finally:
        print("End of program!")

# Call the main method
if __name__ == "__main__":
    main()
