# A software company sells a package that retails for $99.
# Quantity discounts are given according to the following table:
# Quantity          Discount
# 10–19             10%
# 20–49             20%
# 50–99             30%
# 100 or more       40%
# Write a program that asks the user to enter the number of packages purchased.
# The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.

number_of_packages = int(input("How many packages have you purchased? "))

discount_percentage = ""

if number_of_packages in range(10,20):      # for a range between 10 and 19
    discount_percentage = 0.1
elif 20 <= number_of_packages <= 49:        # range can also be defined like this
    discount_percentage = 0.2
elif number_of_packages in range(50,100):   # range 50-99
    discount_percentage = 0.3
elif number_of_packages >= 100:
    discount_percentage = 0.4
else:                                       # for numbers smaller 10
    discount_percentage = 0


"""
OR
if number_of_packages < 10:
    discount_percentage = 0
elif number_of_packages in range(10,20):      # for a range between 10 and 19
    discount_percentage = 0.1
elif 20 <= number_of_packages <= 49:        # range can also be defined like this
    discount_percentage = 0.2
elif number_of_packages in range(50,100):   # range 50-99
    discount_percentage = 0.3
else:                                       # all numbers equal or bigger 100
    discount_percentage = 0.4
"""

purchase = number_of_packages * 99
discount_amount = purchase * discount_percentage
total = purchase - discount_amount

print("The amount of the discount (if any) is:", discount_amount,
      "\nand the total amount of the purchase after the discount is: ", total, ".",
      f"\nAs you purchased {number_of_packages} packages you received a {discount_percentage*100}% discount.")
