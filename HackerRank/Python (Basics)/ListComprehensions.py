# List Comprehension Funtion
def list_comprehension(a, b, c, num):
    # List comprehension using two inner loops
    result = [[i, j, k] for i in range(a + 1) for j in range(b + 1) for k in range(c + 1) if (i + j + k) != num]    
    # Display the permutations
    print(result)

# Check if the script is running directly
if __name__ == '__main__':
    # Enter integer
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Call the function
    list_comprehension(x, y, z, n)