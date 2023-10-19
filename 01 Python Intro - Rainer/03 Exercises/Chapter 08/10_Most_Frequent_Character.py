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

    # Loop through the string from the user
    for ch in user_string:
        ch = ch.upper() # Convert the character to uppercase to handle both lowercase and uppercase.

        # Determine which letter this character is.
        # Find the index of the character in the uppercase letters string.
        index = letters.find(ch)

        # the index of the list cannot be smaller 0
        if index >= 0:
            # Increment the count for the corresponding letter.
            count[index] = count[index] + 1

    # Iterate through the count list to find the most frequent letter.
    for i in range(len(count)):
        # if the number from the count list is bigger than the number at position frequent, set the frequent to that position index
        if count[i] > count[frequent]:
            frequent = i

    # Display the most frequently appearing character.
    # --> the letters list has the same indexes as the count list,
    # so before we found the biggest number and its index in the count list,
    # therefore we know that the letter from the letter list at that index is the one appearing most frequent.
    print(f'The character that appears most frequently '
          f'in the string is {letters[frequent]}.')


# Call the main function.
if __name__ == '__main__':
    main()
