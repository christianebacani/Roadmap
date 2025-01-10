# Function to squared every iteration
def squared_num(nums):
    # Loop through each iteration of number
    for i in range(nums):
        # Check if the num is not negative
        if i >= 0:
            # Squared every iteration
            result = i ** 2
            print(result) # Display the result
            # Increment
            i += 1


# Main functions
if __name__ == '__main__':
    n = int(input())
    squared_num(n)



