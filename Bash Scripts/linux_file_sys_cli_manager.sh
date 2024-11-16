#!/bin/bash

# Linux File System CLI Manager

# TODO : Rename the variables to follow global naming conventions

# Main Function
function main(){
	read -p "Press any key to start: " START

	clear
	manage_dir
}


# Change Directory Function
function manage_dir(){
	function reload(){
		clear
		ls -l
	}

	while true
	do
		printf "\n"
		echo "-----------------------------------------------------------------"
		printf "\t\tDIRECTORIES\n\n"

		echo "1.) Parent root"
        	echo "2.) child root"
        	echo "3.) scripts"
        	echo "4.) playground"
			echo "5.) personal"
        	echo "6.) exit"

		read -p "Enter your option here : " OPTION

		# Check if user's option is invalid
		if [[ "$OPTION" -le 0 ]] && [[ "$OPTION" -ge 7 ]]; then 
			reload
			continue

		elif [[ "$OPTION" =~ [A-Za-z]+ ]]; the 
			reload 
			continue
	
		fi


		# Change directory and list all the script inside the directory
		if [[ "$OPTION" -eq 1 ]]; then
			cd /


		elif [[ "$OPTION" -eq 2 ]]; then
			cd /root


		elif [[ "$OPTION" -eq 3 ]]; then
			cd /root/scripts


		elif [[ "$OPTION" -eq 4 ]]; then
			cd /root/scripts/playground


		elif [[ "$OPTION" -eq 5 ]]; then
			cd /root/scripts/playground/personal

		else
			# Exit message
			printf "\n\t\tEXITING\n"

			echo "-----------------------------------------------------------------"
			cd /root
			reload

			break


		fi

		reload
		manage_directory

	done
}


# Modifying Directory Function
function manage_directory(){
	while true; do
		printf "\n"
		echo "-----------------------------------------------------------------"
		printf "\t\tCOMMANDS\n\n"

		echo "1.) Remove"
		echo "2.) Rename"
		echo "3.) Moving"
		echo "4.) Execute"
		echo "5.) Create/Modify"
		echo "6.) Change permission"
		echo "7.) Exit"

		read -p "Choose your commands here : " COMMAND

		# Check if the user's choice of commannd is valid
		if [[ "$COMMAND" -le 0 ]] && [[ "$COMMAND" -ge 8 ]] || [[ "$COMMAND" =~ [A-Za-z]+ ]]; then
			reload
			continue

		fi


		# Exit interface
		if [[ "$COMMAND" -eq 7 ]]; then
			break

		fi


		read -p "Enter the script name here : " SCRIPT

		manage_script "$SCRIPT" "$COMMAND"
		reload

	done
}


# Function to manage script
function manage_script(){
	local LOCAL_SCRIPT="$1"
	local LOCAL_COMMAND="$2"


	# Remove a script
	if [[ -f "$LOCAL_SCRIPT" ]] && [[ "$LOCAL_COMMAND" -eq 1 ]]; then
                rm "$LOCAL_SCRIPT"


	# Renaming script
	elif [[ -f  "$LOCAL_SCRIPT" ]] && [[ "$LOCAL_COMMAND" -eq 2 ]]; then
		renameScript "$1"


	# Moving script to another directory
	elif [[ -f "$LOCAL_SCRIPT" ]] && [[ "$LOCAL_COMMAND" -eq 3 ]]; then
		moveScript "$LOCAL_SCRIPT"

	# Execute script/s
	elif [[ -f "$LOCAL_SCRIPT" ]] && [[ "$LOCAL_COMMAND" -eq 4 ]]; then
		bash "$LOCAL_SCRIPT"
		read -p "Press any key to load the Command Line Interface again: "


	# Create/Edit script/s
	elif [[ "$LOCAL_COMMAND" -eq 5 ]]
	then
		createOrModifyScript "$LOCAL_SCRIPT"


	# Change permissions
	else

		changeScriptPermission "$LOCAL_SCRIPT"

	fi
}



# Rename script
function renameScript(){
	local LOCAL_SCRIPT="$1"

	read -p "Enter the new script name : " NEW_SCRIPT

	if [[ -n "$NEW_SCRIPT" ]]; then
		mv "$LOCAL_SCRIPT" "$NEW_SCRIPT"

	else
		echo "Invalid file name!"

	fi

}



# Move script
function moveScript(){
	local LOCAL_SCRIPT="$1"

	read -p "Enter a directory to store your script : " DIRECTORY


	if [[ -d "$DIRECTORY" ]]; then
		mv "$LOCAL_SCRIPT" "$DIRECTORY"

	else
		echo "The ${DIRECTORY} doesn't exist! Please try again."

	fi
}



# Create/Modify script
function createOrModifyScript(){
	local LOCAL_SCRIPT="$1"

	if [[ -n "$LOCAL_SCRIPT" ]]; then
		nano "$LOCAL_SCRIPT"

	else
		echo "Invalid Input! Please try again."
		read -p "Press enter to load the interface again : "

	fi
}



# Changing script permission
function changeScriptPermission(){
	function invalidInput(){
		echo "Invalid input! Please try again."
		read -p "Press any key to load the interface again : "

	}

	local LOCAL_SCRIPT="$1"

	echo "-----------------------------------------------------------------"
	printf "\t\tChange Permissions\n\n"

	echo "Read (r)"
	echo "Write (w)"
	echo "Execute (x)"

	read -p "Change file permission here based on the acronyms : " PERMISSION

	PERMISSION=${PERMISSION,,}

	if [[ "$PERMISSION" =~ [0-9]+ ]]; then
		invalidInput

	elif [[ "$PERMISSION" == "r" ]]; then
		chmod u+r "$LOCAL_SCRIPT"


	elif [[ "$PERMISSION" == "w" ]]; then
		chmod u+w "$LOCAL_SCRIPT"


	elif [[ "$PERMISSION" == "x" ]]; then
		chmod u+x "$LOCAL_SCRIPT"

	else
		invalidInput

	fi

}


# Execute the function
main

