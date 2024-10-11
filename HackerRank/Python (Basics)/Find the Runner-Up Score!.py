# Function to get the second highest number
def find_runner_up(nums):
    # Remove duplicates for easy fetching of second highest number
    non_duplicate_nums = list(set(nums))

    # Sort to ascending order
    sorted_nums = sorted(non_duplicate_nums)

    # Get the second highest value
    print(sorted_nums[-2])



if __name__ == '__main__':
    # N score
    n = int(input())
    # List of scores
    arr = map(int, input().split())
    
    # Execute the function
    find_runner_up(arr)
