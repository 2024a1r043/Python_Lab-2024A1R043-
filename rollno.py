name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

username = name[:3] + roll_number[-2:]
print("Generated username:", username)