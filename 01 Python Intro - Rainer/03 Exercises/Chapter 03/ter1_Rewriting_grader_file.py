# Rewrite grader.py (see chapter 3 programs)
# by using
#   • Version 1: the elif statement
#   • Version 2: the match / case statement (is a “switch”-like statement available from v3.10 on)

# grader.py:
# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade.
"""
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.') 
"""

# Version 1: the elif statement
"""
if score >= A_score:
    print('Your grade is A.')
elif B_score <= score < A_score:
    print('Your grade is B.')
elif C_score <= score < B_score:
    print('Your grade is C.')
elif D_score <= score < C_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
"""

# Version 2: the match / case statement (is a “switch”-like statement available from v3.10 on)

match score:
    case score if score >= A_score:          # this
        print('Your grade is A.')
    case int(score) if score >= B_score:     # this
        print('Your grade is B.')
    case _ if score >= C_score:              # or this works, but there must be something between case and if!
        print('Your grade is C.')
    case _ if score >= D_score:
        print('Your grade is D.')
    case _:                                  # final case to catch any remaining cases.
        print('Your grade is F.')

