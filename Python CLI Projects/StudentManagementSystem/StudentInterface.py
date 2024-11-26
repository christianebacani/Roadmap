import PrintGradeInterface
import DisplayStudentGradeInterface
import CustomMessagesScript

# Student Interface Module

def studentInterface(studentDict, studentID):
    studentOptions = ['Print Grade', 'View Grade', 'Exit']
    while True:
        try:
            print("--------------------------------------------")
            print("\t- STUDENT INTERFACE -\n")
            
            for number, options in enumerate(studentOptions):
                print(f"\t{number + 1}.) {options}")

            studentChoice = int(input("\n\tEnter your choice here : "))
            studentChoice -= 1

            if studentOptions[studentChoice] == 'Print Grade':
                PrintGradeInterface.printGradeInterface(studentDict, studentID)
            
            elif studentOptions[studentChoice] == 'View Grade':
                DisplayStudentGradeInterface.displayStudentGradeInterface(studentDict, studentID)
                
            elif studentOptions[studentChoice] == 'Exit':
                CustomMessagesScript.displayExitMessage()
                break

            else:
                CustomMessagesScript.displayInvalidInputMessage()
                continue
        
        except:
            CustomMessagesScript.displayInvalidInputMessage()
            continue
