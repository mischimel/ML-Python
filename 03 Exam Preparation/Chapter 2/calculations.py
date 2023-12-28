# Performing Calculations

# Addition
sum_result = 10 + 5                  # = 15

# Subtraction
difference_result = 10 - 5           # = 5

# Multiplication
product_result = 10 * 5              # = 50

# Floating Point Division
division_result = 10 / 4             # = 2.5

# Integer Division
integer_division_result = 10 // 4   # = 2

# Modulo (Remainder)
remainder_result = 10 % 4           # = 2 (2*4 fit into 10, but 2 remain, as 10 - (2*4) = 2)

# Using Variables in Expressions
# ** is the exponentiation operator
radius = 3
pi = 3.14159
area = pi * radius ** 2             # = 28.27431

# Operator Precedence and Grouping with Parentheses Example

# Using parentheses to force a specific order of operations
result1 = 2 + 3 * 4         # Without parentheses, multiplication takes precedence
                            # = 2 + 12 = 14

result2 = (2 + 3) * 4       # With parentheses, addition is performed first
                            # = 5 * 4 = 20

# Exponentiation
result3 = 2 ** 3            # 2 raised to the power of 3
                            # = 2 * 2 * 2 = 2^3 = 8

# Mixed operators with precedence
result4 = 5 * 2 + 10 / 2    # Multiplication and division have higher precedence than addition
                            # = 10 + 5 = 15.0

# Using parentheses to override precedence
result5 = 5 * (2 + 10) / 2  # Addition is forced to be performed before multiplication
                            # = 5 * 12 / 2 = 30.0


# Mixed-Type Expressions and Data Type Conversion Example

# Two int values: result is an int
result1 = 10 + 5        # = 15 <int>

# Two float values: result is a float
result2 = 10.0 + 5.5    # = 15.5 <float>

# int and float: int temporarily converted to float, result is a float
result3 = 10 + 5.5      # = 15.5 <float>

# Mixed-type expression: float to int causes truncation of the fractional part
result4 = (int(10.8) + 5) # = 15 <int>






