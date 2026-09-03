#Take roll number like 2024A1R057 and extract admission year, program code, and roll no digits using slicing
roll_number = input("Enter roll number:")
year = roll_number[:4]
program_code = roll_number[4:7]
roll_no_digits = roll_number[-3:]

print("Admission Year:", year)
print("Program Code:", program_code)
print("Roll Number Digits:", roll_no_digits)