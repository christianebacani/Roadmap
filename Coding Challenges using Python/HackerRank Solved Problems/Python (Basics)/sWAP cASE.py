# Question Name : sWAP cASE
# Question Category : Python (Basic)
# Question Sub-Category : Strings

# Function to swap case
def swap_case(s):
    word = ''

    # Check every char if it's lower or upper then invert
    for char in s:
        if char.islower():
            char = char.upper()
                        
        else:
            char = char.lower()
        
        word += char

    return word

# Execute the function
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

