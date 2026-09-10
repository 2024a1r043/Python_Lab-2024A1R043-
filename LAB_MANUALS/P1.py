#Write a program to demonstrate type checking of various data types and demonstrate the use of following built in functions in python: abs(), len(), min(), round(),isalnum(), type().
# Demonstrate type checking of various data types
# and use of abs(), len(), min(), round(), isalnum(), type()

a = int(input("Enter an integer: "))
b = float(input("Enter a decimal number: "))
name = input("Enter a string: ")
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of name:", type(name))
print("Type of numbers:", type(numbers))

print("Absolute value:", abs(a))
print("Length of name:", len(name))
print("Minimum number:", min(numbers))
print("Rounded value:", round(b, 2))
print("Is name alphanumeric?:", name.isalnum())