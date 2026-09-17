#WAP to input numbers in a list and find the second largest number
n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()

print("Second largest number:", numbers[-2])