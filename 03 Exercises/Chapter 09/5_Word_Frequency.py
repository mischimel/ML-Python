# Write a program that reads the contents of a text file.
# The program should create a dictionary in which the keys are the individual words found
# in the file and the values are the number of times each word appears.
# For example, if the word “the” appears 128 times, the dictionary would contain an element
# with 'the' as the key and 128 as the value. The program should either display the frequency of
# each word or create a second file containing a list of each word and its frequency.

def main():

    # Open the file
    infile = open("sample.txt", "r")

    # create an empty dictionary
    dict = {}

    # loop through the file line by line
    for line in infile:

        # split lines into words
        words = line.split()

        # loop through words
        for word in words:
            word = word.strip().strip(".,!?();:'").strip('"') # remove all kind of chars includin spaces and \n
            word = word.lower() # make the whole word to lower case

            if word in dict:
                dict[word] = dict.get(word) + 1
            else:
                dict[word] = 1

    # print the result (.items() gives back a pair of key (word) and value (frequency)
    for word, frequency in dict.items():
        print(f"{word}: {frequency}")


if __name__ == "__main__":
    main()