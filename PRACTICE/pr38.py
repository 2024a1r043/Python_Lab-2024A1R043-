#Write a Python program to check whether a given value is present in a tuple. If present, display its position
t = (10, 20, 30, 40, 50)

value = int(input("Enter value to search: "))

if value in t:
    position = t.index(value)
    print("Value is present")
    print("Position =", position)
else:
    print("Value is not present")