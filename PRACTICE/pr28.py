#WAP to input a list and create new list with unique elements
n=int(input("Enter no of elements:"))

numbers =[]

for i in range(n):
    x=int(input("Enter no:"))
    numbers.append(x)

unique = []

for x in numbers:
    if x not in unique:
        unique.append(x)

print("Unique elements:", unique)