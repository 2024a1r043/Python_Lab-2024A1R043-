#Write a Python program to check whether a given value is present in a tuple. If present, display its position
n = int(input("Enter number of elements: "))

t = ()

for i in range(n):
    value = int(input("Enter element: "))
    t = t + (value,)

print("Tuple:", t)

search = int(input("Enter value to search: "))

if search in t:
    print("Value is present")
    print("Position =", t.index(search))
else:
    print("Value is not present")