# Main method
def main ():
    try:
        # Open file for reading
        infile = open('numbers.txt', 'r')  # infile is the file handler variable

        # .realines() reads all lines, .readline() reads only 1 line, so here you must find where the end is
        for line in infile:
            print(line.strip()) # deletes all the spaces before and after (, end ="" would only kill the \n after)

        infile.close()

    # except IOError: --> specific error covered
    except Exception: # will cover all possible errors --> this will through a warning, as python would like to have more details (like above) about the exception
        print("Error occured!")

    finally:
        print("Bye...")


# Call the main method
if __name__ == '__main__':
    main()