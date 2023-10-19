# Write a program that creates a dictionary containing states as keys,
# and their capitals as values. (Use the Internet to get a list of the states and their capitals.)
# The program should then randomly quiz the user by displaying the name of a state and
# asking the user to enter that state’s capital.
# The program should keep a count of the number of correct and incorrect responses.
# --> changed it to swiss cantons and their abbreviations

import  random

def main():

    # create diconnaire
    swiss_cantons = {
        'Aargau': 'AG', 'Bern': 'BE', 'Freiburg': 'FR', 'Genf': 'GE',
        'Glarus': 'GL', 'Graubünden': 'GR', 'Jura': 'JU', 'Luzern': 'LU',
        'Neuenburg': 'NE', 'St.Gallen': 'SG', 'Schaffhausen': 'SH', 'Schwyz': 'SZ',
        'Solothurn': 'SO', 'Thurgau': 'TG', 'Tessin': 'TI', 'Uri': 'UR', 'allis': 'VS',
        'Vaud / Waadt': 'VD', 'Zug': 'ZG', 'Zürich': 'ZH', 'Appenzell Ausserrhoden': 'AR',
        'Appenzell Inner Rhodes': 'AI', 'Basel-Stadt': 'BS', 'Basel-Landschaft': 'BL',
        'Obwalden': 'OW', 'Nidwalden': 'NW'
    }



    # set up the quiz

    # initalise some variables needed in the loops
    correct = 0
    wrong = 0
    questions = 0

    while True: # infinite loop, with the if loop we check when to break the loop
        canton = random.choice(list(swiss_cantons.keys()))  # Randomly select a canton name (diconaire do not work with index)
        abbreviation = swiss_cantons[canton]  # when giving the canton name (key) to the diconnaire it gives back the values
        print(f"What is the abbreviation for the canton '{canton}'?")
        # getting the user input and deleting any spaces (.strip()) making it all to uppercase (.upper())
        user_input = input("Enter the abbreviation (enter 'stop' to finish the quiz): ").strip().upper()

        if user_input == "STOP": # STOP in capitals as the .upper() makes the userinput all in capital letters
            break # stoppes the code

        elif user_input == abbreviation:
            print("Correct")
            correct += 1
        else:
            print(f"Wrong! Correct would be {abbreviation}!")
            wrong += 1

        # counting the questions here, so it gets only count when the user did not stop the quiz before
        questions += 1


    print(f"You stopped the quiz after {questions} questions. \n"
          f"Out of {questions} questions you have answered {correct} correct and {wrong} wrong.")


if __name__ == "__main__":
    main()