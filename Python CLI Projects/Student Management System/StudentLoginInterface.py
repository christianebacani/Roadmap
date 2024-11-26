import StudentInterface
import CustomMessagesScript

# Student Login Interface Module

def studentLoginInterface(studentDict):
    while True:
        try:
            print("--------------------------------------------")
            print("\t- STUDENT LOGIN INTERFACE -\n")
        
            print("\tPress enter key only to exit : ")
            studentID = input("\tEnter your Student ID : ")

            if not studentID:
                CustomMessagesScript.displayExitMessage()
                break

            elif studentID not in studentDict:
                CustomMessagesScript.displayInvalidInputMessage()
                continue    
                
            StudentInterface.studentInterface(studentDict, studentID)
            break

        except Exception:
            CustomMessagesScript.displayInvalidInputMessage()
            continue