t = (10, 20, 30, 40, 50)

value = int(input("Enter value to search: "))

if value in t:
    position = t.index(value)
    print("Value is present")
    print("Position =", position)
else:
    print("Value is not present")