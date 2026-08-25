#WAP to take 2 digit no as ip and find sum of its digits
num = int(input("Enter a 2-digit number: "))
d1 = num // 10
d2 = num % 10
sum_of_digits = d1 + d2
print("Sum of digits:", sum_of_digits)