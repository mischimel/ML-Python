# Write a program that determines – using a function –
# the minimum of three integers which are read from the console.

# Method for finding the maximum of two numbers
def maximum(num_1, num_2):
    if num_1 < num_2:
        return num_2
    else:
        return num_1


# Main method
def main():
    num_1 = int(input("Please enter number 1: "))
    num_2 = int(input("Please enter number 2: "))
    # num_3 = int(input("Please enter number 3: "))
    print(f"Maximum of the two numbers is: {maximum(num_1, num_2)}")

# Calling the main method
main()
