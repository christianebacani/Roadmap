# Question: Status Arrays
# Categories: 7 Kyu

def status(nums: list[int]) -> list[int]:
    status_and_number = []

    for i in range(len(nums)):
        position = i
        count = 0

        for j in range(len(nums)):
            if i != j and nums[i] > nums[j]:
                count += 1
        
        status_and_number.append([position + count, nums[i]])
    
    sorted_distinct_status = []
    
    for i in range(len(status_and_number)):
        sorted_distinct_status.append(status_and_number[i][0])
    
    sorted_distinct_status = sorted(list(set(sorted_distinct_status)))
    result = []

    for i in range(len(sorted_distinct_status)):
        numbers_with_same_status = []

        for j in range(len(status_and_number)):
            if sorted_distinct_status[i] == status_and_number[j][0]:
                numbers_with_same_status.append(status_and_number[j][1])
        
        result.extend(numbers_with_same_status)
    
    return result