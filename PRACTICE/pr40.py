students = [
    ("Bhawana", 101, 85),
    ("Riya", 102, 72),
    ("Anjali", 103, 90),
    ("Simran", 104, 68),
    ("Neha", 105, 80)
]

print("Students who scored above 75:")

for student in students:
    if student[2] > 75:
        print("Name:", student[0])
        print("Roll Number:", student[1])
        print("Marks:", student[2])
        print()