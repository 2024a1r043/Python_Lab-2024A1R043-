#Write a python program to determine whether a student is eligible for a scholarship
#The scholarship should be granted if the student satisfies either of the following conditions:
#a, the student has a cgpa of 8.5 or above and attendance of 85 percent or above
#b, the student has won a national-level competition
#The program should take cgpa,attedance percentage, and national-level  competition status as input, then display whether the student is eligible for a scholarship
Cgpa = float(input("Enter student's CGPA:"))
attendance_percentage = float(input("Enter student's attendance percentage:"))
competition_status = input("Enter competition status:").lower()

if (Cgpa >= 8.5 and attendance_percentage >= 85) or competition_status == "won":
    print("Student is eligible for a scholarship.")
else:
    print("Student is not eligible for a scholarship.")



