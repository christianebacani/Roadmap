import time

def displayInvalidInputMessage():
    message = '\tInvalid input! Please try again.'

    for char in message:
        time.sleep(0.04)
        print(char, end='')
    print()
    

def displayUpdatingMessage():
    for seconds in range(3, 0, -1):
        time.sleep(1)
        print(f"\tUpdating in {seconds}...")
    time.sleep(1)


def displayDeletingMessage():
    for seconds in range(3, 0, -1):
        time.sleep(1)
        print(f"\tDeleting in {seconds}...")
    time.sleep(1)


def displayExitMessage():
    askUser = '\tPress any key to exit : '    
    
    for char in askUser:
        time.sleep(0.04)
        print(char, end='')
    input()


def displayPrintMessage():
    for seconds in range(3, 0 , -1):
        time.sleep(1)
        print(f"\tPrinting in {seconds}...")
    time.sleep(1)
    
    message = '\tYour data has been successfully printed in excel sheets!\n\tPress any key to exit interface : '

    for char in message:
        time.sleep(0.04)
        print(char, end='')
    input()


