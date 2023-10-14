# Write a program that opens a specified text file then displays a list of all the unique words found in the file.
# Hint: Store each word as an element of a set. --> set does not allow for duplicates

def main():

    # Open a file
    infile = open("sample.txt", "r")

    # Ititalize an empty set to store the unique_words
    unique_words = set()

    # loop through each line of the file
    for line in infile:
        # splite the lines in the words
        words = line.split() #default as there is only a space separating the words (words is a list)

        # to lower each words first letter, loop through the word list, and then add the lower_word to the set
        for word in words:
            lower_words = word.lower()
            unique_words.add(lower_words)

        # only lower case chars for each word and update the set with the word
        #unique_words.update(word.lower() for word in words)

    # print the set with the unique words
    print('These are the unique words in the text:')
    unique_words = sorted(unique_words) # sort them
    for word in unique_words:
        print(word)


if __name__ == "__main__":
    main()