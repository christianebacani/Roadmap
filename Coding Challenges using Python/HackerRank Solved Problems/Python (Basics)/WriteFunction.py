# Function to check if the year is a leap year or not
def is_leap(year):
    # Initialize the variable to determine if the year is leap year or not
    leap = False
    
    # It is a Leap Year if it's divisible by 4
    if (year % 4) == 0:
        leap = True
        # If it's divisible by 100 also, then it is not a Leap Year
        if (year % 100) == 0:
            leap = False
            
            # If it's divisible by 400 also, then it is a Leap Year
            if (year % 400) == 0:
                leap = True

    # Return the value
    return leap

# Execute the function
year = int(input())
print(is_leap(year))


