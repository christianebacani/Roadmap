import pandas as pd
import CustomMessagesScript

# Print Grade Interface Module

def printGradeInterface(studentDict, studentID):
    while True:
        try:
            print("--------------------------------------------")
            print("\t- PRINT GRADE INTERFACE -\n")
    
            printGrade = input('\tDo you want to print your grade (y/n)?: ').lower()

            if (printGrade == 'y') or (printGrade == 'yes'):                
                average = float(f'{(sum(studentDict[studentID][3].values()) / len(studentDict[studentID][3].values())):.2f}')

                student_df = pd.DataFrame({'First Name' : studentDict[studentID][0],
                                           'Middle Name' : studentDict[studentID][1],
                                           'Last Name' : studentDict[studentID][2],
                                           'Mathematics' : studentDict[studentID][3]['Mathematics'],
                                           'Science' : studentDict[studentID][3]['Science'],
                                           'English' : studentDict[studentID][3]['English'],
                                           'Araling Panlipunan' : studentDict[studentID][3]['Araling Panlipunan'],
                                           'Mapeh' : studentDict[studentID][3]['Mapeh'],
                                           'GWA' : average}, index=[0])
            
                target_fileath = f'Student Management System\\Students Data\\{studentDict[studentID][2]}GradesData.csv'
                
                student_df.to_csv(target_fileath, index=False)                                                               
                CustomMessagesScript.displayPrintMessage()

                break
            
            elif (printGrade == 'n') or (printGrade == 'no'):
                CustomMessagesScript.displayExitMessage()
                break

            else:
                CustomMessagesScript.displayInvalidInputMessage()
                continue
        
        except Exception:

            CustomMessagesScript.displayInvalidInputMessage()
            continue
            
        