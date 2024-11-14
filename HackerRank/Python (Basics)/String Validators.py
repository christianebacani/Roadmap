# Question Name : String Validators
# Category Name : Python (Basics)
# Sub-Category Name : Strings

def validateString(s):
    # Storing the booleans
    boolList = []


    anyAlphaNum = []
    anyAlpha = []
    anyDigit = []
    anyLower = []
    anyUpper = []

    # Check if any characters are alphanumeric
    for char in s:
        if char.isalnum():
            anyAlphaNum.append(True)
        else:
            anyAlphaNum.append(False)

    # Check if any characters are alphabetic
    for char in s:
        if char.isalpha():
            anyAlpha.append(True)
        else:
            anyAlpha.append(False)

    # Check if any characters are digit
    for char in s:
        if char.isdigit():
            anyDigit.append(True)
        else:
            anyDigit.append(False)
        
    # Check if any characters are lowercase
    for char in s:
        if char.islower():
            anyLower.append(True)
        
        else:
            anyLower.append(False)
    
    # Check if any characters are uppercase
    for char in s:
        if char.isupper():
            anyUpper.append(True)
        else:
            anyUpper.append(False)
    

    # Stores the final boolean value to check if any characters are alphanumeric, alphabetic, digit, lower, and uppercase
    boolList = [any(anyAlphaNum), any(anyAlpha), any(anyDigit), any(anyLower), any(anyUpper)]
    
    for bool in boolList:
        print(bool)


if __name__ == '__main__':
    s = input()
    validateString(s)
