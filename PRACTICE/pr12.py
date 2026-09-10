#Write a python program to check whether a number is a perfect number. A number is perfect if the sum of its proper divisor is equal to the number itself
num = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i
if sum_of_divisors == num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")