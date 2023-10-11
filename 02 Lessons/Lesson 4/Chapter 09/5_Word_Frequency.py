# 5. Word Frequency Write a program that reads the contents of a text file.
# The program should create a dictionary in which the keys are the individual
# words found in the file and the values are the number of times each word appears.
# For example, if the word “the” appears 128 times, the dictionary would contain
# an element with 'the' as the key and 128 as the value.
# The program should either display the frequency of each word or create
# a second file containing a list of each word and its frequency.

def main():

    input_file = open("text.txt", "r")
    text = input_file.read()
    all_punct = ",.?!"

    # Running a loop to remove all punctions
    for element in text:
        if element in all_punct:
            text = text.replace(element, "")

    # words is a list
    words = text.split() # default version means to split when there is a space " "

    # list comprhension to make all words lowercase
    words = [word.lower() for word in words]

    unique_words = set(words)

    unique_words = sorted(unique_words)

    for word in unique_words:
        print(word)

    print(unique_words)

    input_file.close()

if __name__ == "__main__":
    main()