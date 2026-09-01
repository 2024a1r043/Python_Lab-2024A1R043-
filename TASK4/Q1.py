#write a pp to take inputs a and b , swap their values using temporary variable, and print updated values.

a = int(input())
b = int(input())

d = a
a=b
b = d
print(f"After swapping the a is {a} and b is {b}")