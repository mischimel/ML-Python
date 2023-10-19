# Write a program that determines – using a function – the minimum of three integers which are read from the console.

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

print(f"The Maximum of the three numbers: {num_1}, {num_2}, and {num_3} is \n{max(num_1, num_2, num_3)}.")
print(f"The Minimum of the three numbers: {num_1}, {num_2}, and {num_3} is \n{min(num_1, num_2, num_3)}.")


def is_max(num_a, num_b,num_c):
    if num_a > num_b and num_a > num_c:
        return num_a
    elif num_b > num_a and num_b > num_c:
        return num_b
    elif num_c > num_a and num_c > num_b:
        return num_c
    elif num_a == num_b and num_a > num_c:
        return num_a, num_b
    elif num_a > num_b and num_a == num_c:
        return num_a, num_c
    elif num_b > num_a and num_b == num_c:
        return num_b, num_c
    else:
        return "numbers are identical"

print("function: ", is_max(num_1,num_2,num_3))