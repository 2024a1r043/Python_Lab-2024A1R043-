#Take name , branch, and year. generate a code name using string concatenation, slicing and repetition
name = input("Enter your name: ")
branch = input("Enter your branch: ")
year = input("Enter your year: ")
code_name = name[:3] + "-" + branch[:3] + "-" + year[-2:]
print("*" * 30)
print("Student Code:", code_name) 
print("*" * 30)