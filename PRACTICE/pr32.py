#WAP to count how many times a particular element appears in a list
lst = list(map(int, input("Enter elements: ").split()))
element = int(input("Enter element to count: "))

count = lst.count(element)

print("Element appears", count, "times")