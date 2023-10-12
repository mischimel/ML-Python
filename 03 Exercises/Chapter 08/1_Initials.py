# Write a program that gets a string containing a person’s first, middle, and last names,
# and displays their first, middle, and last initials. For example,
# if the user enters John William Smith, the program should display J. W. S.
def main():

    name = input("Please enter your first, middle, and last name: ")

    print(f"Your name is: {name}, so your initials you are:", end=" ")

    name_list = name.split()

    for name in name_list:
        if name: # check if name is not empty
            i = 0
            if i == len(name_list) - 1: # check if it is the last object
                print(name[0].upper())
            else:
                print(f"{name[0].upper()}.", end=" ")

if __name__ == "__main__":
    main()