#. Write a Python program to show that tuple values cannot be changed directly. Convert the tuple into a list, update it, and convert it back into a tuple.
n = int(input("Enter number of elements: "))

t = ()

for i in range(n):
    value = input("Enter element: ")
    t = t + (value,)

print("Original tuple:", t)

lst = list(t)

pos = int(input("Enter position to update: "))
new_value = input("Enter new value: ")

if 0 <= pos < len(lst):
    lst[pos] = new_value
    t = tuple(lst)
    print("Updated tuple:", t)
else:
    print("Invalid position")