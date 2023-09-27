# Running on a particular treadmill you burn 4.2 calories per minute.
# Write a program that uses a loop to display the number of calories
# burned after 10, 15, 20, 25, and 30 minutes.

# Constant
calories_per_minute = 4.2

print("Minutes\t\tCalories burned")
print("---------------------------")

# Calculate the calories with a for loop
for minutes in range (10,35,5):
    calories_burned = minutes * calories_per_minute
    print(minutes, "\t\t\t", calories_burned)