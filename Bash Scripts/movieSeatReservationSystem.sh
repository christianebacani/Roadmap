#!/bin/bash


# Movie Seat Reservation System in Bash


# Function for Main Interface
function mainInterface(){
	while true; do
		echo "--------------------------------------------------------------"
		printf "\t\tMOVIE SEAT RESERVATION SYSTEM\n\n"

		mainInterfaceOptions=("1.) I am an Admin" "2.) I want to watch movies" "3.) Exit")

		# Display the interface options
		for option in "${mainInterfaceOptions[@]}"; do
			printf "\t\t${option}\n"
		done

		printf "\n\t\t"

		read -p "Option : " userChoice


		if [[ "$userChoice" -eq 1 ]]; then
			adminLoginInterface "${adminData[@]}" "${movie1Descriptions[@]}" "${movie1TicketPrices[@]}" "${movie2Descriptions[@]}" "${movie2TicketPrices[@]}" "${movie3Descriptions[@]}" "${movie3TicketPrices[@]}"


		elif [[ "$userChoice" -eq 2 ]]; then
			clear

			displayMoviesDataInterface "${movie1Descriptions[@]}" "${movie1TicketPrices[@]}" "${movie2Descriptions[@]}" "${movie2TicketPrices[@]} ${movie3Descriptions} ${movie3TicketPrices[@]}"

			customerInterface "${movie1Seats[@]}" "${movie1TicketPrices[@]}" "${movie2Seats[@]}" "${movie2TicketPrices[@]}" "${movie3Seats[@]}" "${movie3TicketPrices[@]}"


		elif [[ "$userChoice" -eq 3 ]]; then
			echo "Exiting..."
			break

		fi

		clear
	done
}



# Admin Interface
function adminLoginInterface(){
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

			if [[ $count -eq 3 ]]; then
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

		adminInterface "${adminData[@]}" "${movie1Descriptions[@]}" "${movie1TicketPrices[@]}" "${movie2Descriptions[@]}" "${movie2TicketPrices[@]}" "${movie3Descriptions[@]}" "${movie3TicketPrices[@]}"
		break
	done
}



# Function for Admin Interface
function adminInterface (){
	local adminInterfaceOptions=("1.) Update Account" "2.) Update Movie" "3.) Exit")

	while true; do
		clear
		echo "--------------------------------------------------------------"
		printf "\t\tADMIN INTERFACE"
		printf "\n\n"

		for option in "${adminInterfaceOptions[@]}"; do
			printf "\t\t"
			echo "${option}"
		done

		printf "\n\t\t"
		read -p "Option : " adminChoice


		if [[ "$adminChoice" -eq 1 ]]; then
			updateAdminAccountInterface "${adminData[@]}"


		elif [[ "$adminChoice" -eq 2 ]]; then
			updateMovieDataInterface "${movie1Descriptions[@]}" "${movie1TicketPrices[@]}" "${movie2Descriptions[@]}" "${movie2TicketPrices[@]}" "${movie3Descriptions[@]}" "${movie3TicketPrices[@]}"


		elif [[ "$adminChoice" -eq 3 ]]; then
			printf "\n\n\t\t\tExiting..."
			break

		else
			continue

		fi

	done
}



# Function to update admin account
function updateAdminAccountInterface(){
	while true; do
		clear
		echo "--------------------------------------------------------------"
		printf "\t\tUPDATE ACCOUNT\n\n"

		printf "\t\t"
		read -p "Do you want to update your account (y/n)?: " updateAccount

		updateAccount=${updateAccount,,}

		if ( [ "$updateAccount" != "y" ] && [ "$updateAccount" != "yes" ] ); then
			break

		fi

		printf "\n\t\t"
		read -p "New Username : " newUsername

		printf "\t\t"
		read -p "New Password : " newPassword


		printf "\t\t"
		read -p "Press 'y' to confirm new account, press 'n' if not : " confirmNewAdminAccount

		confirmNewAdminAccount=${confirmNewAdminAccount,,}


		if ( [ "$confirmNewAdminAccount" != "y" ] && [ "$confirmNewAdminAccount" != "yes" ] ); then
			printf "\n"
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
function updateMovieDataInterface(){
	while true; do
		clear

		echo "--------------------------------------------------------------"
		printf "\t\tUPDATE MOVIES\n\n"


		printf "\t\t"
		echo "1.) ${movie1Descriptions[0]}"

		printf "\t\t"
		echo "2.) ${movie2Descriptions[0]}"

		printf "\t\t"
		echo "3.) ${movie3Descriptions[0]}"


		printf "\t\t"
		echo "4.) Exit"

		printf "\n\t\tPress enter key only to exit\n\t\t"
		read -p "Enter the movie number to be updated : " movieNum


		if [[ -z $movieNum ]]; then
			continue

		elif [[ $movieNum =~ [A-Za-z]+ ]]; then
			continue


		elif [[ $movieNum -le 0 ]]; then
			continue


		elif [[ $movieNum -ge 5 ]]; then
			continue


		elif [[ $movieNum -eq 1 ]]; then
			updateMovie1DataInterface "${movie1Descriptions[@]}" "${movie1TicketPrices[@]}"


		elif [[ $movieNum -eq 2 ]]; then
			updateMovie2DataInterface "${movie2Descriptions[@]}" "${movie2TicketPrices[@]}"


		elif [[ $movieNum -eq 3 ]]; then
			updateMovie3DataInterface "${movie3Descriptions[@]}" "${movie3TicketPrices[@]}"


		else
		
			break

		fi

	done
}



# Update movie 1 data interface
function updateMovie1DataInterface(){
	while true; do
		clear
		echo "--------------------------------------------------------------"
		printf "\t\tUPDATE MOVIE 1 DESCRIPTIONS\n\t\t"


		printf "\n\t\tPress enter key only to exit\n\t\t"
		read -p "Movie 1 Name : " newMovie1Name


		if [[ -z "$newMovie1Name" ]]; then
			break
		fi


		printf "\t\t"
		read -p "Movie 1 Genre : " newMovie1Genre

		printf "\n\t\t"
		echo "Ticket Prices"

		printf "\t\t"
		read -p "Row 1 ticket price : Php " movie1Row1TicketPrice

		printf "\t\t"
		read -p "Row 2 ticket price : Php " movie1Row2TicketPrice

		printf "\t\t"
		read -p "Row 3 ticket price : Php " movie1Row3TicketPrice


		printf "\t\t"
		read -p "Row 4 ticket price : Php " movie1Row4TicketPrice

		printf "\t\t"
		read -p "Row 5 ticket price : Php " movie1Row5TicketPrice


		printf "\t\t"
		read -p "Press 'y' to confirm the new movie, press 'n' if not : " confirmNewMovie1Descriptions

		confirmNewMovie1Descriptions=${confirmNewMovie1Descriptions,,}


		if ( [ "$confirmNewMovie1Descriptions" != "y" ] && [ "$confirmNewMovie1Descriptions" != "yes" ] ); then
			printf "\n"
			continue

		fi

		movie1Descriptions[0]="$newMovie1Name"
		movie1Descriptions[1]="$newMovie1Genre"
		movie1TicketPrices[0]="$movie1Row1TicketPrice"
		movie1TicketPrices[1]="$movie1Row2TicketPrice"
		movie1TicketPrices[2]="$movie1Row3TicketPrice"
		movie1TicketPrices[3]="$movie1Row4TicketPrice"
		movie1TicketPrices[4]="$movie1Row5TicketPrice"


		printf "\n\t\tSuccessfully Updated!\n\t\t"
		read -p "Press any key to exit interface : "
		break
	done
}



# Update movie 2 data interface
function updateMovie2DataInterface(){
	while true; do
		clear
		echo "--------------------------------------------------------------"
		printf "\t\tUPDATE MOVIE 2 DESCRIPTIONS\n\t\t"


		printf "\n\t\tPress enter key only to exit\n\t\t"
		read -p "Movie 2 Name : " newMovie2Name


		if [[ -z "$newMovie2Name" ]]; then
			break

		fi


		printf "\t\t"
		read -p "Movie 2 Genre : " newMovie2Genre

		printf "\n\t\t"
		echo "Ticket Prices"

		printf "\t\t"
		read -p "Row 1 ticket price : Php " movie2Row1TicketPrice

		printf "\t\t"
		read -p "Row 2 ticket price : Php " movie2Row2TicketPrice

		printf "\t\t"
		read -p "Row 3 ticket price : Php " movie2Row3TicketPrice


		printf "\t\t"
		read -p "Row 4 ticket price : Php " movie2Row4TicketPrice

		printf "\t\t"
		read -p "Row 5 ticket price : Php " movie2Row5TicketPrice


		printf "\t\t"
		read -p "Press 'y' to confirm the new movie, press 'n' if not : " confirmNewMovie2Descriptions

		confirmNewMovie2Descriptions=${confirmNewMovie2Descriptions,,}


		if ( [ "$confirmNewMovie2Descriptions" != "y" ] && [ "$confirmNewMovie2Descriptions" != "yes" ] ); then
			printf "\n"
			continue

		fi

		movie2Descriptions[0]="$newMovie2Name"
		movie2Descriptions[1]="$newMovie2Genre"

		movie2TicketPrices[0]="$movie2Row1TicketPrice"
		movie2TicketPrices[1]="$movie2Row2TicketPrice"
		movie2TicketPrices[2]="$movie2Row3TicketPrice"
		movie2TicketPrices[3]="$movie2Row4TicketPrice"
		movie2TicketPrices[4]="$movie2Row5TicketPrice"


		printf "\n\t\tSuccessfully Updated!\n\t\t"
		read -p "Press any key to exit interface : "
		break
	done
}



# Update movie 3 data interface
function updateMovie3DataInterface(){
	while true; do
		clear
		echo "--------------------------------------------------------------"
		printf "\t\tUPDATE MOVIE 3 DESCRIPTIONS\n\t\t"


		printf "\n\t\tPress enter key only to exit\n\t\t"
		read -p "Movie 3 Name : " newMovie3Name


		if [[ -z "$newMovie3Name" ]]; then
			break
		fi


		printf "\t\t"
		read -p "Movie 3 Genre : " newMovie3Genre

		printf "\n\t\t"
		echo "Ticket Prices"

		printf "\t\t"
		read -p "Row 1 ticket price : Php " movie3Row1TicketPrice

		printf "\t\t"
		read -p "Row 2 ticket price : Php " movie3Row2TicketPrice

		printf "\t\t"
		read -p "Row 3 ticket price : Php " movie3Row3TicketPrice


		printf "\t\t"
		read -p "Row 4 ticket price : Php " movie3Row4TicketPrice

		printf "\t\t"
		read -p "Row 5 ticket price : Php " movie3Row5TicketPrice


		printf "\t\t"
		read -p "Press 'y' to confirm the new movie, press 'n' if not : " confirmNewMovie3Descriptions

		confirmNewMovie3Descriptions=${confirmNewMovie3Descriptions,,}


		if ( [ "$confirmNewMovie3Descriptions" != "y" ] && [ "$confirmNewMovie3Descriptions" != "yes" ] ); then
			printf "\n"
			continue

		fi

		movie3Descriptions[0]="$newMovie3Name"
		movie3Descriptions[1]="$newMovie3Genre"

		movie3TicketPrices[0]="$movie3Row1TicketPrice"
		movie3TicketPrices[1]="$movie3Row2TicketPrice"
		movie3TicketPrices[2]="$movie3Row3TicketPrice"
		movie3TicketPrices[3]="$movie3Row4TicketPrice"
		movie3TicketPrices[4]="$movie3Row5TicketPrice"


		printf "\n\t\tSuccessfully Updated!\n\t\t"
		read -p "Press any key to exit interface : "
		break
	done
}



# Function to display movies data interface
function displayMoviesDataInterface(){
	# Displaying first movie data
	echo "--------------------------------------------------------------"

	printf "\t\tMOVIE 1 DESCRIPTIONS\n\n\t\t"

	echo "Title: ${movie1Descriptions[0]}"

	printf "\t\t"
	echo "Genre : ${movie1Descriptions[1]}"

	printf "\n\t\t"
	echo "TICKET PRICES:"
	printf "\n"

	row=0
	for ticketPrices in "${movie1TicketPrices[@]}"; do
		row=$(( row + 1 ))

		if [[ $row -eq 1 ]]; then
			printf "\t\tFirst row ticket price : Php "

		elif [[ $row -eq 2 ]]; then
			printf "\t\tSecond row ticket price : Php "

		elif [[ $row -eq 3 ]]; then
			printf "\t\tThird row ticket price : Php "

		elif [[ $row -eq 4 ]]; then
			printf "\t\tFourth row ticket price : Php "

		elif [[ $row -eq 5 ]]; then
			printf "\t\tFifth row ticket price : Php "

		fi

		echo "${ticketPrices}.00"
	done

	printf "\n\t\t"
	read -p "Press any key to load the next interface : "
	clear

	# Displaying second movie data
	echo "--------------------------------------------------------------"

	printf "\t\tMOVIE 2 DESCRIPTIONS\n\n\t\t"

	echo "Title: ${movie2Descriptions[0]}"

	printf "\t\t"
	echo "Genre : ${movie2Descriptions[1]}"

	printf "\n\t\t"
	echo "TICKET PRICES:"
	printf "\n"

	row=0
	for ticketPrices in "${movie2TicketPrices[@]}"; do
		row=$(( row + 1 ))

		if [[ $row -eq 1 ]]; then
			printf "\t\tFirst row ticket price : Php "

		elif [[ $row -eq 2 ]]; then
			printf "\t\tSecond row ticket price : Php "

		elif [[ $row -eq 3 ]]; then
			printf "\t\tThird row ticket price : Php "

		elif [[ $row -eq 4 ]]; then
			printf "\t\tFourth row ticket price : Php "

		elif [[ $row -eq 5 ]]; then
			printf "\t\tFifth row ticket price : Php "

		fi

		echo "${ticketPrices}.00"
	done


	printf "\n\t\t"
	read -p "Press any key to load the next interface : "
	clear

	# Displaying third movie data
	echo "--------------------------------------------------------------"

	printf "\t\tMOVIE 3 DESCRIPTIONS\n\n\t\t"

	echo "Title: ${movie3Descriptions[0]}"

	printf "\t\t"
	echo "Genre : ${movie3Descriptions[1]}"

	printf "\n\t\t"
	echo "TICKET PRICES:"
	printf "\n"

	row=0
	for ticketPrice in "${movie3TicketPrices[@]}"; do
		row=$(( row + 1 ))

		if [[ $row -eq 1 ]]; then
			printf "\t\tFirst row ticket price : Php "

		elif [[ $row -eq 2 ]]; then
			printf "\t\tSecond row ticket price : Php "

		elif [[ $row -eq 3 ]]; then
			printf "\t\tThird row ticket price : Php "

		elif [[ $row -eq 4 ]]; then
			printf "\t\tFourth row ticket price : Php "

		elif [[ $row -eq 5 ]]; then
			printf "\t\tFifth row ticket price : Php "

		fi

		echo "${ticketPrice}.00"
	done

	printf "\n\t\t"
	read -p "Press any key to load the interface : "
}



# Function for customer interface
function customerInterface(){
	while true; do
		# Boolean values to check if customer wants to reserve more movie seats
		reserveMovie1Seats=true
		reserveMovie2Seats=true
		reserveMovie3Seats=true

		# Variable to calculate the total prices per customer's chosen seats
		movie1TotalPrice=0
		movie2TotalPrice=0
		movie3TotalPrice=0


		clear
		echo "--------------------------------------------------------------"
		printf "\t\tMOVIE THEATRE\n\n"

		printf "\t\t"
		echo "1.) ${movie1Descriptions[0]}"

		printf "\t\t"
		echo "2.) ${movie2Descriptions[0]}"

		printf "\t\t"
		echo "3.) ${movie3Descriptions[0]}"

		printf "\t\t"
		echo "4.) Exit"

		printf "\n\t\t"
		read -p "Enter the movie number you want to watch : " movieNum


		if [[ -z $movieNum ]]; then
			continue


		elif [[ $movieNum =~ [A-Za-z]+ ]]; then
			continue


		elif [[ $movieNum -le 0 ]]; then
			continue


		elif [[ $movieNum -ge 5 ]]; then
			continue


		elif [[ $movieNum -eq 1 ]]; then
			reserveMovie1RowSeatsInterface "$reserveMovie1Seats" "${movie1Seats[@]}" "${movie1TicketPrices[@]}" $movie1TotalPrice


		elif [[ $movieNum -eq 2 ]]; then
			reserveMovie2RowSeatsInterface "$reserveMovie2Seats" "${movie2Seats[@]}" "${movie2TicketPries[@]}" $movie2TotalPrice


		elif [[ $movieNum -eq 3 ]]; then
			reserveMovie3RowSeatsInterface "$reserveMovie3Seats" "${movie3Seats[@]}" "${movie3TicketPrices[@]}" $movie3TotalPrice


		else
			break

		fi

	done
}



# Movie 1 row seats interface
function reserveMovie1RowSeatsInterface(){
	while true; do
		if [[ "$reserveMovie1Seats" == false ]]; then
			break
		fi

		clear
		echo "--------------------------------------------------------------"
		printf "\t\tMOVIE 1 THEATRE\n"

		printf "\n\t${movie1ColumnSeats[*]}"
		printf "\n\t${movie1Row1Seats[*]}"
		printf "\n\t${movie1Row2Seats[*]}"
		printf "\n\t${movie1Row3Seats[*]}"
		printf "\n\t${movie1Row4Seats[*]}"
		printf "\n\t${movie1Row5Seats[*]}"
		printf "\n\n\t\t"

		printf "Press enter to exit interface\n\t\t"
		read -p "Enter row : " row


		if [[ -z $row ]]; then
			break

		elif [[ $row =~ ^[A-Za-z]+$ ]]; then
			continue

		elif [[ $row -le 0 ]]; then
			continue

		elif [[ $row -ge 6 ]]; then
			continue


		else
			reserveMovie1ColumnSeatsInterface $row "$reserveMovie1Seats" "${movie1Seats[@]}" "${movie1TicketPrices[@]}" $movie1TotalPrice
			break

		fi

	done
}



# Movie 1 column seats interface
function reserveMovie1ColumnSeatsInterface(){
	while true; do
		printf "\t\t"
		read -p "Enter column : " column


		if [[ -z $column ]]; then
			break


		elif [[ $column =~ ^[A-Za-z]+$ ]]; then
			continue


		elif [[ $column -le 0 ]]; then
			continue

		elif [[ $column -ge 11 ]]; then
			continue


		fi


		if [[ $row -eq 1 ]] && [[ "${movie1Row1Seats[$column]}" != "[X]" ]]; then
			movie1Row1Seats[$column]="[X]"
			movie1TotalPrice=$(( movie1TotalPrice + "${movie1TicketPrices[0]}" ))


		elif [[ $row -eq 2 ]] && [[ "${movie1Row2Seats[$column]}" != "[X]" ]]; then
			movie1Row2Seats[$column]="[X]"
			movie1TotalPrice=$(( movie1TotalPrice + "${movie1TicketPrices[1]}" ))


		elif [[ $row -eq 3 ]] && [[ "${movie1Row3Seats[$column]}" != "[X]" ]]; then
			movie1Row3Seats[$column]="[X]"
			movie1TotalPrice=$(( movie1TotalPrice + "${movie1TicketPrices[2]}" ))


		elif [[ $row -eq 4 ]] && [[ "${movie1Row4Seats[$column]}" != "[X]" ]]; then
			movie1Row4Seats[$column]="[X]"
			movie1TotalPrice=$(( movie1TotalPrice + "${movie1TicketPrices[3]}" ))


		elif [[ $row -eq 5 ]] && [[ "${movie1Row5Seats[$column]}" != "[X]" ]]; then
			movie1Row5Seats[$column]="[X]"
			movie1TotalPrice=$(( movie1TotalPrice + "${movie1TicketPrices[4]}" ))

		else
			printf "\t\tSeat was already taken!\n\n\t"
			read -p "Press any key to load the interface again : "
			printf "\n"

			reserveMovie1RowSeatsInterface "$reserveMovie1Seats" "${movie1Seats[@]}" "${movie1TicketPrices[@]}" $movie1TotalPrice
			break

		fi

		clear
		echo "--------------------------------------------------------------"
		printf "\t\tMOVIE 1 THEATRE\n"

		# Display updated seats
		printf "\n\t${movie1ColumnSeats[*]}"
		printf "\n\t${movie1Row1Seats[*]}"
		printf "\n\t${movie1Row2Seats[*]}"
		printf "\n\t${movie1Row3Seats[*]}"
		printf "\n\t${movie1Row4Seats[*]}"
		printf "\n\t${movie1Row5Seats[*]}"

		askCustomerToReserveMoreMovie1Seats "$reserveMovie1Seats" "${movie1Seats[@]}" "${movie1TicketPrices[@]}" $movie1TotalPrice
		break

	done
}



# Function to ask customer if they want to reserve more seats for movie 1
function askCustomerToReserveMoreMovie1Seats(){
	while true; do
		printf "\n\n\t"
		read -p "Do you want to reserve more seats (y/n)?: " reserveMoreSeats

		reserveMoreSeats=${reserveMoreSeats,,}

		if ( [ $reserveMoreSeats != "n" ] && [ $reserveMoreSeats != "no" ] ); then
			reserveMovie1RowSeatsInterface "$reserveMovie1Seats" "${movie1Seats[@]}" "${movie1TicketPrices[@]}" $movie1TotalPrice

		else
			billingSys $movie1TotalPrice

		fi

		break

	done
}



# Movie 2 seats interface
function reserveMovie2RowSeatsInterface(){
	while true; do
		if [[ "$reserveMovie2Seats" == false ]]; then
			break
		fi

		clear
		echo "--------------------------------------------------------------"
		printf "\t\tMOVIE 2 THEATRE\n"

		printf "\n\t${movie2ColumnSeats[*]}"
		printf "\n\t${movie2Row1Seats[*]}"
		printf "\n\t${movie2Row2Seats[*]}"
		printf "\n\t${movie2Row3Seats[*]}"
		printf "\n\t${movie2Row4Seats[*]}"
		printf "\n\t${movie2Row5Seats[*]}"
		printf "\n\n\t\t"

		printf "Press enter to exit interface\n\t\t"
		read -p "Enter row : " row


		if [[ -z $row ]]; then
			break

		elif [[ $row =~ ^[A-Za-z]+$ ]]; then
			continue

		elif [[ $row -le 0 ]]; then
			continue

		elif [[ $row -ge 6 ]]; then
			continue

		else
			reserveMovie2ColumnSeatsInterface $row "$reserveMovie2Seats" "${movie2Seats[@]}" "${movie2TicketPrices[@]}" $movie2TotalPrice
			break
		fi
	done
}



# Movie 2 column seats interface
function reserveMovie2ColumnSeatsInterface(){
	while true; do
		printf "\t\t"
		read -p "Enter column : " column


		if [[ -z $column ]]; then
			break


		elif [[ $column =~ ^[A-Za-z]+$ ]]; then
			continue


		elif [[ $column -le 0 ]]; then
			continue

		elif [[ $column -ge 11 ]]; then
			continue

		fi


		if [[ $row -eq 1 ]] && [[ "${movie2Row1Seats[$column]}" != "[X]" ]]; then
			movie1Row1Seats[$column]="[X]"
			movie2TotalPrice=$(( movie2TotalPrice + "${movie2TicketPrices[0]}" ))


		elif [[ $row -eq 2 ]] && [[ "${movie2Row2Seats[$column]}" != "[X]" ]]; then
			movie2Row2Seats[$column]="[X]"
			movie2TotalPrice=$(( movie2TotalPrice + "${movie2TicketPrices[1]}" ))


		elif [[ $row -eq 3 ]] && [[ "${movie2Row3Seats[$column]}" != "[X]" ]]; then
			movie2Row3Seats[$column]="[X]"
			movie2TotalPrice=$(( movie2TotalPrice + "${movie2TicketPrices[2]}" ))


		elif [[ $row -eq 4 ]] && [[ "${movie2Row4Seats[$column]}" != "[X]" ]]; then
			movie2Row4Seats[$column]="[X]"
			movie2TotalPrice=$(( movie2TotalPrice + "${movie2TicketPrices[3]}" ))


		elif [[ $row -eq 5 ]] && [[ "${movie2Row5Seats[$column]}" != "[X]" ]]; then
			movie2Row5Seats[$column]="[X]"
			movie2TotalPrice=$(( movie2TotalPrice + "${movie2TicketPrices[4]}" ))


		else
			printf "\t\tSeat was already taken!\n\n\t"
			read -p "Press any key to load the interface again : "
			printf "\n"

			reserveMovie2RowSeatsInterface "$reserveMovie2Seats" "${movie2Seats[@]}" "${movie2TicketPrices[@]}" $movie2TotalPrice
			break

		fi

		clear
		echo "--------------------------------------------------------------"
		printf "\t\tCUSTOMER INTERFACE\n"

		# Display updated seats
		printf "\n\t${movie2ColumnSeats[*]}"
		printf "\n\t${movie2Row1Seats[*]}"
		printf "\n\t${movie2Row2Seats[*]}"
		printf "\n\t${movie2Row3Seats[*]}"
		printf "\n\t${movie2Row4Seats[*]}"
		printf "\n\t${movie2Row5Seats[*]}"

		askCustomerToReserveMoreMovie2Seats "$reserveMovie2Seats" "${movie2Seats[@]}" "${movie2TicketPrices[@]}" $movie2TotalPrice
		break

	done
}



# Ask customer to reserve more seats again for movie 2
function askCustomerToReserveMoreMovie2Seats(){
	while true; do
		printf "\n\n\t"
		read -p "Do you want to reserve more seats (y/n)?: " reserveMoreSeats

		reserveMoreSeats=${reserveMoreSeats,,}

		if ( [ $reserveMoreSeats != "n" ] && [ $reserveMoreSeats != "no" ] ); then
			reserveMovie2RowSeatsInterface "$reserveMovie2Seats" "${movie2Seats[@]}" "${movie2TicketPrices[@]}" $movie1TotalPrice

		else
			billingSys $movie2TotalPrice

		fi

		break

	done
}



# Movie 3 row seats interface
function reserveMovie3RowSeatsInterface(){
	while true; do
		if [[ "$reserveMovie3Seats" == false ]]; then
			break
		fi


		clear
		echo "--------------------------------------------------------------"
		printf "\t\tMOVIE 3 THEATRE\n"

		printf "\n\t${movie3ColumnSeats[*]}"
		printf "\n\t${movie3Row1Seats[*]}"
		printf "\n\t${movie3Row2Seats[*]}"
		printf "\n\t${movie3Row3Seats[*]}"
		printf "\n\t${movie3Row4Seats[*]}"
		printf "\n\t${movie3Row5Seats[*]}"
		printf "\n\n\t\t"

		printf "Press enter to exit interface\n\t\t"
		read -p "Enter row : " row


		if [[ -z $row ]]; then
			break

		elif [[ $row =~ ^[A-Za-z]+$ ]]; then
			continue

		elif [[ $row -le 0 ]]; then
			continue

		elif [[ $row -ge 6 ]]; then
			continue


		else
			reserveMovie3ColumnSeatsInterface $row "$reserveMovie3Seats" "${movie3Seats[@]}" "${movie3TicketPrices[@]}" $movie3TotalPrice
			break
		fi
	done

}



# Movie 3 column seats interface
function reserveMovie3ColumnSeatsInterface(){
	while true; do
		printf "\t\t"
		read -p "Enter column : " column


		if [[ -z $column ]]; then
			break

		elif [[ $column =~ ^[A-Za-z]+$ ]]; then
			continue

		elif [[ $column -le 0 ]]; then
			continue

		elif [[ $column -ge 11 ]]; then
			continue

		fi


		if [[ $row -eq 1 ]] && [[ "${movie3Row1Seats[$column]}" != "[X]" ]]; then
			movie3Row1Seats[$column]="[X]"
			movie3TotalPrice=$(( movie3TotalPrice + "${movie3TicketPrices[0]}" ))


		elif [[ $row -eq 2 ]] && [[ "${movie2Row2Seats[$column]}" != "[X]" ]]; then
			movie3Row2Seats[$column]="[X]"
			movie3TotalPrice=$(( movie3TotalPrice + "${movie3TicketPrices[1]}" ))


		elif [[ $row -eq 3 ]] && [[ "${movie3Row3Seats[$column]}" != "[X]" ]]; then
			movie3Row3Seats[$column]="[X]"
			movie3TotalPrice=$(( movie3TotalPrice + "${movie3TicketPrices[2]}" ))


		elif [[ $row -eq 4 ]] && [[ "${movie3Row4Seats[$column]}" != "[X]" ]]; then
			movie3Row4Seats[$column]="[X]"
			movie3TotalPrice=$(( movie3TotalPrice + "${movie3TicketPrices[3]}" ))


		elif [[ $row -eq 5 ]] && [[ "${movie3Row5Seats[$column]}" != "[X]" ]]; then
			movie3Row5Seats[$column]="[X]"
			movie3TotalPrice=$(( movie3TotalPrice + "${movie3TicketPrices[4]}" ))


		else
			printf "\t\tSeat was already taken!\n\n\t"
			read -p "Press any key to load the interface again : "
			printf "\n"

			reserveMovie3RowSeatsInterface "$reserveMovie3Seats" "${movie3Seats[@]}" "${movie3TicketPrices[@]}" $movie3TotalPrice
			break
		fi

		clear
		echo "--------------------------------------------------------------"
		printf "\t\tCUSTOMER INTERFACE\n"

		# Display updated seats
		printf "\n\t${movie3ColumnSeats[*]}"
		printf "\n\t${movie3Row1Seats[*]}"
		printf "\n\t${movie3Row2Seats[*]}"
		printf "\n\t${movie3Row3Seats[*]}"
		printf "\n\t${movie3Row4Seats[*]}"
		printf "\n\t${movie3Row5Seats[*]}"

		askCustomerToReserveMoreMovie3Seats "$reserveMovie3Seats" "${movie3Seats[@]}" "${movie3TicketPrices[@]}" $movie3TotalPrice
		break
	done
}



# Ask customer if they want to reserve more movie 3 seats
function askCustomerToReserveMoreMovie3Seats(){
	while true; do
		printf "\n\n\t"
		read -p "Do you want to reserve more seats (y/n)?: " reserveMoreSeats

		reserveMoreSeats=${reserveMoreSeats,,}

		if ( [ $reserveMoreSeats != "n" ] && [ $reserveMoreSeats != "no" ] ); then
			reserveMovie3RowSeatsInterface "$reserveMovie3Seats" "${movie3Seats[@]}" "${movie3TicketPrices[@]}" $movie3TotalPrice

		else
			billingSys $movie3TotalPrice

		fi

		break
	done
}



# Billing Function
function billingSys(){
	local totalPrice="$1"

	while true; do
		clear
		echo "--------------------------------------------------------------"
		printf "\t\tBILLING INTERFACE\n\n"

		printf "\t\tTotal Price : Php ${totalPrice}.00\n\t\t"
		read -p "Enter your payment here : Php " userPayment

		if [[ $userPayment -lt $totalPrice ]]; then
			printf "\n\t\tInsufficient Money!\n\t\t"
			read -p "Press any key to load the interface : "
			printf "\n"
			continue

		else
			change=$(( $userPayment - $totalPrice ))
			printf "\n\t\tChange : Php ${change}.00\n\t\t"

			read -p "Press any key to load the interface : "
			break
		fi
	done
}



# Admin's username and password
adminData=("admin" "admin")


# Movie 1 seats, descriptions, and ticket prices
movie1ColumnSeats=(" " " 1 " " 2 " " 3 " " 4 " " 5 " " 6 " " 7 " " 8 " " 9 " " 10 ")
movie1Row1Seats=("1" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie1Row2Seats=("2" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie1Row3Seats=("3" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie1Row4Seats=("4" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie1Row5Seats=("5" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")

movie1Seats=("${movie1ColumnSeats[@]}" "${movie1Row1Seats[@]}" "${movie1Row2Seats[@]}" "${movie1Row3Seats[@]}" "${movie1Row4Seats[@]}" "${movie1Row5Seats[@]}")	

movie1Descriptions=("Venom : The Last Dance" "Sci-Fi, Action, and Horror")
movie1TicketPrices=(500 450 400 350 300)


# Movie 2 seats, descriptions, and ticket prices
movie2ColumnSeats=(" " " 1 " " 2 " " 3 " " 4 " " 5 " " 6 " " 7 " " 8 " " 9 " " 10 ")
movie2Row1Seats=("1" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie2Row2Seats=("2" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie2Row3Seats=("3" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie2Row4Seats=("4" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie2Row5Seats=("5" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")


movie2Seats=("${movie2ColumnSeats[@]}" "${movie2Row1Seats[@]}" "${movie2Row2Seats[@]}" "${movie2Row3Seats[@]}" "${movie2Row4Seats[@]}" "${movie2Row5Seats[@]}")	

movie2Descriptions=("Haikyuu : The Dumpster Battle" "Sports, Actions, and High-School")
movie2TicketPrices=(600 550 500 450 400)


# Movie 3 seats, descriptions, and ticket prices
movie3ColumnSeats=(" " " 1 " " 2 " " 3 " " 4 " " 5 " " 6 " " 7 " " 8 " " 9 " " 10 ")
movie3Row1Seats=("1" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie3Row2Seats=("2" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie3Row3Seats=("3" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie3Row4Seats=("4" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")
movie3Row5Seats=("5" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]" "[ ]")


movie3Seats=("${movie3ColumnSeats[@]}" "${movie3Row1Seats[@]}" "${movie3Row2Seats[@]}" "${movie3Row3Seats[@]}" "${movie3Row4Seats[@]}" "${movie3Row5Seats[@]}")	

movie3Descriptions=("Hello, Love, Again" "Drama and Romance")
movie3TicketPrices=(700 650 600 550 500)


# Execute the main interface function
clear
mainInterface "${adminData[@]}" "${movie1Seats[@]}" "${movie1Descriptions[@]}" "${movie1TicketPrices[@]} ${movie2Seats[@]} ${movie2Descriptions[@]} ${movie2TicketPrices[@]} ${movie3Seats[@]} ${movie3Descriptions[@]} ${movie3TicketPrices[@]}"
clear

