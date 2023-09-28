# Write a program that asks the user for the number of males and the number of females registered in a class.
# The program should display the percentage of males and females in the class.
# Hint: Suppose there are 8 males and 12 females in a class.
#       There are 20 students in the class.
#       The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%.
#       The percentage of females can be calculated as 12 ÷ 20 = 0.6, or 60%.

# Ask for number of males and females in a class
males = int(input("How many of the class are males: "))
females = int(input("How many of the class are females: "))

# Calculate the total number of students in a class
total_class = males + females

# Calculate the percentage
male_percentage = males / total_class * 100
female_percentage = females / total_class * 100

# Print the percentage of males and females
print("The class has in total", total_class, ".",
      "\nIn the class there are ", male_percentage, "% males and ",
      female_percentage, "% females.")
