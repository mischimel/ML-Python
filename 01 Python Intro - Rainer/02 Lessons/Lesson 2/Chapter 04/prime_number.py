import sympy

number = int(input("Please enater an interger: "))
if sympy.isprime(number):
    print(number, "is prime.")
else:
    print(number, "is not prime.")
