#WAP to reverse every kth row in a matrix
r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

matrix = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter element: ")))
    matrix.append(row)

k = int(input("Enter k: "))

for i in range(k - 1, r, k):
    matrix[i].reverse()

print("Matrix after reversing every kth row:")

for row in matrix:
    print(row)