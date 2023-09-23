# Write a program that asks the user for an integer and converts this integer into a binary number.
# Example: 10 -> 00001010
# Hint: There exist different ways for implementation.

# Ask the user for an integer input
int_num = int(input("Enter the integer you want to convert into a binary number: "))

# Convert the integer to a binary string
binary_representation = bin(int_num)[2:]  # [2:] to remove the '0b' prefix

# Ensure that the binary representation has 8 bits (leading zeros if necessary)
binary_representation = binary_representation.zfill(8)

# Print the binary representation
print("The integer", int_num, " converted into a binary number is ", binary_representation)
