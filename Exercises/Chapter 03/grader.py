# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade. Condition using elif statement.
# if, elif, else needs a ":"
if score >= A_score:
    print("Your grade is A.")
elif score >= B_score:
    print("Your grade is B.")
elif score >= C_score:
    print("Your grade is C.")
elif score >= D_score:
    print("your grade is D.")
else:
    print("Your grade is F.")


# Using "switch" stementent to determin the grade.
match score:
    case int(score) if score >= A_score:
        print("A")
    case int(score) if score >= B_score:
        print("B")