# Check Username Function
def username_match():
    while True:
        # Ask user for their username
        username = str(input("Enter your username : "))

        # Proceed to next function if user enters correct username
        if username in registered_usernames:
            password_match()
            break
        
        # Ask for the username again
        else:
            print("Wrong username! Please try again.")
            continue


# Check Password Function
def password_match():
    while True:
        # Ask user for their password
        password = str(input("Please enter your password : "))

        # Exit the condition if username enters correct password
        if password in registered_passwords:
            print("Access Granted")
            break
        
        # Ask the user again if they entered incorrect password
        else:
            print("Wrong password! Please try again.")
            continue
        

# Login Function
def login():
    print("\nWelcome to Login Page!")
    # Username Prompt
    username = str(input("Enter your username : "))
    
    # Check if the username is correct and proceed to next block of code
    while True:
        # If username is correct, ask user for their password
        if username in registered_usernames:
            password = str(input("Enter your password : "))

            # Display a message when user enters correct password
            if password in registered_passwords:
                print("Access Granted")

            # If password is incorrect, proceed to password_match function to ask again the user for their password
            else:
                print("Wrong password! Please try again.")
                password_match()

        # If username is incorrect, ask the user again using the username_match function
        else:
            print("Wrong username! Please try again.")
            username_match()
        
        # Exit the function if the user correctly enters username and password
        break


# Registration Funtion
def register():
    print("\nWelcome to Registration Page!")
    # User creates username and password
    create_username = str(input("Create your username here : "))
    create_password = str(input("Create your password here : "))

    while True:
        # User enters the password again to confirm
        confirm_password = str(input("Confirm your password here : "))

        # Store the newly created username and password to the array
        if confirm_password == create_password:
            registered_usernames.append(create_username)
            registered_passwords.append(create_password)

            # Display a message after successfully registration
            print("Successfully Registered!")
            break
        
        # Ask user again after incorrect match to the created password
        else:
            print("Incorrect Password! Please try again.")
            continue


# Main function
if __name__ == "__main__":
    # Welcome message
    print("Welcome to my Simple Registration and Login Python Script!")

    # While loop always ask user to enter their choice
    while True:
        # Available Features
        options = ['Login', 'Register']

        # Display the options
        for i, option in enumerate(options):
            print(f"{i + 1}.) {option}")

        # Ask user to choose their option
        userchoice = str(input("Enter your choice here : "))

        # Array to store the data of the registered usernames and passwords (applicable also in newly registered username and passwords)
        registered_usernames = ["Christiane"]
        registered_passwords = ["12-04-2003"]

        # Load Login Function
        if userchoice == "1":
            print()
            login()

        # Load Register Funtion and Login Function after registered username and password
        elif userchoice == "2":
            register()

            login()

        # Ask user again if they enter invalid prompt
        else:
            print("Invalid choice! Please try again.")
            continue
        
        # Exit the program after Login or Register Function
        break




