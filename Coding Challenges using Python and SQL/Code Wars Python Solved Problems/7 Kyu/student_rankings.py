# Question: Student Rankings
# Categories: 7 Kyu

def post_grades(students: list[str]) -> list[tuple[str, float]]:
    student_id_and_average_grade = {}

    for i in range(len(students)):
        student_id = students[i].split(' - ')[0]
        student_grades = students[i].split(' - ')[2].split()
        total = 0

        for j in range(len(student_grades)):
            total += float(student_grades[j])
        
        average = total / len(student_grades)
        student_id_and_average_grade[student_id] = average
    
    sorted_average_grades = sorted(list(student_id_and_average_grade.values()), reverse=True)
    result = []

    for i in range(len(sorted_average_grades)):
        for student_id, average in student_id_and_average_grade.items():
            if sorted_average_grades[i] == average:
                result.append(tuple([student_id, average]))
    
    return result