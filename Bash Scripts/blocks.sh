#!/bin/bash


# Building Blocks that is inspired in one of the lessons in CS50X


# Blocks function
function blocks(){
	# While loop to execute until a specific condition is met
	while true
	do
		# Ask user for the length and width
		read -p "Length: " LENGTH
		read -p "Width: " WIDTH

		if [[ "$LENGTH" -ge 1 ]] && [[ "$WIDTH" -ge 1 ]]
		then

			# Loop for every rows
			for i in $(seq 1 "$LENGTH")
			do

				# Loop for every lines inside the row
				for j in $(seq 1 "$WIDTH")
				do
					printf "#"
				done

				# Dislay a newline after iteration of inner loop
				printf "\n"

			done

			# Break the loop
			break

		# Ask user again
		else
			echo "Invalid input! Please try again."
			continue

		fi
	done
}

# Reload Function
function reload(){
	# While loop to execute the program until a specific condition is met
	while true
	do
		# Ask user to reload the program
		read -p "Do you want to build a blocks again? (y/n) : " ANSWER

		ANSWER="${ANSWER,,}"

		# Reload the program if yes
		if [[ "$ANSWER" == "y" ]]
		then
			printf "\n"
			blocks

		# Exit the program if no
		elif [[ "$ANSWER" == "n" ]]
		then
			echo "Exiting..."
			break

		# Ask the user again if they enter invalid prompt
		else
			echo "Invalid input!"
			continue

		fi
	done

}

# Execute the functions
blocks
reload
