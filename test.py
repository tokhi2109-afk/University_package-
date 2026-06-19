course_ID = 1002

Grades = [67, 23, 34, 57, 23, 41, 15 ,31, 78, 90, 56, 82, 45, 62, 88, 91, 73, 54, 69, 80 , 77, 84, 92, 58, 63, 70, 81, 49, 55, 66, 74]



student_name = "John Doe"
student_id = "S12345"
email_id = "kjbrobhgw@ojhberojh"




grade_letter = []

for i in Grades:
    if i >= 90:
        grade_letter.append("A")
    elif i >= 80:
        grade_letter.append("B")
    elif i >= 70:
        grade_letter.append("C")
    elif i >= 60:      
        grade_letter.append("D")
    else:
        grade_letter.append("F")  

    



print(f"\n{'=' * 45}")
print(f"  TRANSCRIPT — {student_name} ({student_id})")
print(f"  Email : {email_id}")
print(f"{'=' * 45}")

print(f" Course ID : {(' ') * 10} Grade : {(' ') * 10} Grade Letter : ")

for i in Grades:
    print(f" {(' ') * 3} {course_ID} {(' ') * 15} {i} {(' ') * 20} {grade_letter[Grades.index(i)]}")



print(Grades.index(67))

print(f" Avarage Grade : {course_ID}   -> ({email_id})")

#jhfjkhfkhf kg g lkjg lgf khf khf fkf khf kf hfg 

print("hello world")