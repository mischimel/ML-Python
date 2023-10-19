# Write a program that asks the user to enter a series of single-digit numbers
# with nothing separating them. The program should display
# the sum of all the single digit numbers in the string. For example,
# if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1, and 4

def main():
    # get user input
    number_string = input("Please enter a series of single-digit numbers with nothing separating them: ")

    # call the function
    total = string_total(number_string)

    # print the result
    print(f"The total of the digits is {total}.")

# create the function
def string_total(string):
    number = 0
    total = 0

    # loop through the string
    for i in range(len(string)):

        # Convert characters to integers
        number = int(string[i])
        # print(f"i = {i} | num = {number}")

        # Accumulate the integers
        total += number

    # return the total
    return total






if __name__ == "__main__":
    main()