# Write a program that displays a table of the Celsius temperatures 0 through 20 and their Celsius equivalents.
# The formula for converting a temperature from Celsius to Fahrenheit is: F = 9/5*C + 32
# where F is the Fahrenheit temperature, and C is the Celsius temperature.
# Your program must use a loop to display the table.

print("Celsius\t\t\tFahrenheit")
print("--------------------------")

temp_C = ""
temp_F = ""

for temp_C in range (0,10,1):
    temp_F = 9/5*temp_C+32
    print(f"{temp_C:.1f}\t\t\t{temp_F:.1f}")

for temp_C in range (10,21,1):
    temp_F = 9/5*temp_C+32
    print(f"{temp_C:.1f}\t\t{temp_F:.1f}")

# range splitted so the table looks nice - see the different amount of tabs in line 14 and 18