#. Write a Python program to show that tuple values cannot be changed directly. Convert the tuple into a list, update it, and convert it back into a tuple.
numbers = (10,20,30,40)
print("Original tuple:", numbers)

temp = list(numbers)
temp[1] = 200
numbers = tuple(temp)

print("Updated tuple:", numbers)


