# Write a program that asks the user to enter the monthly costs for the following expenses incurred
# from operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance.
# The program should then display the total monthly cost of these expenses, and the total annual cost of these expenses.

loan_payment = float(input("Please enter the expenses incurred for loan payment: "))
insurance = float(input("Please enter the expenses incurred for insurance: "))
gas = float(input("Please enter the expenses incurred for gas: "))
oil = float(input("Please enter the expenses incurred for oil: "))
tires = float(input("Please enter the expenses incurred for tires: "))
maintenance = float(input("Please enter the expenses incurred for maintenance: "))

total_montly = loan_payment + insurance + gas + oil + tires + maintenance
total_yearly = total_montly * 12

print(f"The monthly expenses incurred are {total_montly} CHF, and the yearly expenses incurred are {total_yearly} CHF.")
