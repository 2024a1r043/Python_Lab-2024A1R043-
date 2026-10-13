#WAP to perform searching activity using linear and binary search
numbers = input("Enter elements separated by spaces: ").split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

target = int(input("Enter number to search: "))

# Linear Search in original list

linear_position = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        linear_position = i
        break

# Binary Search in sorted list

sorted_numbers = sorted(numbers)

low = 0
high = len(sorted_numbers) - 1

binary_position = -1

while low <= high:

    middle = (low + high) // 2

    if sorted_numbers[middle] == target:
        binary_position = middle
        break

    elif target < sorted_numbers[middle]:
        high = middle - 1

    else:
        low = middle + 1


if linear_position != -1:
    print("Linear Search: Number found at position",
          linear_position + 1)
else:
    print("Linear Search: Number not found")


print("Sorted list for Binary Search:",
      sorted_numbers)


if binary_position != -1:
    print("Binary Search: Number found at position",
          binary_position + 1, "in the sorted list")
else:
    print("Binary Search: Number not found")