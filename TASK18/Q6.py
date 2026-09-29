#Write a Python program to store one student's data as a tuple: name, roll number, and marks. Display the grade based on marks.
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

student = (name, roll, marks)

print("\nStudent Details:")
print("Name:", student[0])
print("Roll Number:", student[1])
print("Marks:", student[2])

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)