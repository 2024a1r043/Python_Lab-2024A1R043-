#WAP to take inputs a and b , swap their values using a temporary variable and print updated values
a =int(input("Enter a no:"))
b =int(input("Enter another no:"))
a= a+b
b = a-b
a = a-b
print("After swapping :")
print("a=",a)
print("b=",b)