#. Write a Python program to show that tuple values cannot be changed directly. Convert the tuple into a list, update it, and convert it back into a tuple.
t = (10, 20, 30, 40)

print("Original tuple:", t)

# t[1] = 50
# This will give TypeError because tuple cannot be changed directly.

lst = list(t)

lst[1] = 50

t = tuple(lst)

print("Updated tuple:", t)