# Design a program that asks the user to enter a series of 20 numbers.
# The program should store the numbers in a list then display the following data:
# • The lowest number in the list
# • The highest number in the list
# • The total of the numbers in the list
# • The average of the numbers in the list

import statistics

# main method
def main():

    # Initalize empty list for the numbers

    numbers = []
    # Loop to ask user for input and store numbers in a list
    for i in range(1,21,1):
        num = int(input(f"Number #{i} is: "))
        numbers.append(num)

    print(f"The list with the 20 numbers is: {numbers}")
    print(f"The lowest number of the list is: {min(numbers)}")
    print(f"The highest number of the list is: {max(numbers)}")
    print(f"The total of the numbers in the list is: {sum(numbers)}")
    print(f"The average of the numbers in the list is: {(sum(numbers)/len(numbers))}")
    # OR
    print(f"The average of the numbers in the list is: {statistics.mean(numbers)}")


# Call the main method
if __name__ == "__main__":
    main()
