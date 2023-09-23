# Write a program that asks the user for the number of males and the number of females registered in a class.
# The program should display the percentage of males and females in the class.
# Hint: Suppose there are 8 males and 12 females in a class.
#       There are 20 students in the class.
#       The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%.
#       The percentage of females can be calculated as 12 ÷ 20 = 0.6, or 60%.

males = int(input("How many of the class are males: "))
females = int(input("How many of the class are females: "))

total_class = males + females

male_percentage = males / total_class * 100
female_percentage = females / total_class * 100

print("The class has in total", total_class, ".",
      "\nIn the class there are ", male_percentage, "% males and ",
      female_percentage, "% females.")
