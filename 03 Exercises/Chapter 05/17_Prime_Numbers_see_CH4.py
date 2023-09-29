# A prime number is a number that is only evenly divisible by itself and 1.
# For example, the number 5 is prime because it can only be evenly divided by 1 and 5.
# The number 6, however, is not prime because it can be divided evenly by 1, 2, 3, and 6.
# Write a Boolean function named is_prime which takes an integer as an argument and returns
# true if the argument is a prime number, or false otherwise.
# Use the function in a program that prompts the user to enter a number
# then displays a message indicating whether the number is prime.

# define main method
def main():

    number = int(input("Enter a number: "))

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# define method to check if it is a prime number
def is_prime(number):
    half = (int(number/2))+1
    status = True

    for x in range(2,half):
        if number % x == 0:
            status = False
    return status

# call the main method
main()