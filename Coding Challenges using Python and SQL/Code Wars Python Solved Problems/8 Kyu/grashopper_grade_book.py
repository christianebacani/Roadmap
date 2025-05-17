# Question: Grasshopper - Grade book
# Categories: 8 Kyu

def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3

    if average >= 90:
        return 'A'

    elif average >= 80 and average < 90:
        return 'B'
    
    elif average >= 70 and average < 80:
        return 'C'
    
    elif average >= 60 and average < 70:
        return 'D'
    
    else:
        return 'F'