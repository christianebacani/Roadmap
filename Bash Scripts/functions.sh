#!/bin/bash


# Organizing Functions in Bash (Bourne Again Shell)


# Ask the user
function ask_user(){
while true
do
        read -p "How many times do you want your cat to meow? : " NUMBER

        if [[ "$NUMBER" -ge 1 ]]

        then
                make_sound "$NUMBER"

                break
        else
                echo "No Meow"

                continue

        fi
done
}


# Main function
function make_sound(){

        # Argument
        local USER_NUMBER="$1"

        for i in $(seq 1 "$USER_NUMBER")
        do
                # Execute the meow function
                meow

        done
}


# Meow function
function meow(){

        echo "Meow"

}


# Function to try again
function try_again(){
while true
do
        read -p "Do you want to try again our program? (y/n) : " ANSWER

        ANSWER="${ANSWER,,}"

        if [[ "$ANSWER" == "y" ]]
        then

                ask_user

        elif [[ "$ANSWER" == "n" ]]
        then

                echo "Exiting..."
                break

        else

                echo "Invalid Input!"

                continue
        fi
done
}

# Execute the main functions
ask_user
try_again

