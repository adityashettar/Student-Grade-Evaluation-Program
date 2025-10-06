Marks = float(input("Enter the student marks: "))
if Marks >= 90:
    Grade = 'A'
elif Marks >= 80:
    Grade = 'B'
elif Marks >= 70:
    Grade = 'C'
elif Marks >= 60:
    Grade = 'D'
elif Marks >= 50:
    Grade = 'E'
else:
    Grade = 'F'
print(f"The student grade is:"{Grade})