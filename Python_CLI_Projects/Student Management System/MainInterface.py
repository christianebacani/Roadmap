import ProfessorLoginInterface
import StudentLoginInterface
import CustomMessagesScript

# Main Interface Module

def mainInterface():
    professorAccount = ['admin', 'admin'] # Professor's account
    studentDict = {} # Student's Data
    studentSubjects = ['Mathematics', 'Science', 'English', 'Araling Panlipunan', 'Mapeh'] # Student's Subject Data
    
    while True:
        try:
            print("--------------------------------------------")
            print("\t- Student Management System -\n")
    
            options = ['Professor', 'Student', 'Exit']

            for index, option in enumerate(options):
                print(f"\t{index + 1}. {option}")
    
            userOption = int(input("\n\tEnter Option: "))
            userOption -= 1

            if options[userOption] == 'Professor':
                ProfessorLoginInterface.professorLoginInterface(professorAccount, studentDict, studentSubjects)

            elif options[userOption] == 'Student':
                print("\tTo be developed...")
                StudentLoginInterface.studentLoginInterface(studentDict)

            elif options[userOption] == 'Exit':
                print("--------------------------------------------")
                break

            else:
                CustomMessagesScript.displayInvalidInputMessage()
                continue
        
        except Exception:
            CustomMessagesScript.displayInvalidInputMessage()
            continue


if __name__ == "__main__":
    mainInterface()
    
