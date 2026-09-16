#Write a python prog to print a centered pyramid using stars
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)