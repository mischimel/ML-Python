# Write a program that gives simple math quizzes.
# The program should display two random numbers that are to be added, such as: 247 + 129
# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect, a message showing the correct answer should be displayed.

import random

number_1 = random.randint(1,1001)
number_2 = random.randint(1,1001)
result = number_1 + number_2

solution = float(input(f"What is {number_1} + {number_2} = "))

if solution == result:
    print(f"Congratulations, you solved the following equation correct: {number_1} + {number_2} = {result} !")
else:
    print(f"Sorry, you solved the following equation incorrect, here is the correct solution {number_1} + {number_2} = {result} !")