##Write a python program to input four numbers from the user and find the greatest number among them.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    greatest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    greatest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    greatest = num3
else:
    greatest = num4
print(f"The greatest number is: {greatest}")