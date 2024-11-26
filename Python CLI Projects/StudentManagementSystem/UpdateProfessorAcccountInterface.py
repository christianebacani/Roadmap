import CustomMessagesScript

# Update Professor Account Interface Module

def updateProfessorAccountInterface(professorAccount):
    while True:
        print("--------------------------------------------")
        print("\t- UPDATE ACCOUNT -\n")

        askProfessor = input("\tDo you want to update your account (y/n)?: ").lower()

        if askProfessor != "y":
            CustomMessagesScript.displayExitMessage()
            break
                
        newUsername = input("\tNew Username : ")
        newPassword = input("\tNew Password : ")

        confirmUpdatedAccount = input("\tPress 'y' to confirm your new account, and 'n' if no: ").lower()

        if confirmUpdatedAccount != "y":
            continue

        professorAccount[0] = newUsername
        professorAccount[1] = newPassword

        CustomMessagesScript.displayUpdatingMessage()
        print("\n\tSuccessfully Updated!")
        break