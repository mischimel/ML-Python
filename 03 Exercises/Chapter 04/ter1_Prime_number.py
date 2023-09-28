# Write a program that reads an integer from the console and determines if the integer is a prime number or not.

number = int(input("Enter a number to check if it is a prime: "))

if number > 1:
    i = 0
    for i in range(2, int(number/2) +1): # * see explanation below
        if (number%i) == 0: # if this is true, then there is a divisor
            print(f"{number} is NOT a prime.")
            break  # to end the checking and printing after one divisor has been found
    else:
        print(f"{number} is a prime.")
else:
    print(f"{number} is either 0, 1, or negative, and therefore not a prime.")

# * To optimize the loop, we don't need to check numbers greater than half of the entered number.
# This is because if a number is divisible by any number greater than half of itself,
# it would also be divisible by a smaller number (less than half of itself), which we've already checked.