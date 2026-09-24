#Write a Python program to store repeated values in a tuple and count how many times a given value appears.
t = (10, 20, 10, 30, 10, 40, 20, 10)

value = int(input("Enter value to count: "))

count = t.count(value)

print(value, "appears", count, "times")