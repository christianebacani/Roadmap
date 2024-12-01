# Question Name : Capitalize()
# Category Name : Python (Basics)
# Sub-Category Name : Strings
 
#!/bin/python3
import os 

# Complete the solve function below
def solve(s):
    # Convert the string of first name and last name to capitalize strings
    list = s.split(' ')
    stringCapitalize = [word.capitalize() for word in list]
    stringCapitalize = ' '.join(stringCapitalize)
    return stringCapitalize


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = solve(s) 
    fptr.write(result + '\n')
    fptr.close()