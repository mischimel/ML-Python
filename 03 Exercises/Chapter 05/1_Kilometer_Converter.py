# Write a program that asks the user to enter a distance in kilometers, then converts that distance to miles.
# The conversion formula is as follows: Miles = Kilometers * 0.6214

kilometers = float(input("Enter a distance in kilometers: "))

miles = kilometers * 0.6214

print(f"{kilometers:.2f}kilometers are {miles:.2f}miles.")