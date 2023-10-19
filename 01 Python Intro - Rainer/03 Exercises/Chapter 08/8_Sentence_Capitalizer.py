# Write a program with a function that accepts a string as an argument
# and returns a copy of the string with the first character of each sentence capitalized.
# For instance, if the argument is “hello. my name is Joe. what is your name?”
# the function should return the string “Hello. My name is Joe.
# What is your name?” The program should let the user enter a string and then pass it to the function.
# The modified string should be displayed.

def main():
    userinput = input("Please enter something: ")

    sentences = userinput.split(". ")

    # Capitalize the first letter of each sentence
    capitalized_sentences = [capitalize_first_letter(sentence) for sentence in sentences]

    # Join the sentences back together
    result = ". ".join(capitalized_sentences)

    print("Modified String:")
    print(result)

def capitalize_first_letter(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Check if the sentence is not empty
    if words:
        # Capitalize the first letter of the first word
        words[0] = words[0].capitalize()

        # Reconstruct the sentence by joining the words with spaces
        return ' '.join(words)

    # If the sentence is empty, return an empty string
    return ""

if __name__ == "__main__":
    main()