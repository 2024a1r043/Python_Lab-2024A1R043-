#WAP to rotate a list one position to the right
lst = list(map(int, input("Enter elements: ").split()))

last = lst.pop()
lst.insert(0, last)

print("Rotated list:", lst)