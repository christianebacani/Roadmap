import ManipulateStudentDataInterface
import CustomMessagesScript

# Manage Student Data Interface Module

def manageStudentDataInterface(studentDict, studentSubjects, manageStudentsOptions):    
    while True:
        try:
            print("--------------------------------------------")
            print("\t- STUDENT DATA -\n")
                    
            if not studentDict:
                print(f"\tNo Student Data Yet...\n")
            
            else:
                # Display the Student`s Data from Dictionary
                for studentID, studentData in studentDict.items():
                    print(f"\t{studentID} : {studentData[2]}, {studentData[0]} {studentData[1][0]}.")

                    for subject in studentSubjects:
                        print(f"\t{subject} : {studentDict[studentID][3][subject]}\t")
                    print()
                    
            input("\tPress any key to load the interface : ")

            print("--------------------------------------------")
            print("\t- MANAGE STUDENT DATA -\n")

            for number, option in enumerate(manageStudentsOptions):
                print(f"\t{number + 1}. {option}")
    
            choice = int(input("\n\tOption : "))
            choice -= 1

            if (manageStudentsOptions[choice] == manageStudentsOptions[0]):
                ManipulateStudentDataInterface.addStudentData(studentDict, studentSubjects)

            elif (manageStudentsOptions[choice] == manageStudentsOptions[1]):
                ManipulateStudentDataInterface.removeStudentData(studentDict)

            elif (manageStudentsOptions[choice] == manageStudentsOptions[2]):
                ManipulateStudentDataInterface.updateStudentData(studentDict, studentSubjects)

            elif (manageStudentsOptions[choice] == manageStudentsOptions[3]):
                CustomMessagesScript.displayExitMessage()
                break 

            else:
                CustomMessagesScript.displayInvalidInputMessage()
                            
        except Exception:
            CustomMessagesScript.displayInvalidInputMessage()
            