# Write a program that translates single words, word fragments or full sentences from an arbitrary source language to English.
# The source language should be detected automatically.
# Texts to be translated into English should be entered via the console with entering “stop” for quitting the program.
# The translation itself should be coded using a function.
# For implementation use an existing powerful Python package. Assess the quality of the translations conducted.

# Import the Translator class from the googletrans module (use version 4.0.0.rc1)
from googletrans import Translator

# Define a function named 'translate_to_english' that takes one argument 'input_text' and translates it to 'output_text'
def translate_to_english(input_text) -> str: # -> str = is a typehint, so you know what the output of this method/function
    # Create an instance of the Translator class
    translator = Translator() # this is object oriented, but will not be covered in this class

    # Use the translator to translate 'input_text' from its detected language to English
    # 'dest' specifies the destination language (English in this case)
    # 'src' is set to 'auto' to automatically detect the source language
    output_text = translator.translate(input_text, dest="english", src="auto")

    # Return the translated text as a string
    return output_text.text

# getting the first input from the user
user_text = input("Enter something to translate it into Englisch (stop to stop the translation): ")

# translating user input and asking for new input
while user_text != "stop":
    print(translate_to_english(user_text))
    user_text = input("Enter something to translate it into Englisch (stop to stop the translation): ")

# after user typed "stop" the following gets printed
print("Thank you for translating with Michèle's translator")
