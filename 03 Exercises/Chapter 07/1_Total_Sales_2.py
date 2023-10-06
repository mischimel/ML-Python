# Design a program that asks the user to enter a store’s sales for each day of the week.
# The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.

def main():
    # Initialize an empty list to store daily sales
    weekly_sales = []

    # Define a list of days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Use a loop to get sales for each day
    for day in days_of_week:
        # Ask the user to enter sales for the current day
        sales = float(input(f"Enter sales for {day}: $"))

        # Append the sales to the weekly_sales list
        weekly_sales.append(sales)

    # Calculate the total sales for the week
    total_sales = sum(weekly_sales)

    # Display the total sales for the week
    print(f"Total sales for the week: ${total_sales:.2f}")


if __name__ == "__main__":
    main()