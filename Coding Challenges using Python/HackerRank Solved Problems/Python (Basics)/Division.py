# Function to divide two int and return integer
def divide_int(x, y):
    return int(x / y)

# Function to divide two int and return float
def divide_float(x, y):
    return x / y

# Main function
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    # Execute the functions
    print(divide_int(a, b))
    print(divide_float(a, b))
