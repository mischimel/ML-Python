# Strings and String Literals

string = "This is a string."
string = 'This is a string.'

string_literal = 'This is a string literal.'
string_literal = "This is a string literal."

multiline_literal = """
This is a multiline
string literal.
It can contain both 'single' and "double" quotes.
"""

multiline_literal = '''
This is a multiline
string literal.
It can contain both 'single' and "double" quotes.
'''

# More About The print Function Example

# Using newline character as the default end of printed data
print("This is the first line.")
print("This is the second line.")

# Using a custom delimiter (comma and space) as the end of printed data
print("This is the third line.", end=", ")
print("And this is still part of the third line.")

# Using a custom separator (pipe) between items in the print function
print("Item 1", "Item 2", "Item 3", sep=" | ")

# Using special characters in string literals
print("This is a string with a newline character.\nThis is the second line after the newline character.")

# Using a combination of special characters and custom end/separator
print("First part", end="\t")  # \t is the horizontal tab character
print("Second part")

print()
# f-strings
num = 12345.6789
print(f'The number is {num:12,.2f}')

print(f'{num:<20.2f}')
print(f'{num:>20.2f}')
print(f'{num:^20.2f}')

print(f'{num:^10,.2f}')



