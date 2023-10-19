# If you have downloaded the source code from the Computer Science Portal you will find a file named text.txt
# in the Chapter 08 folder. The text that is in the file is stored as one sentence per line.
# Write a program that reads the file’s contents and calculates the average number of words per sentence.

def main():

    infile = open("text.txt", "r")
    content = infile.read() # content is a list

    # each line (sentences) is now a member of the list
    sentences = content.split("\n") # sentences is a list

    # loop through all sentences and each sentence's words gets add as member to the list,
    # which length is then taken and added to the total
    total_words = 0

    for sentence in sentences:
        words = sentence.split() # default (means: split by " "), words is a list
        total_words += len(words)


    # calculate the average
    print(f"The average words/sentence of the document text.txt is: {total_words/len(sentences): .2f}")


    infile.close()

if __name__ == "__main__":
    main()