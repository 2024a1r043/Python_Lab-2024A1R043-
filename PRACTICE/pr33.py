#WAP to input two lists and create a third list containing common elements
list1 = [10,20,30,40]
list2 = [30,40,50,60]
common = []
for x in list1:
    if x in list2:
        common.append(x)
print("common elements",common)