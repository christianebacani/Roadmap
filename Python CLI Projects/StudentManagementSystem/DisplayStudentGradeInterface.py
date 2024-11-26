import CustomMessagesScript

# Display Student Grade Interface Module 

def displayStudentGradeInterface(studentDict, studentID):
    print("--------------------------------------------")
    print("\t- DISPLAY STUDENT GRADE INTERFACE -\n")

    print(f"\tStudent Full Name : {studentDict[studentID][2]}, {studentDict[studentID][0]} {studentDict[studentID][1]}")
    
    for subject, grade in studentDict[studentID][3].items():
        print(f'\t{subject} : {grade}')
    
    average = float(f'{(sum(studentDict[studentID][3].values()) / len(studentDict[studentID][3].values())):.2f}')
    print(f"\tAverage Grade : {average}")

    print()
    CustomMessagesScript.displayExitMessage()
