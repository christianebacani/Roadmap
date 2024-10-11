# Function to get the second highest number
def find_runner_up(nums):
    # Non duplicate array
    data = []

    # Iterate through the loop
    for i in nums:
        # Check if the current iteration is not present to the non duplicate array
        if i not in data:
            # Store the current iteration to the non-duplicate array
            data.append(i)

    # Sorted to ascending and get the second highest value
    print(sorted(data)[-2])

 

if __name__ == '__main__':
    # N score
    n = int(input())
    # List of scores
    arr = map(int, input().split())
    
    # Execute the function
    find_runner_up(arr)
