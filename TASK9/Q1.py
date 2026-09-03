#Take student full name and roll number. Generate email using first 3 letters of first name, first 3 letters of last name, and last 3 characters of roll number
name = input("Enter student's full name: ")
roll = input("Enter roll number: ")

parts = name.split()

first_name = parts[0]
last_name = parts[-1]

email = first_name[:3] + last_name[:3] + roll[-3:] + "@mietjammu.in"

print("Generated Email:", email.lower())