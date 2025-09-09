import CustomMessagesScript

# Manipulate Student Data Interface Module

# Adding Student Data Function
def addStudentData(studentDict, studentSubjects):
    print("--------------------------------------------")
    print("\t- ADD STUDENT DATA -")

    while True:
        try:
            print("\n\tPress only enter key to exit")
            studentID = input("\tStudent ID : ")
    
            if not studentID:
                CustomMessagesScript.displayExitMessage()
                break

            if studentID in studentDict:
                CustomMessagesScript.displayInvalidInputMessage()
                continue

            studentFirstName = input("\tFirst Name : ")
            # String formatting for student's first name
            studentFirstName = [word.lower() for word in studentFirstName.split()]
            studentFirstName = [word.capitalize() for word in studentFirstName]
            studentFirstName = ' '.join(studentFirstName)

            studentMiddleName = input("\tMiddle Name : ")
            # String formatting for student's middle name
            studentMiddleName = [word.lower() for word in studentMiddleName.split()]
            studentMiddleName = [word.capitalize() for word in studentMiddleName]
            studentMiddleName = ' '.join(studentMiddleName)

            studentLastName = input("\tLast Name : ")
            # String formatting for student's last name
            studentLastName = [word.lower() for word in studentLastName.split()]
            studentLastName = [word.capitalize() for word in studentLastName]
            studentLastName = ' '.join(studentLastName)

            gradesDict = {}
            invalidStudentGrade = False

            # Add Grades
            print("\n\tSubject Grades:")
            for subject in studentSubjects:
                addGrade = float(input(f"\t{subject} Grade : "))        

                if (addGrade <= 69.9) or (addGrade >= 100.0):
                    invalidStudentGrade = True
                
                gradesDict[subject] = addGrade

            if invalidStudentGrade:
                CustomMessagesScript.displayInvalidInputMessage()
                continue

            confirm = input("\tPress 'y' to confirm the added student, or 'n' if not : ").lower()

            if (confirm == "y" or confirm == "yes"):
                # studentDict Format = {'studentID' : [FN, MN, LN, {Subject : Grade}]}
                studentDict[studentID] = [studentFirstName, studentMiddleName, studentLastName, gradesDict]
                CustomMessagesScript.displayUpdatingMessage()
                break
        
        except Exception:
            CustomMessagesScript.displayInvalidInputMessage()
            continue


# Delete Student Data Function
def removeStudentData(studentDict):
    print("--------------------------------------------")
    print("\t- DELETE STUDENT DATA -")

    while True:
        print("\n\tPress only enter key to exit")
        studentID = input("\tStudent ID : ")

        if not studentID:
            CustomMessagesScript.displayExitMessage()
            break
        
        elif studentID not in studentDict:
            CustomMessagesScript.displayInvalidInputMessage()
            continue
        
        confirm = input("\tPress 'y' to confirm to remove the student's data, press 'n' if not : ").lower()

        if confirm == "y" or confirm == "yes":
            del studentDict[studentID]
            CustomMessagesScript.displayDeletingMessage()
            break


# Update Student Data
def updateStudentData(studentDict, studentSubjects):
    print("--------------------------------------------")
    print("\t- UPDATE STUDENT DATA -")
    
    while True:
        try:
            print("\n\tPress only enter key to exit")
            studentID = input("\tStudent ID: ")

            if not studentID:
                CustomMessagesScript.displayExitMessage()
                break
        
            elif studentID not in studentDict:
                CustomMessagesScript.displayInvalidInputMessage()
                continue

            newStudentFirstName = input("\tNew First Name : ")
            # String formatting for student's first name
            newStudentFirstName = [word.lower() for word in newStudentFirstName.split()]
            newStudentFirstName = [word.capitalize() for word in newStudentFirstName]
            newStudentFirstName = ' '.join(newStudentFirstName)

            newStudentMiddleName = input("\tNew Middle Name : ")
            # String formatting for student's middle name
            newStudentMiddleName = [word.lower() for word in newStudentMiddleName.split()]
            newStudentMiddleName = [word.capitalize() for word in newStudentMiddleName]
            newStudentMiddleName = ' '.join(newStudentMiddleName)

            newStudentLastName = input("\tNew Last Name : ")
            # String formatting for student's last name
            newStudentLastName = [word.lower() for word in newStudentLastName.split()]
            newStudentLastName = [word.capitalize() for word in newStudentLastName]
            newStudentLastName = ' '.join(newStudentLastName)
            
            gradesDict = {}
            invalidStudentGrade = False

            print("\n\tSubject Grades:")
            for subject in studentSubjects:
                updateGrade = float(input(f'\t{subject} Grade : '))
                
                if (updateGrade <= 69.9) or (updateGrade >= 100.00):
                    invalidStudentGrade = True

                gradesDict[subject] = updateGrade
 
            if invalidStudentGrade:
                CustomMessagesScript.displayInvalidInputMessage()
                continue

            confirm = input("\tPress 'y' to confirm the added subject, or 'n' if not : ").lower()

            if (confirm == "y" or confirm == "yes") and (not invalidStudentGrade):
                CustomMessagesScript.displayUpdatingMessage()
                studentDict[studentID] = [newStudentFirstName, newStudentMiddleName, newStudentLastName, gradesDict]
                break

        except Exception:
            CustomMessagesScript.displayInvalidInputMessage()
            continue