#Write a python program to check whether a number is a perfect number.A number is perfect if the sum of its proper divisors is equal to the number itsself
number=int(input("Enter a number:"))
sum=0
for i in range(1,number):
    if number%i==0:
        sum+=i
if sum==number:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")