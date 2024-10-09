# Print function
def printFunc(num):
    # Display the iteration starting from 1 to n(inclusive) (ex: n = 3 : 123)
    for i in range(1, num + 1):
        print(i, end='')
    

# Check if the script is running directly
if __name__ == '__main__':
    n = int(input())

    # Execute the function
    printFunc(n)



