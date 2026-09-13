name = input("please enter your name: ")
marks1 = int(input("Please enter your 1st marks: "))
marks2 = int(input("Please enter your 2nd marks: "))
marks3 = int(input("Please enter your 3rd marks: "))
total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3


if average_marks >= 80:
    grade = "A+"

elif average_marks >= 70:
    grade = "A"

elif average_marks >= 60:
    grade = "B"

elif average_marks >= 50:
    grade = "C"

else: grade = "F"    

print("Student Name:", name.title(), "Total Marks:", total_marks, "Average Marks:", average_marks, "Grade:", grade)