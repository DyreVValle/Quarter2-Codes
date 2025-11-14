students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

scount = 1
total_average = 0
while scount <= students:
    print("Student", scount)
    subjcount = 1
    sum = 0
    while subjcount <= subjects:
        subjcount = subjcount + 1
        score = int(input("Enter score:"))
        sum += score
    average = sum/subjects
    print("Average for Student", scount,":", average)
    scount = scount + 1
    total_average += average
class_average = total_average/students
print("Class Average:", class_average)