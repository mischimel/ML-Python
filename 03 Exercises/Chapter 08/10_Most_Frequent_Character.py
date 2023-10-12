# Write a program that lets the user enter a string and displays the character that appears most frequently in the string.


def main():
    # Set up local variables:
    # Create a list to count the frequency of each letter (A to Z).
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # Create a string of uppercase letters.
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Initialize variables for tracking the most frequent letter.
    index = 0
    frequent = 0


    # Receive user input.
    user_string = input('Enter a string: ')

    for ch in user_string:
        ch = ch.upper()
        # Convert the character to uppercase to handle both lowercase and uppercase.

        # Determine which letter this character is.
        index = letters.find(ch)
        # Find the index of the character in the uppercase letters string.
        if index >= 0:
            # Check if the character is an uppercase letter.

            # Increase counting array for this letter.
            count[index] = count[index] + 1
            # Increment the count for the corresponding letter.

    for i in range(len(count)):
        if count[i] > count[frequent]:
            frequent = i
        # Iterate through the count list to find the most frequent letter.

    print(f'The character that appears most frequently '
          f'in the string is {letters[frequent]}.')
    # Display the most frequently appearing character.

# Call the main function.
if __name__ == '__main__':
    main()
