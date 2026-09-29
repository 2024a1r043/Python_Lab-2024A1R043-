#Write a Python program to store multiple student records as a list of tuples. Each tuple should contain name, roll number, and marks. Display students who scored above 75 marks.
n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    student = (name, roll, marks)
    students.append(student)

print("\nStudents who scored above 75:")

for student in students:
    if student[2] > 75:
        print("Name:", student[0])
        print("Roll Number:", student[1])
        print("Marks:", student[2])
        print()