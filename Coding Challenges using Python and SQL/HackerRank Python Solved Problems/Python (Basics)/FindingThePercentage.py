# Function to get the averages based on student's name
def get_average(marks, name):
    # Get the grade of the specific student
    grades = marks.get(name)
    
    # Initialize a total variable
    total = 0

    # Add all the value of the grade of a specific student
    for grade in grades:
        total += grade
    
    # Get the average
    average = total / 3
    print(f"{average:.2f}") # Round the average value to 2 decimal places


# Check if the script is running directly
if __name__ == "__main__":
    # User enters the length of the dictionary
    dict_length = int(input())

    # Student marks dict
    student_marks = {}
    
    # User enters the key(student name) and three values(grade)
    for i in range(dict_length):
        # Pass to the variable
        student_name, *grade = input().split()
        student_scores = list(map(float, grade)) # Map the grades value to convert it as a float to a list

        student_marks[student_name] = student_scores # Assign the student's name based on their respective grades

    # Enter student name
    student = input()

    # Get the average
    get_average(student_marks, student)






