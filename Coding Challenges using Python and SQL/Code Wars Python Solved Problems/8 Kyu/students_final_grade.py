# Question: Student's Final Grade
# Categories: 8 Kyu

def final_grade(exam_grade: int, completed_projects: int) -> int:
    if exam_grade > 90 or completed_projects > 10:
        return 100
    
    elif exam_grade > 75 and completed_projects > 4:
        return 90
    
    elif exam_grade > 50 and completed_projects > 1:
        return 75
    
    else:
        return 0