#Write a Python program to create records of n students. Store each student record as a dictionary containing roll number, name, branch, and marks. Store all records in a list and search for a student using roll number. Roll numbers must be unique.
n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    roll = int(input("Enter roll number: "))

    while any(s["roll"] == roll for s in students):
        print("Roll number already exists!")
        roll = int(input("Enter another roll number: "))

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

print("\nStudent Records:")

for student in students:
    print(student)

roll = int(input("\nEnter roll number to search: "))

found = False

for student in students:
    if student["roll"] == roll:
        print("Student found:")
        print(student)
        found = True
        break

if found == False:
    print("Student not found")