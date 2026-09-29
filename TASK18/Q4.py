#Write a Python program to store repeated values in a tuple and count how many times a given value appears.
n = int(input("Enter number of elements: "))

t = ()

for i in range(n):
    value = int(input("Enter element: "))
    t = t + (value,)

print("Tuple:", t)

search = int(input("Enter value to count: "))

count = t.count(search)

print(search, "appears", count, "times")