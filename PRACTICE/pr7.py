##Write a python program to input four numbers from the user and find the greatest number among them.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
greatest = max(num1, num2, num3, num4)
print(f"The greatest number is: {greatest}")