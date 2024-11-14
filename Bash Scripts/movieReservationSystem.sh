#!/bin/bash


# Movie Seat Reservation System in Bash


# Function for Main Interface
function mainInterface(){
	while true; do
		echo "--------------------------------------------------------------"
		printf "\tWelcome to movie seat reservation system!\n\n"

		interfaceOptions=("1.) I am an Admin" "2.) I want to watch movies" "3.) Exit")

		# Display the interface options
		for option in "${interfaceOptions[@]}"; do
			printf "\t\t${option}\n"
		done

		printf "\n\t\t"

		read -p "Option : " userChoice

		if [[ "$userChoice" -eq 1 ]]; then
			adminInterface "${adminData[@]}" "${movieDescriptions[@]}" "${ticketPrices[@]}"

		elif [[ "$userChoice" -eq 2 ]]; then
			clear

			printf "\n"
			echo "--------------------------------------------------------------"
			printf "\t\tMOVIE DESCRIPTIONS\n\n\t\t"

			echo "Title: ${movieDescriptions[0]}"

			printf "\t\t"
			echo "Genre : ${movieDescriptions[1]}"

			printf "\n\t\t"
			echo "TICKET PRICES:"

			printf "\t\t"
			echo "First row : Php ${ticketPrices[0]}.00"

			printf "\t\t"
			echo "Second row : Php ${ticketPrices[1]}.00"

			printf "\t\t"
			echo "Third row : Php ${ticketPrices[2]}.00"

			printf "\t\t"
			echo "Fourth row : Php ${ticketPrices[3]}.00"

			printf "\t\t"
			echo "Fifth row : Php ${ticketPrices[4]}.00"

			printf "\n\t\t"
			read -p "Press any key to load the interface : "

			reserveSeat=1

			totalPrice=0

			customerInterface $reserveSeat "$movieSeats" $totalPrice "${ticketPrices[@]}"

		elif [[ "$userChoice" -eq 3 ]]; then
			echo "Exiting...."
			break

		fi

		clear

	done
}


# Admin Interface
function adminInterface(){
	# Admin interface options
	local adminOptions=("1.) Update Account" "2.) Update Movie" "3.) Exit")

	local count=0

	while true; do
		clear
		echo "--------------------------------------------------------------"
		printf "\t\tLOG-IN INTERFACE\n\n"

		printf "\t\t"
		read -p "Username : " username

		printf "\t\t"
		read -p "Password : " password

		if ( [ "$username" != "${adminData[0]}" ] || [ "$password" != "${adminData[1]}" ] ); then
			count=$(( count + 1 ))

			if [[ "$count" -eq 3 ]]; then
				printf "\n\t\tSystem Abort!\n\t\t"
				read -p "Press any key to load the interface again : "
				break
			fi

			printf "\n\t\tInvalid username or password!\n"

			printf "\t\t"
			read -p "Press any key to load again the interface : "
			continue

		fi

		printf "\n\t\tSuccessfully Logged-In!\n\t\t"
		read -p "Press any key to load the interface : "
		printf "\n"

		while true; do
			clear
			echo "--------------------------------------------------------------"
			printf "\t\tADMIN INTERFACE"
			printf "\n\n"

			for option in "${adminOptions[@]}"; do
				printf "\t\t"
				echo "${option}"
			done

			printf "\n\t\t"
			read -p "Option : " adminOption

			if [[ "$adminOption" -eq 1 ]]; then
				updateAdminAccount "${adminData[@]}"


			elif [[ "$adminOption" -eq 2 ]]; then
				updateMovieDescriptions "${movieDescriptions[@]}" "${ticketPrices[@]}"


			elif [[ "$adminOption" -eq 3 ]]; then
				printf "\n\n\t\t\tExiting..."
				break


			else
				printf "\n\t\t"
				echo "Invalid input! Please try again."
				continue

			fi

		done

		break

	done
}


# Function to update admin account
function updateAdminAccount(){
	while true; do
		printf "\t\t"
		read -p "Do you want to update your account (y/n)?: " updateAccount

		updateAccount=${updateAccount,,}

		if ( [ "$updateAccount" != "y" ] && [ "$updateAccount" != "yes" ] ); then
			break

		fi

		clear
		echo "--------------------------------------------------------------"
		printf "\t\tUPDATE ACCOUNT\n"

		printf "\n\t\t"
		read -p "New Username : " newUsername

		printf "\t\t"
		read -p "New Password : " newPassword


		printf "\t\t"
		read -p "Press 'y' to confirm new account, press 'n' if not : " confirmNewAccount

		confirmNewAccount=${confirmNewAccount,,}


		if ( [ "$confirmNewAccount" != "y" ] && [ "$confirmNewAccount" != "yes" ] ); then
			continue

		fi

		adminData[0]="$newUsername"
		adminData[1]="$newPassword"

		printf "\n\t\tSuccessfully Updated!\n\t\t"
		read -p "Press any key to load the interface : "
		printf "\n"

		break

	done
}


# Function for updating movie descriptions
function updateMovieDescriptions(){
	while true; do
		printf "\t\t"
		read -p "Do you want to update the movie descriptions (y/n)?: " updateMovie

		updateMovie=${updateMovie,,}

		if ( [ "$updateMovie" != "y" ] && [ "$updateMovie" != "yes" ] ); then
			break

		fi

		clear
		echo "--------------------------------------------------------------"
		printf "\t\tUPDATE MOVIE DESCRIPTIONS\n\t\t"


		printf "\n\t\t"
		read -p "Movie Name : " newMovieName

		printf "\t\t"
		read -p "Movie Genre : " newMovieGenre

		printf "\n\t\t"
		echo "Ticket Prices"

		printf "\t\t"
		read -p "First row ticket price : Php " firstRowTicketPrice

		printf "\t\t"
		read -p "Second row ticket price : Php " secondRowTicketPrice

		printf "\t\t"
		read -p "Third row ticket price : Php " thirdRowTicketPrice


		printf "\t\t"
		read -p "Fourth row ticket price : Php " fourthRowTicketPrice

		printf "\t\t"
		read -p "Fifth row ticket price : Php " fifthRowTicketPrice


		printf "\t\t"
		read -p "Press 'y' to confirm the new movie, press 'n' if not : " confirmNewMovieDescriptions

		confirmNewMovieDescriptions=${confirmNewMovieDescriptions,,}


		if ( [ "$confirmNewMovieDescriptions" != "y" ] && [ "$confirmNewMovieDescriptions" != "yes" ] ); then
			continue

		fi

		movieDescriptions[0]="$newMovieName"
		movieDescriptions[1]="$newMovieGenre"
		movieDescriptions[2]=$newMoviePrice
		ticketPrices[0]="$firstRowTicketPrice"
		ticketPrices[1]="$secondRowTicketPrice"
		ticketPrices[2]="$thirdRowTicketPrice"
		ticketPrices[3]="$fourthRowTicketPrice"
		ticketPrices[4]="$fifthRowTicketPrice"


		printf "\n\t\tSuccessfully Updated!\n\t\t"
		read -p "Press any key to exit interface : "
		break

	done
}


# Function for user interface
function customerInterface(){
	while true; do
		if [[ $reserveSeat -eq 0 ]]; then
			break

		fi

		clear
		echo "--------------------------------------------------------------"
		printf "\t\tCUSTOMER INTERFACE\n"

		printf "\n\t${columnSeats[*]}"
		printf "\n\t${firstRowMovieSeats[*]}"
		printf "\n\t${secondRowMovieSeats[*]}"
		printf "\n\t${thirdRowMovieSeats[*]}"
		printf "\n\t${fourthRowMovieSeats[*]}"
		printf "\n\t${fifthRowMovieSeats[*]}"
		printf "\n\n\t\t"

		printf "Press enter to exit interface\n\t\t"
		read -p "Enter row : " row


		if [[ -z $row ]]; then
			break

		elif [[ $row =~ [A-Za-z_.,?!]+ ]]; then
			continue

		elif [[ $row -le 0 ]] && [[ $row -ge 6 ]]; then
			continue

		fi

		while true; do
			printf "\t\t"
			read -p "Enter column : " column

			if [[ -z $column ]]; then
				break


			elif [[ $column =~ [A-Za-z_.,?!]+ ]]; then
				continue


			elif [[ $column -le 0 ]] && [[ $column -ge 10 ]]; then
				continue

			fi


			if [[ $row -eq 1 ]] && [[ "${firstRowMovieSeats[$column]}" != "[X]" ]]; then
				firstRowMovieSeats[$column]="[X]"
				totalPrice=$(( totalPrice + "${ticketPrices[0]}" ))


			elif [[ $row -eq 2 ]] && [[ "${secondRowMovieSeats[$column]}" != "[X]" ]]; then
				secondRowMovieSeats[$column]="[X]"
				totalPrice=$(( totalPrice + "${ticketPrices[1]}" ))


			elif [[ $row -eq 3 ]] && [[ "${thirdRowMovieSeats[$column]}" != "[X]" ]]; then
				thirdRowMovieSeats[$column]="[X]"
				totalPrice=$(( totalPrice + "${ticketPrices[2]}" ))


			elif [[ $row -eq 4 ]] && [[ "${fourthRowMovieSeats[$column]}" != "[X]" ]]; then
				fourthRowMovieSeats[$column]="[X]"
				totalPrice=$(( totalPrice + "${ticketPrices[3]}" ))


			elif [[ $row -eq 5 ]] && [[ "${fifthRowMovieSeats[$column]}" != "[X]" ]]; then
				fifthRowMovieSeats[$column]="[X]"
				totalPrice=$(( totalPrice + "${ticketPrices[4]}" ))

			else
				printf "\t\tSeat was already taken!\n\n\t"
				read -p "Press any key to load the interface again : "
				printf "\n"

				break

			fi


			clear
			echo "--------------------------------------------------------------"
			printf "\t\tCUSTOMER INTERFACE\n"

			# Display updated seats
			printf "\n\t${columnSeats[*]}"
			printf "\n\t${firstRowMovieSeats[*]}"
			printf "\n\t${secondRowMovieSeats[*]}"
			printf "\n\t${thirdRowMovieSeats[*]}"
			printf "\n\t${fourthRowMovieSeats[*]}"
			printf "\n\t${fifthRowMovieSeats[*]}"

			askUserToReserveMoreSeats $reserveSeat "$movieSeats" $totalPrice "${ticketPrices[@]}"
			break

		done
	done

}


# Function to ask user if they want to reserve more seats
function askUserToReserveMoreSeats(){
	while true; do
		printf "\n\n\t"
		read -p "Do you want to reserve more seats (y/n)?: " reserveMoreSeats

		reserveMoreSeats=${reserveMoreSeats,,}

		if ( [ $reserveMoreSeats != "n" ] && [ $reserveMoreSeats != "no" ] ); then
			customerInterface $reserveSeat "$movieSeats" $totalPrice "${ticketPrices[@]}"
			break

		else
			billingSys $totalPrice

			reserveSeat=0
			totalPrice=0

			customerInterface $reserveSeat "$movieSeats" $totalPrice "${ticketPrices[@]}"
			break

		fi

	done
}


# Billing Function
function billingSys(){
	local totalPrice="$1"

	clear
	echo "--------------------------------------------------------------"
	printf "\t\tBILLING INTERFACE\n\n"

	while true; do
		printf "\t\tTotal Price : Php ${totalPrice}.00\n\t\t"
		read -p "Enter your payment here : Php " userPayment

		if [[ $userPayment -lt $totalPrice ]]; then
			printf "\n\t\tInsufficient Money!\n\t\t"
			read -p "Press any key to load the interface : "
			printf "\n"

		else
			change=$(( $userPayment - $totalPrice ))
			printf "\n\t\tChange : Php ${change}.00\n\t\t"

			read -p "Press any key to load the interface : "
			break
		fi
	done
}


adminData=("admin" "admin")

columnSeats=(" " " 1 " " 2 " " 3 " " 4 " " 5 " " 6 " " 7 " " 8 " " 9 " " 10 ")
firstRowMovieSeats=("1" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
secondRowMovieSeats=("2" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
thirdRowMovieSeats=("3" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
fourthRowMovieSeats=("4" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
fifthRowMovieSeats=("5" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")

movieSeats=("${columnSeats[@]}" "${firstRowMovieSeats[@]}" "${secondRowMovieSeats[@]}" "${thirdRowMovieSeats[@]}" "${fourthRowMovieSeats[@]}" "${fifthRowMovieSeats[@]}")	

movieDescriptions=("Venom : The Last Dance" "Sci-Fi, Action, and Horror")
ticketPrices=(500 450 400 350 300)



clear
mainInterface "${adminData[@]}" "${movieSeats[@]}" "${movieDescriptions[@]}" "${ticketPrices[@]}"
clear

