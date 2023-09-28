# Write a program that uses a Python package for checking if an integer is a prime number or not.
# The Python Package Index (PyPI, https://pypi.org/) is a repository of software for the Python programming language.

import sympy

number = int(input("Please enter an number: "))

if sympy.isprime(number):
    print(number, "is a prime.")
else:
    print(number, "is NOT a prime.")