# Iteration over a list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("List elements:")
for num in numbers:
    print(num)

# Iteration over a dictionary

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")

student = {
    "Name": name,
    "Age": age,
    "Course": course
}

print("Dictionary elements:")
for key, value in student.items():
    print(key, ":", value)