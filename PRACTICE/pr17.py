#WAP to repeateadly calculate the sum of digits of a number until the result becomes a single digit
#eg: 9875 -> 9 + 8 + 7 + 5 = 29 -> 2 + 9 -> 11 -> 1+1 =2
num = int(input("Enter a number: "))

while num >= 10:
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    num = sum

print("Single digit result:", num)