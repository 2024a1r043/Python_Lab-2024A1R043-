string = input("Enter a string: ")

# Count the number of alphabets
count = 0

for ch in string:
    if ch.isalpha():
        count += 1

print("Number of alphabets:", count)

# Extract characters from a given range
start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

print("Extracted string:", string[start:end])

# Check whether the string is alphanumeric
print("Is the string alphanumeric?:", string.isalnum())