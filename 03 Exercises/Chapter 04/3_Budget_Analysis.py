# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total.
# When the loop finishes, the program should display the amount that the user is over or under budget.

budget = float(input("What is your monthly budget in CHF? "))

sum_expenses = 0
expense = ""

while expense != 0 :
    expense = float(input("Expense of current month (type 0 to see if budget is over- or underspend) "))
    sum_expenses += expense

spend = budget - sum_expenses
statement = ""

if spend == 0:
    statement = f"you are absolutely in Budget, neither over- nor underspent it. So {spend} CHF is left."
elif spend > 0:
    statement = f"you have underspent your budget, so {spend} CHF is left."
else:
    statement = f"you have overspend your budget, so {spend*(-1)} CHF has been spent too much."

print(f"Your budget is {budget} CHF, the total of your inputted expenses is {sum_expenses} CHF,",
      f"\ntherefore {statement}")