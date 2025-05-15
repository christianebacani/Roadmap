# Question: How good are you really?
# Categories: 8 Kyu

def better_than_average(class_points, your_points) -> bool:
    total_points = 0
    total_students = len(class_points)

    for i in range(len(class_points)):
        total_points += class_points[i]

    average_points = round(total_points / total_students)

    if your_points > average_points:
        return True
    
    return False