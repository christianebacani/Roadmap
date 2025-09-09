import ManageStudentDataInterface
import UpdateProfessorAcccountInterface
import CustomMessagesScript

# Professor Interface Module

def professorInterface(professorAccount, studentDict, studentSubjects):
    professorOptions = ['Manage Student', 'Update Account', 'Exit'] # Professor Options
    
    manageStudentsOptions = ['Add Student', 'Remove Student', 'Update Student', 'Exit'] # Professor's Options for Managing Student Data
    
    while True:
        try:
            print("--------------------------------------------")
            print("\t - PROFESSOR INTERFACE -\n")

            for index, option in enumerate(professorOptions):
                print(f"\t{index +  1}. {option}")
            
            professorChoice = int(input("\n\tOption : "))
            professorChoice -= 1
        
            if professorOptions[professorChoice] == 'Manage Student':
                ManageStudentDataInterface.manageStudentDataInterface(studentDict, studentSubjects, manageStudentsOptions)
        
            elif professorOptions[professorChoice] == 'Update Account':
                UpdateProfessorAcccountInterface.adminUpdateAccountInterface(professorAccount)

            elif professorOptions[professorChoice] == 'Exit':
                CustomMessagesScript.displayExitMessage()
                break
        
            else:
                CustomMessagesScript.displayInvalidInputMessage()
                continue

        except Exception:
            CustomMessagesScript.displayInvalidInputMessage()
            continue
