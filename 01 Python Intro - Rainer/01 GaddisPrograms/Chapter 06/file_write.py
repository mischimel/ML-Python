# This program writes three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'w') # w = write, r = read, r+ or w+ means reading plus writing vice versa

    # Write the names of three philosphers
    # to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file.
    outfile.close()

# Call the main function.
if __name__ == '__main__':   # __method__ = magic method
    main()

# The __main__  code will be executed only if this script is run as the main program
# and not when it is imported as a module in another script.