#WAP to input numbers in a list and create two seperate lists for even and odd numbers
n = int(input("Enter number of elements: "))

numbers = []
even = []
odd = []

for i in range(n):
    x = int(input("Enter number: "))
    numbers.append(x)

for x in numbers:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Even numbers:", even)
print("Odd numbers:", odd)