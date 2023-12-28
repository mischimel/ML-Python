"""5. Distance Traveled
Assuming there are no accidents or delays, the distance that a car travels down the interstate can be calculated
with the following formula: Distance = Speed * Time
A car is traveling at 70 miles per hour.
Write a program that displays the following:
• The distance the car will travel in 6 hours
• The distance the car will travel in 10 hours
• The distance the car will travel in 15 hours
"""

# Calculate
SPEED = 70
time1 = 6
time2 = 10
time3 = 15

distance1 = SPEED * time1
distance2 = SPEED * time2
distance3 = SPEED * time3

print(f"When the car travels at 70 miles per hour, it will make in: \n"
      f"- {time1} hours, {distance1} miles \n"
      f"- {time2} hours, {distance2} miles \n"
      f"- {time3} hours, {distance3} miles \n")

