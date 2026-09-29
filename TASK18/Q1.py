#Write a Python program to store two points as tuples and calculate the distance between them
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

p1 = (x1, y1)
p2 = (x2, y2)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Point 1:", p1)
print("Point 2:", p2)
print("Distance =", distance)