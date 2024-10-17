#!/bin/bash


# CLI for Managing Directories in Linux using Bash


# Main Function
function main(){

	echo "Changing/Managing Directory Bash Script!"

	# Press enter to start
	read -p "Press any key to start: " START

	# Execute the function to manage directory
	manage_dir
}


# Change Directory Function
function manage_dir(){

	while true
	do
	 	# Options to choose of different directory
	        echo "Directories:"
		echo "1.) Parent"
        	echo "2.) Root"
        	echo "3.) Scripts"
        	echo "4.) Playground"
        	echo "5.) Exit"

		read -p "Enter your option here : " OPTION

		# Check if user's choice is valid
		if [[ "$OPTION" -ge 1 ]] && [[ "$OPTION" -le 5 ]]
		then
			# Change directory and list all the script inside the directory
			if [[ "$OPTION" -eq 1 ]]
			then
				cd /


			elif [[ "$OPTION" -eq 2 ]]
			then
				cd /root


			elif [[ "$OPTION" -eq 3 ]]
			then
				cd /root/scripts


			elif [[ "$OPTION" -eq 4 ]]
			then
				cd /root/scripts/playground

			else
				# Exit message

				echo "Exiting..."

				break

			fi


			# Clear past CLI Interactions and display the scripts in long listing format in the current directory

			clear
			ls -l

			# Execute manage directory function
			manage_directory


		# Ask user again if it's invalid choice
		else
			echo "Invalid input!"


		fi

	done

}


# Modifying Directory Function
function manage_directory(){

	while true
	do
		# Options
		echo "Choose Directory Commands"
		echo "1.) Remove script"
		echo "2.) Rename script"
		echo "3.) Moving script"
		echo "4.) Execute script"
		echo "5.) Edit/Create a script"
		echo "6.) Change permission for a script"
		echo "7.) Exit Interface"

		read -p "Choose your commands here : " COMMAND # User Choose any command

		# Check if the user's choice of commannd is valid
		if [[ "$COMMAND" -ge 1 ]] && [[ "$COMMAND" -le 7 ]]
		then
			# Manage script

			if [[ "$COMMAND" -ge 1 ]] && [[ "$COMMAND" -le 6 ]]
			then

				# User enters the script name
				read -p "Enter the script name here : " SCRIPT

				# Execute the manage script function
				manage_script "$SCRIPT" "$COMMAND"

				# Command to clear the past interactions of CLI Interface in shell environment
				clear

				# Display all the scripts inside the directory in long listing format
				ls -l


			# Exit interface
			else

				echo "Exiting..."
				break

			fi


		else
			# Display a message when user enters invalid prompt
			echo "Invalid input!"

		fi
	done
}


# Function to manage script
function manage_script(){

	local LOCAL_SCRIPT="$1" # Argument of the user's script choice

	local LOCAL_COMMAND="$2" # Argument of the user's option


	# Check if the script is a valid script name
	if [[ ${#LOCAL_SCRIPT} -ge 1 ]] # Check if the script is not null
	then

		# Remove a script

		if [[ "$LOCAL_COMMAND" -eq 1 ]]
		then

			# Command to remove script from the directory
                        rm "$LOCAL_SCRIPT"


		# Renaming script

		elif [[ "$LOCAL_COMMAND" -eq 2 ]]
		then

			# User enters the new script name
			read -p "Enter the new script name : " NEW_SCRIPT

			if [[ ${#NEW_SCRIPT} -ge 1 ]] # Check if the new script is not null
			then
				# Command to rename the script
				mv "$LOCAL_SCRIPT" "$NEW_SCRIPT"

			else
				# Invalid message when user writes invalid script name
				echo "Invalid file name!"

			fi


		# Moving script to another directory

		elif [[ "$LOCAL_COMMAND" -eq 3 ]]
		then

			# User enters the directory to store the script
			read -p "Enter a directory to store your specific script : " DIRECTORY


			# Check if the directory is a valid directory or existing
			if [[ "$DIRECTORY" == "/root/scripts/playground" ]] || [[ "$DIRECTORY" == "/root/scripts" ]] || [[ "$DIRECTORY" == "/root" ]]
			then
				# Command to move script to another directory
				mv "$LOCAL_SCRIPT" "$DIRECTORY"


			else
				# Display message when user writes invalid directory
				echo "Invalid directory!"

			fi


		# Execute script/s

		elif [[ "$LOCAL_COMMAND" -eq 4 ]]
		then
			# Command to execute script

			. "$LOCAL_SCRIPT"

			# Ask user to reload the interface
			read -p "Press any key to load the Command Line Interface again: "


		# Create or edit script/s
		elif [[ "$LOCAL_COMMAND" -eq 5 ]]
		then
			# Edit or open a new script

			nano "$LOCAL_SCRIPT"


		# Change permissions
		else
			# Permission options

			echo "Permission options"
			echo "Read (r)"
			echo "Write (w)"
			echo "Execute (x)"


			# User writes the permission
			read -p "Enter your choice here based on the letter of command : " PERMISSION

			if [[ "$PERMISSION" == "r" ]] || [[ "$PERMISSION" == "w" ]] || [[ "$PERMISSION" == "x" ]]
			then

				# Command to change permission
				chmod u+"${PERMISSION}" "$LOCAL_SCRIPT"

			else
				# Display a message when user enters invalid permission

				echo "Invalid permission!"


			# Ask user to press any key to load the interface again

			read -p "Press any key to load the interface again : "


			fi

		fi

	else

		# Display a message when user writes an invalid script
		echo "Invalid script!"

	fi
}


# Execute the function
main

