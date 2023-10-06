# Assume a file containing a series of names (as strings) is named names.txt and exists on the computer’s disk.
# Write a program that displays the number of names that are stored in the file.
# Hint: Open the file and read every string stored in it.
# Use a variable to keep a count of the number of items that are read from the file.

# Main method
def main():

    # The following try block is used to handle potential exceptions that may occur
    try:
        # Open file for reading
        infile = open("names.txt", "r")

        # Counter
        num_names = 0

        # Loop through the lines
        for line in infile:
            num_names += 1 # count the line/names
            print(line.strip()) # print the names without a empty line

        # print the number of names in the file
        print(f"There are {num_names} names in the file.")

        # Close the file
        infile.close()

    # The except block is used to catch and handle specific exceptions
    except Exception: # This will catch all possible exceptions
        print("Error occured!")

    #  The finally block is executed regardless of whether an exception occurred or not
    finally:
        print("Saletti Spaghetti...")


# Call the main method
if __name__ == '__main__':
    main()
