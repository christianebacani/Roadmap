# Function to get the second lowest grade per student name
def second_lowest_grade(array_list, scores):
    non_duplicate_score = list(set(scores)) # Remove duplicates to the score

    sorted_scores = sorted(non_duplicate_score) # Sort the scores into ascending order

    second_lowest = sorted_scores[1] # Get the second lowest score

    # Get the student name who has the second lowest grade by comparing their grades
    student_name = [elements[0] for elements in array_list for element in elements if element == second_lowest]
    
    # Sort alphabetially the name of the student's who had a second lowest score
    sorted_student_name = sorted(student_name)

    # Display the student's name who has the second lowest grade, separated by newline
    for name in sorted_student_name:
        print(name)


# Check if the script is running directly
if __name__ == '__main__':
    # Initialize the array
    array = []
    score_array = []

    for i in range(int(input())):
        name = input()
        score = float(input())

        # Store inside an array all the name and score per iteration
        array.append([name, score])

        # Store the scores in another array
        score_array.append(score)

    # Execute the function to get the second lowest grade
    second_lowest_grade(array, score_array)
    