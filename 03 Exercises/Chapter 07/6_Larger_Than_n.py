# In a program, write a function that accepts two arguments:
# a list, and a number n. Assume that the list contains numbers.
# The function should display all of the numbers in the list that are greater than the number n.

# Create the function
def greather_n(list, n):
    first = True  # Flag to track the first number
    for num in list:
        if num > n:
            if not first:
                print(", ", end="")  # Print a comma and space before the number
            print(num, end="")
            first = False  # Set the flag to False after printing the first number
    print()  # Print a newline at the end to move to the next line

# main method
def main():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    treshold = 25
    greather_n(numbers,treshold)

# Call the main method
if __name__ == "__main__":
    main()