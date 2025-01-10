# Question Name : String Formatting
# Category Name : Python (Basics)
# Sub-Category Name : Strings

def print_formatted(number):
    binaryNumber = (str(bin(number)).replace('0b', ''))
    spacePad = len(binaryNumber)

    for i in range(1, number + 1):
        decimal = str(i) 
        octal = str(oct(i)).replace('0o', '')
        hexadecimal = str(hex(i)).replace('0x', '').upper()
        binary = str(bin(i)).replace('0b', '')

        # Display the current iteration that is right padded with the maximum width of the binary value of the number
        print(decimal.rjust(spacePad), octal.rjust(spacePad), hexadecimal.rjust(spacePad), binary.rjust(spacePad)) # Note : Separated by single space ','
        
if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
