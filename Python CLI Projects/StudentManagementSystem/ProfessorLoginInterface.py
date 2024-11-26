import ProfessorInterfaceScript
import time

# Professor Log-in Interface Module

def professorLoginInterface(professorAccount, studentDict, studentSubjects):
    count = 0
    while True:
        print("--------------------------------------------")
        print("\t\tLOG IN\n")

        username = input("\tUsername : ")
        password = input("\tPassword : ")
                    
        if (username == professorAccount[0]) and (password == professorAccount[1]):
            ProfessorInterfaceScript.professorInterface(professorAccount, studentDict, studentSubjects)
            break

        count += 1

        if count <= 2:
            print("\tInvalid username or password.")
            input("\tPress any key to load the interface again : ")
            continue

        elif count >= 3 and count <= 5:
            print(f"\tWait for the system to load again. Rate limit ({count} seconds)...")
            time.sleep(count)
            continue
                        
        else:
            print("\tSystem will abort!")
            time.sleep(3)
            print()
            break

        
