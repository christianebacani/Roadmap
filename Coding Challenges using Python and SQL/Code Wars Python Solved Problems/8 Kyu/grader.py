# Question: Grader
# Categories: 8 Kyu

def grader(score: float) -> str:
    if score > 1 or score < 0.6:
        return 'F'
    
    elif score >= 0.9:
        return 'A'

    elif score >= 0.8:
        return 'B'
    
    elif score >= 0.7:
        return 'C'
    
    else:
        return 'D'