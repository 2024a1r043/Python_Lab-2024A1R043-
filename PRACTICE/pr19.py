#WAP to print a square pattern of stars for n rows and n columns.
#* * * *
#* * * *
#* * * *
#* * * *
n=int(input("Enter no of rows:"))
m=int(input("Enter no of columns:"))
for i in range(1,n+1):
    for j in range(1,m+1):
        print("*", end=" ")
    print()