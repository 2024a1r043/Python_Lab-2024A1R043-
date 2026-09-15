#WRite a python program to input a number and reverse it using arithmetic operations only
num=int(input("Enter a number:"))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reverse:",rev)