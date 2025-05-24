# Question: Check the exam
# Categories: 7 Kyu

def check_exam(correct_answers: list[str], student_answers: list[str]) -> int:
    total_points = 0

    for i in range(len(correct_answers)):
        if student_answers[i] == '':
            continue

        if correct_answers[i] == student_answers[i]:
            total_points += 4
        
        else:
            total_points -= 1
    
    if total_points < 0:
        return 0
    
    return total_points