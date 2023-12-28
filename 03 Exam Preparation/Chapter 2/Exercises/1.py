"""
1. Personal Information
Write a program that displays the following information:
• Your name
• Your address, with city, state, and ZIP
• Your telephone number
• Your college major
"""

# get the inputs from the user
name = input("your name: ")
street = input("your street and number: ")
city = input("your city: ")
zip = input("your ZIP: ")
state = input("your state: ")
phone = input("your phone number: ")
college_major = input("your college major: ")

# display the input
address = street + "," + zip + "," + city + "," + state
print(f"Your name is: {name}")
print(f"You live at {address}")
print(f"Your phone is {phone}")
print(f"yur college major is {college_major}")
