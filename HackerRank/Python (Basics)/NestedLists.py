# Function to get the second lowest grade per student name
def get_second_lowest_grade(array_list, scores):
    non_duplicate_score = list(set(scores)) # Remove duplicates to the score

    sorted_scores = sorted(non_duplicate_score) # Sort the scores into ascending order

    second_lowest = sorted_scores[1] # Get the second lowest score

    student_name = [] # Initialize student_name array to store student name of second lowest score

    # For loop to check every element
    for i in array_list:    
        for j in i:
            if j == second_lowest: # Get the student name of every iteration that is equal to the second lowest value
                student_name.append(i[0])

    # Sort alphabetially the name of the student's who had a second lowest score
    sorted_student_name = sorted(student_name)

    # Display the student's name, separated by newline
    for i in sorted_student_name:
        print(i)



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

    # Execute the function
    get_second_lowest_grade(array, score_array)
    