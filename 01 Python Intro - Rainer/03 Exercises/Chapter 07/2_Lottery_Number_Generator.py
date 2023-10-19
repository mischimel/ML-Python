# Design a program that generates a seven-digit lottery number.
# The program should generate seven random numbers, each in the range of 0 through 9,
# and assign each number to a list element. (Random numbers were discussed in Chapter 5.)
# Then write another loop that displays the contents of the list.

import random

# main method
def main():

    # Initalize an empty list for the seven-digit lottery number
    lottery_number = []

    # For loop to generate the random numbers and to add them to the list
    for i in range(1,8,1):
        num = random.randint(0,9)
        lottery_number.append(num)

    # Print the seven-digit lottery number
    print(f"The seven-digit lottery number is: {lottery_number}")
    # OR
    print("The seven-digit lottery number is: ",end="")
    for num in lottery_number:
        print(num,end=" ") # print the numbers only seperated with a " "

# Call the main method
if __name__ == '__main__':
    main()