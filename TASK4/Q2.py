#write a pp to swap two numbers without using third variable

x = int(input())
y = int(input())

x = x+y
y = x-y
x = x-y
print(f"After swapping the x is {x} and y is {y}")