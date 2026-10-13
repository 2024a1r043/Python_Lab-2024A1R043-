# Create a database using lists and tuples. Each student record must contain roll number, name, branch, and CGPA. Store each record as a tuple inside a list. Display all records and search for a student using roll number.

# Conditions:
# Each record should be stored as a tuple.
# The complete database should be stored as a list.
# Roll numbers must be unique.
n = int(input("Enter number of students: "))

database = []

for i in range(n):
    print("\nStudent", i + 1)

    roll = int(input("Enter roll number: "))

    while any(record[0] == roll for record in database):
        print("Roll number already exists!")
        roll = int(input("Enter another roll number: "))

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    record = (roll, name, branch, cgpa)

    database.append(record)

print("\nStudent Database:")

for record in database:
    print(record)

roll = int(input("\nEnter roll number to search: "))

found = False

for record in database:
    if record[0] == roll:
        print("Student found:")
        print(record)
        found = True
        break

if found == False:
    print("Student not found")