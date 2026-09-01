#WAP to take marks of three subject out of 100 . print TRue of the srudnet scored at least 40 in all three subjects and average marks are at least 50
marks1 = int(input())
marks2 = int(input())
marks3 = int(input())
average = (marks1+marks2+marks3)//3

print(marks1>40 and marks2>40 and marks3>40 and average >50)