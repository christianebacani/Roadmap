#!/bin/bash


# Linux File System CLI Manager


# Main Interface
function mainInterface(){
	function reload(){
		clear
		ls -l
	}

	while true; do
		echo "-----------------------------------------------------------------"
		printf "\t\tDIRECTORIES\n\n"

		printf "\t\t"
		echo "1.) Parent root"

		printf "\t\t"
        	echo "2.) child root"

		printf "\t\t"
        	echo "3.) scripts"

		printf "\t\t"
        	echo "4.) playground"

		printf "\t\t"
		echo "5.) personal"

		printf "\t\t"
		echo "6.) exit"

		printf "\n\t\t"
		read -p "Enter your option here : " dirOption


		# Check if user's option is invalid
		if [[ "$dirOption" =~ [A-Z-az]+ ]]; then
			reload
			continue

		elif [[ -z "$dirOption" ]]; then
			reload
			continue

		elif [[ "$dirOption" -le 0 ]]; then
			reload
			continue


		elif [[ "$dirOption" -ge 7 ]]; then
			reload
			continue

		fi


		# Change directory and list all the script inside the directory
		if [[ "$dirOption" -eq 1 ]]; then
			cd /


		elif [[ "$dirOption" -eq 2 ]]; then
			cd /root


		elif [[ "$dirOption" -eq 3 ]]; then
			cd /root/scripts


		elif [[ "$dirOption" -eq 4 ]]; then
			cd /root/scripts/playground


		elif [[ "$dirOption" -eq 5 ]]; then
			cd /root/scripts/playground/personal

		else
			# Exit message
			cd /root

			reload
			break

		fi

		reload
		commandInterface

	done
}



# Command Interface
function commandInterface(){
	while true; do
		echo "-----------------------------------------------------------------"
		printf "\t\tCOMMANDS\n\n"

		printf "\t\t"
		echo "1.) Remove"

		printf "\t\t"
		echo "2.) Rename"

		printf "\t\t"
		echo "3.) Moving"

		printf "\t\t"
		echo "4.) Execute"

		printf "\t\t"
		echo "5.) Create/Modify"

		printf "\t\t"
		echo "6.) Change permission"

		printf "\t\t"
		echo "7.) Exit"

		printf "\n\t\t"
		read -p "Choose your commands here : " command


		# Check if the user's choice of commannd is valid
		if [[ "$command" =~ [A-Za-z]+ ]]; then
			reload
			continue

		elif [[ -z "$command" ]]; then
			reload
			continue


		elif [[ "$command" -le 0 ]]; then
			reload
			continue


		elif [[ "$command" -ge 8 ]]; then
			reload
			continue

		fi


		# Exit interface
		if [[ "$command" -eq 7 ]]; then
			cd /root
			reload
			break

		fi


		printf "\t\t"
		read -p "Enter the script name here : " script

		manageScripts "$script" "$command"

		reload
	done
}



# Function to manage script
function manageScripts(){
	local script="$1"
	local command="$2"


	# Remove a scripts
	if [[ "$command" -eq 1 ]] && [[ -f "$script" ]]; then
                rm "$script"


	# Renaming scripts
	elif [[ "$command" -eq 2 ]] && [[ -f "$script" ]]; then
		renameScript "$script"


	# Moving scripts to another directory
	elif [[ "$command" -eq 3 ]] && [[ -f "$script" ]]; then
		moveScript "$script"


	# Execute scripts
	elif [[ "$command" -eq 4 ]] && [[ -f "$script" ]]; then
		clear
		bash "$script"

		read -p "Press any key to load the interface again : "
		clear

	# Create/Edit scripts
	elif [[ "$command" -eq 5 ]] && [[ -n "$script" ]]; then
		createOrModifyScript "$script"


	# Change permissions
	elif [[ "$command" -eq 6 ]] && [[ -f "$script" ]]; then
		reload
		changeScriptPermission "$script"


	else
		printf "\n\t\tInvalid script!\n"

	fi
}



# Rename script
function renameScript(){
	local script="$1"

	printf "\t\t"
	read -p "Enter the new script name : " newScript

	if [[ -n "$newScript" ]]; then
		mv "$script" "$newScript"

	else
		printf "\t\tInvalid file name!\n"

	fi

}



# Move script
function moveScript(){
	local script="$1"

	printf "\t\t"
	read -p "Enter a directory to store your script : " directory


	if [[ -d "$directory" ]]; then
		mv "$script" "$directory"

	else
		printf "\t\t"
		echo "The ${directory} doesn't exist! Please try again."

	fi
}



# Create/Modify scripts
function createOrModifyScript(){
	local script="$1"

	if [[ -n "$script" ]]; then
		nano "$script"

	else
		printf "\t\tInvalid Input! Please try again.\n\t\t"
		read -p "Press enter to load the interface again : "

	fi
}



# Changing script permission
function changeScriptPermission(){
	function invalidInput(){
		printf "\n\t\tInvalid input! Please try again.\n"
	}

	local script="$1"

	echo "-----------------------------------------------------------------"
	printf "\t\tChange Permissions\n\n"

	printf "\t\t"
	echo "Read (r)"

	printf "\t\t"
	echo "Write (w)"

	printf "\t\t"
	echo "Execute (x)"

	printf "\n\t\t"
	read -p "Change file permission here based on the acronyms : " permission

	permission=${permission,,}

	if [[ "$permission" =~ [0-9]+ ]]; then
		invalidInput

	elif [[ "$permission" == "r" ]]; then
		chmod u+r "$script"


	elif [[ "$permission" == "w" ]]; then
		chmod u+w "$script"


	elif [[ "$permission" == "x" ]]; then
		chmod u+x "$script"

	else
		invalidInput

	fi

}


# Execute the main function
clear
mainInterface


