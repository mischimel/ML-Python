"""
2. Sales Prediction
A company has determined that its annual profit is typically 23 percent of total sales.
Write a program that asks the user to enter the projected amount of total sales,
then displays the profit that will be made from that amount.
Hint: Use the value 0.23 to represent 23 percent.
"""
PROFIT = 0.23

#input from user for sales amount
sales = float(input("Please enter the projected amount of total sales: "))
sales_profit = sales * PROFIT
print(f"When making the following sales amount: {sales} \n"
      f"then the following profit is made: {sales_profit}.")