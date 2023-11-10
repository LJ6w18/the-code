def obtain_grade(average):
    if average >= 84.5:
        grade = 'A+'
    elif average >= 79.5:
        grade = 'A'
    elif average >= 74.5:
        grade = 'B+'
    elif average >= 69.5:
        grade = 'B'
    elif average >= 64.5:
        grade = 'C+'
    elif average >= 59.5:
        grade = 'C'
    elif average >= 54.5:
        grade = 'D+'
    elif average >= 49.5:
        grade = 'D'
    else:
        grade = 'F'
    return grade

mark_list = [['Mary', 90.5], ['Charles', 60.4], ['John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]

print("Student Name\tmark\tGrade")
for student in mark_list:
    name = student[0]
    mark = student[1]
    grade = obtain_grade(mark)
    print(f"{name}\t\t{mark}\t{grade}")
