# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food,
# then calculate the amounts of a 18 percent tip and 7 percent sales tax.
# Display each of these amounts and the total.

# Ask for the charge of food
food_charge = float(input("Enter the charge for the food: "))

# Calculate the the tip and the sales tax
tip = food_charge * 0.18
sales_tax = food_charge * 0.07

# Print the tip, sales tax, and total
# Function: round(number, decimals)
print("If the charge of your food is ", food_charge, "\nthen 18% tip are ", round(tip, 2),
      "\nand the 7% sales tax are ", round(sales_tax, 2),
      ".\nThe total consiting of the charge of the food, the tip and the sales tax is ",
      round(food_charge + tip + sales_tax, 2))
